from datetime import datetime
from pathlib import Path
import toml
import platform

# Helper functions
def read_file(fname: str) -> str:
    file = open(fname, 'r')
    res = file.read()
    file.close()
    return res

def timestamp(fmt_str):
    ''' Format timestamps for the current datetime '''
    return datetime.now().strftime(fmt_str)

def read_cfg(cfgfp):
    return toml.loads(read_file(cfgfp))

def expand(path):
    return Path(path).expanduser()

def is_windows():
    return any(platform.win32_ver())
