from pathlib import Path

from git import Repo

from .constants import DEFAULT_PROJECTS_DIR
from .exceptions import ProjectExistsException
from .language import SupportedLanguages, LanguageDefinition
from .utils import clean_filename, get_gitignore


class Project:
    def __init__(self, name: str, description="TODO", language: SupportedLanguages = SupportedLanguages.OTHER,
                 **kwargs):
        self._name = name
        self._language_definition = LanguageDefinition(language)
        self._description = description
        
        if "projects_root" in kwargs:
            self._projects_root = Path(kwargs["projects_root"])
        else:
            self._projects_root = DEFAULT_PROJECTS_DIR

        self._project_path = self._projects_root / clean_filename(self._name)

    def _create_directory_structure(self):
        if self._project_path.exists():
            raise ProjectExistsException(clean_filename(self._name))
        self._project_path.mkdir(parents=True)

        for dir_path in self._language_definition.dirs:
            current_full_dir = self._project_path
            for dir_name in dir_path:
                if dir_name == "$projectName":
                    current_full_dir = current_full_dir / clean_filename(self._name)
                else:
                    current_full_dir = current_full_dir / dir_name
            current_full_dir.mkdir(parents=True, exist_ok=True)

    def _create_files(self):
        for file_path in self._language_definition.files:
            current_full_dir = self._project_path
            for file_name in file_path:
                print(current_full_dir)
                if file_name == "$projectName":
                    current_full_dir = current_full_dir / clean_filename(self._name)
                else:
                    current_full_dir = current_full_dir / file_name
            current_full_dir.touch()

    def _fill_templates(self):
        raise NotImplementedError

    def _setup_venv(self):
        raise NotImplementedError

    def _write_gitignore(self):
        gitignore_text = get_gitignore(self._language_definition.gitignore)
        gitignore_file = (self._project_path / ".gitignore")
        gitignore_file.touch(exist_ok=True)
        with open(gitignore_file, mode="w") as file:
            file.write(gitignore_text)

    def _init_repo(self):
        full_project = self._projects_root / clean_filename(self._name)
        git_repo = Repo.init(full_project)
        # TODO: Get user name and email

    def run(self):
        self._create_directory_structure()
        self._create_files()
        self._init_repo()
        self._write_gitignore()
        # self._fill_templates()

    def __repr__(self):
        return {
            "name": self._name,
            "language": self._language_definition,
            "description": self._description,
            "projects_root": self._projects_root
        }

    def __str__(self):
        return f"AutomateLife(name={self._name}, language={self._language_definition}, description={self._description}, project_root={self._projects_root})"
