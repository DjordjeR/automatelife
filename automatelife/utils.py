import string
import unicodedata
import urllib.request
from pathlib import Path

from .constants import GITIGNORE_URL

"""
TAKEN FROM START:
Url: https://gist.github.com/wassname/1393c4a57cfcbf03641dbc31886123b8
"""

_valid_filename_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
_char_limit = 255


def clean_filename(filename, whitelist=_valid_filename_chars, replace=" "):
    # replace spaces
    for r in replace:
        filename = filename.replace(r, "_")

    # keep only valid ascii chars
    cleaned_filename = (
        unicodedata.normalize("NFKD", filename).encode(
            "ASCII", "ignore").decode()
    )

    # keep only whitelisted chars
    cleaned_filename = "".join(c for c in cleaned_filename if c in whitelist)
    if len(cleaned_filename) > _char_limit:
        print(f"Warning, filename truncated because it was over {_char_limit}."
              f" Filenames may no longer be unique")
    return cleaned_filename[:_char_limit]


"""
TAKEN FROM STOP:
Url: https://gist.github.com/wassname/1393c4a57cfcbf03641dbc31886123b8
"""


def get_gitignore(keywords) -> str:
    """Based on the keywords query gitignore.io api and generate .gitignore
    file."""
    user_agent = ("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7)"
                  " Gecko/2009021910 Firefox/3.0.7")
    headers = {"User-Agent": user_agent}
    url = GITIGNORE_URL
    url += ",".join(keywords)
    request = urllib.request.Request(url, None, headers)
    with urllib.request.urlopen(request) as response:
        text = response.read()
    return text.decode("utf-8")


def discover_supported_languages(templates_dir: Path):
    """ Checks the languages templates directory and returns the list of file
    names inside it."""
    p = templates_dir.glob("**/*")
    return [f.stem for f in p if f.is_file()]
