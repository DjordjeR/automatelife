import json
from typing import List

from .config import Config


class LanguageDefinition:
    """
    Definition of the programming language structure.
    """

    def __init__(self, lang: str, config: Config):
        self._dirs = None
        self._files = None
        self._commands = None
        self._gitignore = None
        self._lang = lang
        self._config = config
        self._language_def_file = self._config.languages_dir / \
            (self._lang + ".json")
        self._load_language_specifics()

    def _load_language_specifics(self):
        with open(self._language_def_file) as f:
            loaded_data = json.loads(f.read())
        self._dirs = loaded_data.get("dirs", [])
        self._files = loaded_data.get("files", [])
        self._commands = loaded_data.get("commands", [])
        self._gitignore = loaded_data.get("gitignore", self._config.gitignore)

    # TODO: Complete __repr__ and __str__
    def __repr__(self):
        return {
            "name": self._lang,
            "template_file": self._language_def_file,
        }

    def __str__(self):
        return (f"LanguageDefinition(name={self._lang}, "
                f"template_file={self._language_def_file})")

    @property
    def lang(self) -> str:
        """
        :returns the name of the language
        """
        return self._lang

    @property
    def dirs(self) -> List[str]:
        """
        :returns: List of directories that need to be created in projectDir
        """
        return self._dirs

    @ property
    def files(self) -> List[str]:
        """
        :returns List of files that need to be created in projectDir
        """
        return self._files

    @ property
    def gitignore(self) -> List[str]:
        """
        :returns List of gitignore keywords.
        """
        return self._gitignore

    @property
    def commands(self) -> List[str]:
        """
        :returns List of commands to be run after project creation
        """
        return self._commands
