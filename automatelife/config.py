import json
from dataclasses import dataclass

from .constants import (CONFIG_DIR, DEFAULT_GITIGNORE, DEFAULT_PROJECTS_DIR,
                        GITIGNORE_URL, LANGUAGES_DIR, TEMPLATES_DIR)


@dataclass
class Config:
    """Contains configuration for the program. You can save and load this 
    configuration from the json file."""

    def __init__(self):
        """Default configuration"""
        self.templates_dir = TEMPLATES_DIR
        self.languages_dir = LANGUAGES_DIR
        self.gitignore = DEFAULT_GITIGNORE
        self.projects_dir = DEFAULT_PROJECTS_DIR
        self.gitignore_url = GITIGNORE_URL
        self.main_git_url = None
        self._save_file_path = CONFIG_DIR / "automatelife"
        self._save_file_path = self._save_file_path / ".config.json"

    def save(self):
        """Save the configuration."""
        with open(self._save_file_path, mode="w") as f:
            json.dump(self, f)

    # TODO: __repr__
    # TODO: __str__
