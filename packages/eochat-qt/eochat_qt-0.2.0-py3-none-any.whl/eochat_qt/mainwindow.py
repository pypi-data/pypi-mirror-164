from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QFile, QIODevice, QObject, Slot, Signal

import asyncio
import sys

# Load UI file directly from file
def init_qt_uic_loader(filepath):
    ui_file = QFile(filepath)
    if not ui_file.open(QIODevice.ReadOnly):
        print(f"Cannot open {filepath}: {ui_file.errorString()}")
        sys.exit(-1)
    loader = QUiLoader()
    return loader, ui_file

# Relay messages to/from QT widgets
class MessageBus(QObject):
    te_messages_received = Signal(bool)
    te_messages_updated = Signal(bool)

class MainWindow(QMainWindow):
    def __init__(self, qwidget):
        super(MainWindow, self).__init__()
        self.messages = list(str())
        self.qwidget = qwidget

        self.setCentralWidget(self.qwidget)
        self.mbus = MessageBus()

        # When we receive a new message, show all new messages
        self.mbus.te_messages_received.connect(self.show_messages)

        # When we update messages, emit new message signal
        self.mbus.te_messages_updated.connect(self.new_message)

        # self.mbus.le_input_send.connect(self.send_message)
        self.qwidget.pb_send.clicked.connect(self.send_message)

    @Slot(bool)
    def new_message(self, message):
        self.messages.append(message)
        self.mbus.te_messages_received.emit(True)

    @Slot(bool)
    def show_messages(self):
         msgs = '\n'.join(self.messages)
         self.qwidget.te_messages.setText(msgs)

    def send_message(self):
        global message_obtained
        msg = self.qwidget.le_input.text()
        message_obtained = True
        return msg

    def clear_input(self):
        self.qwidget.le_input.clear()

    def __del__(self):
        # Exit eo asyncio thread on program quit
        asyncio.get_event_loop().close()

