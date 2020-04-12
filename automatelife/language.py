import json
from enum import Enum
from typing import List
from pathlib import Path

from .constants import LANGUAGES_DIR, DEFAULT_GITIGNORE


class SupportedLanguages(Enum):
    OTHER = 0
    PYTHON = 1


class LanguageDefinition:
    """
    Definition of language structure.
    """

    def __init__(self, lang: SupportedLanguages, **kwargs):
        if "templates_dir" in kwargs:
            self._templates_dir = kwargs["templates_dir"]
        else:
            self._templates_dir = Path(__file__).parent.absolute() / LANGUAGES_DIR

        self._lang = lang
        self._template_file = self._templates_dir / str(self._lang.name.lower() + ".json")
        with open(self._template_file) as f:
            loaded_data = json.loads(f.read())

        self._dirs = loaded_data["dirs"]
        self._files = loaded_data["files"]

        if "readme_template" in loaded_data:
            self._readme_template = loaded_data["readme_template"]
        else:
            self._readme_template = "README.md"

        if "gitignore" in loaded_data:
            self._gitignore = loaded_data["gitignore"]
        else:
            self._gitignore = DEFAULT_GITIGNORE

    @property
    def lang(self) -> SupportedLanguages:
        """
        :returns SupportedLanguages the type of language chosen
        """
        return self._lang

    @property
    def dirs(self) -> List[List[str]]:
        """
        :returns: List of directories that need to be created in projectDir
        """
        return self._dirs

    @property
    def files(self) -> List[List[str]]:
        """
        :returns List of files that need to be created in projectDir
        """
        return self._files

    @property
    def gitignore(self) -> List[str]:
        """
        :returns List of gitignore keywords.
        """
        return self._gitignore

    @property
    def readme_template(self) -> str:
        return self._readme_template
