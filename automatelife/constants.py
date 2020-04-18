import os
from pathlib import Path

if os.name == "nt":
    import ctypes.wintypes
    CSIDL_PERSONAL = 5
    SHGFP_TYPE_CURRENT = 0
    buf = ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
    ctypes.windll.shell32.SHGetFolderPathW(0, CSIDL_PERSONAL, 0, SHGFP_TYPE_CURRENT, buf)
    DEFAULT_PROJECTS_DIR = Path(buf.value) / "Projects"
elif os.name == "posix":
    DEFAULT_PROJECTS_DIR = Path.home() / "Projects"
else:
    DEFAULT_PROJECTS_DIR = Path("Projects")

TEMPLATES_DIR = Path(__file__).resolve().parent / "templates"
LANGUAGES_DIR = TEMPLATES_DIR / "languages"

DEFAULT_GITIGNORE = ["visualstudiocode"]
GITIGNORE_URL = "https://www.gitignore.io/api/"
