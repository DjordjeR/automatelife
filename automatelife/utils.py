import urllib.request
from pathlib import Path
from .constants import GITIGNORE_URL

"""
START:
Url: https://gist.github.com/wassname/1393c4a57cfcbf03641dbc31886123b8
"""
import unicodedata
import string

valid_filename_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
char_limit = 255


def clean_filename(filename, whitelist=valid_filename_chars, replace=' '):
    # replace spaces
    for r in replace:
        filename = filename.replace(r, '_')

    # keep only valid ascii chars
    cleaned_filename = unicodedata.normalize('NFKD', filename).encode('ASCII', 'ignore').decode()

    # keep only whitelisted chars
    cleaned_filename = ''.join(c for c in cleaned_filename if c in whitelist)
    if len(cleaned_filename) > char_limit:
        print(
            "Warning, filename truncated because it was over {}. Filenames may no longer be unique".format(char_limit))
    return cleaned_filename[:char_limit]


"""
STOP:
Url: https://gist.github.com/wassname/1393c4a57cfcbf03641dbc31886123b8
"""


def get_gitignore(keywords=None) -> str:
    if keywords is None:
        raise TypeError
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers = {'User-Agent': user_agent}
    url = GITIGNORE_URL
    for keyword in keywords:
        url += keyword + ","
    url = url.rstrip(",")
    request = urllib.request.Request(url, None, headers)  # The assembled request
    with urllib.request.urlopen(request) as response:
        text = response.read()
    return text.decode("utf-8")


def discover_supported_languages(templates_dir: Path):
    p = templates_dir.glob("**/*")
    files = [f.stem for f in p if f.is_file()]
    return files
