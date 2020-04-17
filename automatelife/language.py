import json
from typing import List

from .constants import LANGUAGES_DIR, DEFAULT_GITIGNORE


class LanguageDefinition:
    """
    Definition of language structure.
    """

    def __init__(self, lang: str, **kwargs):
        if "templates_dir" in kwargs:
            self._templates_dir = kwargs["templates_dir"]
        else:
            self._templates_dir = LANGUAGES_DIR

        self._lang = lang
        self._template_file = self._templates_dir / (self._lang + ".json")
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

    # TODO: Complete __repr__ and __str__
    def __repr__(self):
        return {
            "name": self._lang,
            "template_file": self._template_file,
        }

    def __str__(self):
        return f"LanguageDefinition(name={self._lang}, template_file={self._template_file})"

    @property
    def lang(self) -> str:
        """
        :returns the name of the language
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
