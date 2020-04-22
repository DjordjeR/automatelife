import json
import os

from .constants import TEMPLATES_DIR, LANGUAGES_DIR, DEFAULT_GITIGNORE, DEFAULT_PROJECTS_DIR, GITIGNORE_URL


class Config:
    """Contains configuration for the program. You can save and load this configuration from the json file."""

    def __init__(self):
        """Default configuration"""
        self.templates_dir = TEMPLATES_DIR
        self.languages_dir = LANGUAGES_DIR
        self.gitignore = DEFAULT_GITIGNORE
        self.projects_dir = DEFAULT_PROJECTS_DIR
        self.gitignore_url = GITIGNORE_URL

    @classmethod
    def from_json(cls, json_object):
        """Create configuration object from json format"""
        pass

    def to_json(self) -> str:
        """Convert to json format"""
        obj = {
            "templates_dir": os.fspath(self.templates_dir),
            "languages_dir": os.fspath(self.languages_dir),
            "gitignore": self.gitignore,
            "projects_dir": os.fspath(self.projects_dir),
            "gitignore_url": self.gitignore_url
        }
        return json.dumps(obj)

    def save(self):
        """Save the configuration in the given file. """
        file = "APPDATA"  # TODO: APPDATA on Windows and check for Linux
        with open(file, mode="w") as f:
            f.write(self.to_json())