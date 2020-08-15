import json
from dataclasses import asdict, dataclass, field, is_dataclass
from pathlib import Path
from typing import List

from .constants import (CONFIG_DIR, DEFAULT_GITIGNORE, DEFAULT_PROJECTS_DIR,
                        GITIGNORE_URL, LANGUAGES_DIR, TEMPLATES_DIR)


class _ConfigJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if is_dataclass(o):
            return asdict(o)
        if isinstance(o, Path):
            return str(o)
        return super().default(o)


@dataclass
class Config:
    """Contains configuration for the program. You can save and load this 
    configuration from the json file."""

    templates_dir: Path = TEMPLATES_DIR
    languages_dir: Path = LANGUAGES_DIR
    gitignore: List[str] = field(default_factory=lambda: DEFAULT_GITIGNORE)
    projects_dir: Path = DEFAULT_PROJECTS_DIR
    gitignore_url: Path = GITIGNORE_URL
    main_git_url: Path = "None"
    _save_file_path: Path = CONFIG_DIR / "automatelife"

    def save(self):
        """Save the configuration."""
        self._save_file_path.mkdir(exist_ok=True, parents=True)
        with open(self._save_file_path / ".config.json", mode="w") as f:
            json.dump(self, f, cls=_ConfigJSONEncoder)
