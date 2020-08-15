import json
from typing import List

from .config import Config


# TODO: LanguageDefinition might not be the best name, maybe named project structure or something like that.
# In general this needs to be reformatted to better represent project structure.
class LanguageDefinition:
    """
    Definition of the programming language structure.
    """

    def __init__(self, lang: str, config: Config):
        self._lang = lang
        self._config = config
        self._template_file = self._config.templates_dir / \
            (self._lang + ".json")
        self.__load_language_specifics()

    def __load_language_specifics(self):
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
            self._gitignore = self._config.gitignore

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
        """
        :returns Readme template name
        """
        return self._readme_template
