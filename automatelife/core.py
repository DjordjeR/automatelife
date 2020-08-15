import logging
import subprocess
from pathlib import Path

from .config import Config
from .exceptions import ProjectExistsException
from .language import LanguageDefinition
from .utils import clean_filename, get_gitignore

logger = logging.getLogger(__name__)


class Project:
    """ Takes in data about the project and creates the project with desired
    folder and file structure."""

    def __init__(
        self,
        name: str,
        description="TODO",
        language: str = "other",
        config: Config = None,
        **kwargs,
    ):
        self._name = name
        self._claned_name = clean_filename(name)
        self._language_definition = LanguageDefinition(language, config)
        self._description = description
        self._config = config if config else Config()
        if "project_path" in kwargs:
            self._project_path = kwargs["project_path"] / self._claned_name
        else:
            self._project_path = self._config.projects_dir / self._claned_name

        logger.debug(f"Project created: {self}")

    def _create_directory_structure(self):
        if self._project_path.exists():
            raise ProjectExistsException(self._claned_name)
        self._project_path.mkdir(parents=True)
        for dir_path in self._language_definition.dirs:
            current_full_dir = self._project_path / \
                Path(dir_path.replace("$projectName", self._claned_name))
            current_full_dir.mkdir(parents=True, exist_ok=True)

    def _create_files(self):
        for file_path in self._language_definition.files:
            current_full_path = self._project_path / \
                Path(file_path.replace("$projectName", self._claned_name))
            current_full_path.touch()

    def _fill_templates(self):
        raise NotImplementedError

    def _run_commands(self):
        for command in self._language_definition.commands:
            subprocess.run(command.split(" "), cwd=self._project_path)

    def _write_gitignore(self):
        gitignore_text = get_gitignore(self._language_definition.gitignore)
        gitignore_file = self._project_path / ".gitignore"
        gitignore_file.touch(exist_ok=True)
        with open(gitignore_file, mode="w") as file:
            file.write(gitignore_text)

    def run(self):
        """ Creates the project with the necessary structure. Fails if project
        exists.
        return created project path
        """
        self._create_directory_structure()
        self._create_files()
        self._run_commands()
        self._write_gitignore()
        # self._fill_templates()
        return self._project_path

    def __repr__(self):
        return {
            "name": self._name,
            "language": self._language_definition,
            "description": self._description,
            "config": self._config,
        }

    def __str__(self):
        return (f"Project(name={self._name}, "
                f"language={self._language_definition},"
                f"description={self._description}, config={self._config})")
