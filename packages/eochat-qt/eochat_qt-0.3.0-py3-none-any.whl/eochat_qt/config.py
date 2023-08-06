from eochat_qt.helpers import *

from shutil import copyfile
import os

is_win = is_windows()

LOG_CFG_PATH_WINDOWS    = r'%APPDATA%\eochat\eo_chat-qt\logs'
LOG_CFG_PATH_LINUX      = '~/.config/eochat/eo_chat-qt/logs'

def override_values(default, cmp1, cmp2):
    res = default
    if cmp1 is not None:
        res = cmp1
    elif cmp2 is not None:
        res = cmp2
    return res

def toggle_chat_logging(cfg):
    use_logging = True # Toggle logging by default
    CFG_LOGGING = cfg.get('logging')
    logging = override_values(use_logging, CFG_LOGGING, None)
    return logging

def get_log_name(log_name):
    global LOG_CFG_PATH_LINUX, LOG_CFG_PATH_WINDOWS
    logdir = expand(LOG_CFG_PATH_WINDOWS) if is_win else expand(LOG_CFG_PATH_LINUX)
    if (not logdir.exists()):
        os.makedirs(logdir, exist_ok = True)
    log_name = f'{logdir}\\{log_name}' if is_win else f'{logdir}/{log_name}'
    return log_name

def parse_user_cfg():
    ''' Parse the user's config file '''
    CFG_PATH_WINDOWS    = r'%APPDATA%\eochat\config.toml'
    CFG_PATH_LINUX      = '~/.config/eochat/config.toml'

    cfgfp = expand(CFG_PATH_WINDOWS) if is_win else expand(CFG_PATH_LINUX)

    # If the user config file does not exist
    if (not cfgfp.exists()):
        # Copy our example config over to where it should exist
        os.makedirs(os.path.dirname(cfgfp), exist_ok = True)
        copyfile(f'{Path(__file__).resolve().parents[2]}/config.toml', cfgfp)

    return read_cfg(cfgfp)

def parse_user_appearance(cfg):
    return cfg['character']['appearance'] # Mandatory field

def parse_user_tsformat(cfg):
    DEFAULT_TIMESTAMP_FMT = '"%I:%M %p"' # 10:30 AM
    CFG_TSFORMAT = cfg.get('tsformat')
    fmt = override_values(DEFAULT_TIMESTAMP_FMT, CFG_TSFORMAT, None)
    return fmt

def parse_user_logformat(cfg):
    DEFAULT_TIMESTAMP_FMT   = '%Y-%m-%d %H:%M:%S' # '2022-08-25 22:27:08'
    DEFAULT_LOG_FILE_FMT    = '%Y-%m-%d'

    TIMESTAMP_FMT   = DEFAULT_TIMESTAMP_FMT
    LOG_FILE_FMT    = DEFAULT_LOG_FILE_FMT

    cfg_eochat_qt = cfg.get('eochat-qt')
    if (cfg_eochat_qt):
        cfg_log = cfg_eochat_qt.get('log')
        if (cfg_log):
            cfg_tsformat = cfg_log.get('tsformat')
            cfg_fpformat = cfg_log.get('fpformat')

            TIMESTAMP_FMT = cfg_tsformat
            LOG_FILE_FMT = cfg_fpformat

    log_name = f'chat-{timestamp(LOG_FILE_FMT)}'
    logfp = get_log_name(log_name)
    return log_name, logfp, LOG_FILE_FMT, TIMESTAMP_FMT

def parse_user_creds(cfg):
    ''' Parse the user's login credentials '''
    # Read environment variables
    OUTPOST_USER    = os.environ.get('OUTPOST_USER')
    OUTPOST_PASS    = os.environ.get('OUTPOST_PASSWORD')

    # Read config variables
    CFG_USER        = cfg.get('user')
    CFG_PASS        = cfg.get('password')

    user        = override_values('', OUTPOST_USER, CFG_USER)
    password    = override_values('', OUTPOST_PASS, CFG_PASS)
    return user, password

def select_host(host):
    return (True if host == 'main' else False)

def parse_user_host(cfg):
    # Default
    host = 'main'

    # Read from config file
    CFG_HOST = cfg.get('host')

    host = override_values(host, CFG_HOST, None)

    which       = select_host(host)
    AUTH_HOST   = 'auth.everfree-outpost.com' if which else 'localhost:5000'
    AUTH_BASE   = f'https://{AUTH_HOST}'
    AUTH_ORIGIN = 'http://play.everfree-outpost.com' if which else 'http://localhost:8889'
    GAME_URL    = 'ws://game2.everfree-outpost.com:8888/ws' if which else 'ws://localhost:8888/ws'
    return AUTH_HOST, AUTH_BASE, AUTH_ORIGIN, GAME_URL

