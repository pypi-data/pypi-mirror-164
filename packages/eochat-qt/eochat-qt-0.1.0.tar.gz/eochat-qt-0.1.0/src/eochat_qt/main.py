# Imports
import sys

# TODO: Quick hack to import the eochat module without making a proper setup.py file
from os.path import dirname
sys.path.append(dirname('eoclichat/src/eochat'))

# from eoclichat.src.eochat.periodic import *
# from eoclichat.src.eochat.processer import *
# from eoclichat.src.eochat.builder import *
# import eoclichat.src.eochat.crypto as crypto

from eochat.periodic import *
from eochat.processer import *
from eochat.builder import *
import eochat.crypto as crypto


# Third Party Libaries
from tornado.platform.asyncio import to_asyncio_future
import tornado.websocket
import tornado.platform.asyncio
import tornado.httpclient

# Standard Library Imports
from collections import deque
import asyncio
import base64
import struct
import urllib.parse
import json
import threading

# PySide6 library imports
from PySide6.QtWidgets import QApplication

import mainwindow

from helpers import *
from config import *
from eo_defs import *

# Configure variables
cfg             = parse_user_cfg()
user, password  = parse_user_creds(cfg)
appearance      = parse_user_appearance(cfg)
tsformat        = parse_user_tsformat(cfg)
# logfile,logformat = parse_user_logformat(cfg)
log_name, logfp, LOG_FILE_FMT, LOG_TIMESTAMP_FMT = parse_user_logformat(cfg)
logging         = toggle_chat_logging(cfg)
AUTH_HOST, AUTH_BASE, AUTH_ORIGIN, GAME_URL = parse_user_host(cfg)

# GUI
RESOURCES_DIR   = 'resources'
MAIN_UI_FILE    = f'{RESOURCES_DIR}/mainwindow.ui'

message_obtained = False

# Start up the GUI
# This must be started before the mainwindow call
app = QApplication(sys.argv)

# Global singleton
MAIN_WINDOW: mainwindow.MainWindow

# Log a message to stdout, and the gui
def display(message):
    global mainwindow, log_name, logfp, LOG_TIMESTAMP_FMT, LOG_FILE_FMT

    log_ts  = timestamp(LOG_TIMESTAMP_FMT)
    ts      = timestamp(tsformat)

    # Strip " characters
    log_ts = log_ts.strip('\"')
    ts = ts.strip('\"')

    # Format messages
    log_fmt = f'[{log_ts}] {message}'
    fmt = f'[{ts}] {message}'

    # Print to stdout and to the gui
    print(fmt)
    MAIN_WINDOW.new_message(fmt)

    if logging:
        current_day = f'chat-{timestamp(LOG_FILE_FMT)}'

        # Rotate log if its already new day
        if (current_day > log_name):
            # Lexicographically compare these formats
            # Since they're ordered like this:
            # d1: chat-2022-08-25
            # d2: chat-2022-08-26
            # We can directly compare them across to find out if a new day has passed
            log_name = current_day # Log to a new file
            logfp = get_log_name(log_name)

        # Write file
        with open(logfp, 'a') as log:
            log.write(log_fmt)
            log.write('\n')

def get_ui_input():
    return MAIN_WINDOW.send_message()

# def log(message):
    # if logging:
        # # TODO: Rotate the log

        # # If time is close to but before midnight

        # # We assume that the log file format doesn't change for simplicity
        # # Lexicographically order logs
        # if ()
        # # Append message to log
        # with open(logfp, 'a') as log:
            # log.write(message)


async def do_login(user, password):
    auth_client = tornado.httpclient.AsyncHTTPClient()

    args    = { 'name': user, 'password': password}
    headers = { 'Host': AUTH_HOST, }
    resp = await auth_client.fetch(f'{AUTH_BASE}/login', method='POST',
                                   body=urllib.parse.urlencode(args), headers=headers,
                                   follow_redirects=False, raise_error=False)
    assert resp.code == 302
    cookie = resp.headers['Set-Cookie'].partition(';')[0]
    return cookie

async def get_response(challenge, cookie):
    auth_client = tornado.httpclient.AsyncHTTPClient()

    headers = {
        'Origin': AUTH_ORIGIN,
        'Host': AUTH_HOST,
        'Cookie': cookie,
    }
    body = json.dumps({
        'challenge': base64.urlsafe_b64encode(challenge).decode('ascii'),
    })
    resp = await auth_client.fetch(f'{AUTH_BASE}/api/sign_challenge', method='POST',
                                   body=body, headers=headers)
    j = json.loads(resp.body.decode('ascii'))
    assert j['status'] == 'ok'
    return base64.urlsafe_b64decode(j['response'].encode('ascii'))

async def do_auth(conn, cookie):
    response = await to_asyncio_future(get_response(conn.cb_token, cookie))
    await conn.send(struct.pack('<H', OP_AUTH_RESPONSE) + response)

    while True:
        msg = await to_asyncio_future(conn.recv())
        if msg is None:
            assert False, 'server disconnected unexpectedly'
        opcode, = struct.unpack('<H', msg[:2])

        if opcode == OP_AUTH_RESULT:
            flags, = struct.unpack('<H', msg[2:4])
            if flags == 1:
                name = msg[4:].decode('ascii')
                return name
            else:
                assert False, 'bad auth result: %s' % flags

        else:
            assert False, 'bad opcode: %x' % opcode


async def sender(conn):
    global message_obtained
    try:
        while True:
            # TODO: Fix this to become a nonblocking call
            await asyncio.sleep(1)
            while message_obtained:
                msg = get_ui_input()
                await conn.send(build_chat(msg))
                message_obtained = False
                MAIN_WINDOW.clear_input()
                break;
    finally:
        asyncio.get_event_loop().stop()

async def receiver(conn):
    try:
        while True:
            msg = await to_asyncio_future(conn.recv())
            if msg is None:
                display("Disconnected from server")
                assert False, 'server disconnected'
            op, msg = decode_message(msg)

            if op == CHAT_UPDATE:
                # Indicate local chat messages with (local)
                msg = msg.split('\t')
                msg[2] = " (local)" if (msg[2] == "27686") else ""
                display(f'{msg[0]}{msg[2]}: {msg[1]}')

    finally:
        asyncio.get_event_loop().stop()

class EncryptedSocket:
    def __init__(self):
        self.conn = None
        self.proto = None
        self.recv_queue = deque()
        self.cb_token = None

    async def connect(self, url):
        self.conn = await to_asyncio_future(tornado.websocket.websocket_connect(url))
        self.proto = crypto.Protocol(initiator=True)

        # Perform handshake
        self.proto.open()
        while True:
            evt = self.proto.next_event()
            if evt is None:
                msg = await to_asyncio_future(self.conn.read_message())
                self.proto.incoming(msg)
            elif isinstance(evt, crypto.RecvEvent):
                self.recv_queue.append(evt.data)
            elif isinstance(evt, crypto.OutgoingEvent):
                self.conn.write_message(evt.data, binary=True)
            elif isinstance(evt, crypto.HandshakeFinishedEvent):
                self.cb_token = evt.cb_token
                return
            elif isinstance(evt, crypto.ErrorEvent):
                raise ValueError('crypto error: %s' % evt.message)
            else:
                assert False, 'unknown event type in connect: %r' % (evt,)

    async def recv(self):
        if len(self.recv_queue) > 0:
            return self.recv_queue.popleft()

        while True:
            evt = self.proto.next_event()
            if evt is None:
                msg = await to_asyncio_future(self.conn.read_message())
                self.proto.incoming(msg)
            elif isinstance(evt, crypto.RecvEvent):
                return evt.data
            elif isinstance(evt, crypto.OutgoingEvent):
                self.conn.write_message(evt.data, binary=True)
            elif isinstance(evt, crypto.ErrorEvent):
                raise ValueError('crypto error: %s' % evt.message)
            else:
                assert False, 'unexpected event type in recv: %r' % (evt,)

    async def send(self, data):
        self.proto.send(data)

        while True:
            evt = self.proto.next_event()
            if evt is None:
                return
            elif isinstance(evt, crypto.RecvEvent):
                self.recv_queue.append(evt.data)
            elif isinstance(evt, crypto.OutgoingEvent):
                self.conn.write_message(evt.data, binary=True)
            elif isinstance(evt, crypto.ErrorEvent):
                raise ValueError('crypto error: %s' % evt.message)
            else:
                assert False, 'unexpected event type in send: %r' % (evt,)



async def amain(user, password):
    display('Logging in as %r...' % user)
    cookie = await to_asyncio_future(do_login(user, password))
    display(f'Cookie: \'{cookie}\'')
    display('Connecting...')

    conn = EncryptedSocket()
    await conn.connect(GAME_URL)
    display(f'Challenge: \'{conn.cb_token}\'')
    display('Authenticating...')

    name = await do_auth(conn, cookie)
    display(f'Connected as {name}')

    await conn.send([22,0]) # Send start header
    await conn.send(build_appearance(*appearance)) # With custom appearance

    asyncio.get_event_loop().create_task(receiver(conn))
    asyncio.get_event_loop().create_task(sender(conn))
    asyncio.get_event_loop().create_task(iping(conn))

    display("Connected to Server")

# Load the mainwindow
def init_mainwindow(loader, ui_file):
    global MAIN_WINDOW
    MAIN_WINDOW = mainwindow.MainWindow(loader.load(ui_file))
    ui_file.close()
    if not MAIN_WINDOW:
        print(loader.errorString())
        sys.exit(-1)
    MAIN_WINDOW.show()

def main():
    # Initialize QT6 components
    init_mainwindow(*mainwindow.init_qt_uic_loader(MAIN_UI_FILE))

    tornado.platform.asyncio.AsyncIOMainLoop().install()
    asyncio.get_event_loop().create_task(amain(user, password))

    # Start event loop on separate thread to main loop
    t = threading.Thread(target=asyncio.get_event_loop().run_forever, args=())
    t.daemon = True
    t.start()

    # App must be started on main thread
    app.exec()
