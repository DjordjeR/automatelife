from automatelife.core import Project
from automatelife.utils import discover_supported_languages
from automatelife.constants import LANGUAGES_DIR

if __name__ == "__main__":
    print(discover_supported_languages(LANGUAGES_DIR))
