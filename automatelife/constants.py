import os
from pathlib import Path

CONFIG_DIR = Path.home()

# TODO: The checks are not that good, some fixes might be needed.
if os.name == "nt":
    import ctypes.wintypes

    CSIDL_PERSONAL = 5
    SHGFP_TYPE_CURRENT = 0
    buf = ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
    ctypes.windll.shell32.SHGetFolderPathW(
        0, CSIDL_PERSONAL, 0, SHGFP_TYPE_CURRENT, buf
    )
    DEFAULT_PROJECTS_DIR = Path(buf.value) / "Projects"
    CONFIG_DIR = CONFIG_DIR / "AppData/Roaming"
elif os.name == "posix":
    DEFAULT_PROJECTS_DIR = Path.home() / "Projects"
    CONFIG_DIR = CONFIG_DIR / ".local/share"
else:
    DEFAULT_PROJECTS_DIR = Path("Projects")
    CONFIG_DIR = CONFIG_DIR / "Library/Application Support"

CONFIG_FILE = CONFIG_DIR / "automatelife"
CONFIG_FILE /= ".config.json"

STATIC_DIR = Path(__file__).resolve().parent / "static"
TEMPLATES_DIR = STATIC_DIR / "templates"
DEFINITIONS_DIR = STATIC_DIR / "definitions"

DEFAULT_GITIGNORE = ["visualstudiocode"]
GITIGNORE_URL = "https://www.gitignore.io/api/"
