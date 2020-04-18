# What can we config?


# Default projects dir, where the projects will be saved
# Additional Templates directory

from .constants import *


class Config:
    def __init__(self):
        self.templates_dir = TEMPLATES_DIR
        self.languages_dir = LANGUAGES_DIR
        self.gitignore = DEFAULT_GITIGNORE
        self.projects_dir = DEFAULT_PROJECTS_DIR
        self.gitignore_url = GITIGNORE_URL

    @classmethod
    def from_json(cls, json: str):
        pass

    def to_json(self) -> str:
        """Convert to json file"""
        pass
