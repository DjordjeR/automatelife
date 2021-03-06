import json
import logging
import subprocess
from pathlib import Path
from typing import List

from .config import Config
from .exceptions import ProjectExistsException
from .utils import clean_filename, get_gitignore

logger = logging.getLogger(__name__)


class ProjectDefinition:
    """
    Definition of the project structure.
    """

    def __init__(self, def_: str, config: Config):
        self._dirs = set()
        self._files = set()
        self._commands = set()
        self._gitignore = set()
        self._def = def_
        self._config = config
        self._project_def_file = self._config.definitions_dir / \
            (self._def + ".json")
        try:
            self._load_project_specifics(self._project_def_file)
        except RecursionError:
            print("Language definition has a cyclic dependencie.")
            exit(-1)

    def _load_project_specifics(self, file_path):
        with open(file_path) as f:
            loaded_data = json.loads(f.read())

        parent = loaded_data.get("inherit_from")
        if parent:
            self._load_project_specifics(self._config.definitions_dir / parent)

        self._dirs.update(loaded_data.get("dirs", []))
        self._files.update(loaded_data.get("files", []))
        self._commands.update(loaded_data.get("commands", []))
        self._gitignore.update(loaded_data.get(
            "gitignore", self._config.gitignore))

    # TODO: Complete __repr__ and __str__

    def __repr__(self):
        return {
            "name": self._def,
            "template_file": self._project_def_file,
        }

    def __str__(self):
        return (f"ProjectDefinition(name={self._def}, "
                f"template_file={self._project_def_file})")

    @property
    def name(self) -> str:
        """
        :returns the name
        """
        return self._def

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
        # TODO: This is very hacky ...
        return reversed(list(self._commands))


class Project:
    """ Takes in data about the project and creates the project with desired
    folder and file structure."""

    def __init__(
        self,
        name: str,
        description="TODO",
        project_str: str = "other",
        config: Config = None,
        **kwargs,
    ):
        self._name = name
        self._claned_name = clean_filename(name)
        self._config = config if config else Config()
        self._project_definition = ProjectDefinition(project_str, self._config)
        self._description = description
        if "project_path" in kwargs:
            self._project_path = kwargs["project_path"] / self._claned_name
        else:
            self._project_path = self._config.projects_dir / self._claned_name

        logger.debug(f"Project created: {self}")

    def _create_directory_structure(self):
        if self._project_path.exists():
            raise ProjectExistsException(self._claned_name)
        self._project_path.mkdir(parents=True)
        for dir_path in self._project_definition.dirs:
            current_full_dir = self._project_path / \
                Path(dir_path.replace("$projectName", self._claned_name))
            current_full_dir.mkdir(parents=True, exist_ok=True)

    def _create_files(self):
        for file_path in self._project_definition.files:
            current_full_path = self._project_path / \
                Path(file_path.replace("$projectName", self._claned_name))
            current_full_path.touch()

    def _fill_templates(self):
        raise NotImplementedError

    def _run_commands(self):
        for command in self._project_definition.commands:
            subprocess.run(command.split(" "), cwd=self._project_path)

    def _write_gitignore(self):
        gitignore_text = get_gitignore(self._project_definition.gitignore)
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
            "project_definition": self._project_definition,
            "description": self._description,
            "config": self._config,
        }

    def __str__(self):
        return (f"Project(name={self._name}, "
                f"project_definition={self._project_definition},"
                f"description={self._description}, config={self._config})")
