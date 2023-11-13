import os
from configparser import ConfigParser
from pathlib import Path
from zut import ExtendedConfigParser

def get_user_config_path():
    return Path(f'~/AppData/Local/CMDBase/cmdbase.conf' if os.name == 'nt' else f'~/.local/cmdbase/cmdbase.conf').expanduser()

def read_config(config: ConfigParser):
    config.read([
        # System configuration
        Path(f'C:/ProgramData/cmdbase.conf' if os.name == 'nt' else f'/etc/cmdbase.conf').expanduser(),
        # User configuration
        get_user_config_path(),
        # Local configuration
        "local.conf",
    ], encoding='utf-8')

CONFIG = ExtendedConfigParser()
read_config(CONFIG)

OUT_BASE_DIR = Path(CONFIG.get('cmdbase', 'out_base_dir', fallback='local'))
