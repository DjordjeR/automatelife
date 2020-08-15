import json
from dataclasses import asdict, dataclass, field, is_dataclass
from pathlib import Path
from typing import List

from .constants import (CONFIG_DIR, CONFIG_FILE, DEFAULT_GITIGNORE,
                        DEFAULT_PROJECTS_DIR, GITIGNORE_URL, LANGUAGES_DIR,
                        TEMPLATES_DIR)


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
    gitignore_url: str = GITIGNORE_URL

    def save(self):
        """Save the configuration."""
        CONFIG_DIR.mkdir(exist_ok=True, parents=True)
        with open(CONFIG_FILE, mode="w") as f:
            json.dump(self, f, cls=_ConfigJSONEncoder)

    @classmethod
    def load_config(cls):
        with open(CONFIG_FILE, mode="r") as f:
            config_dict = json.load(f)
        config_dict["templates_dir"] = Path(config_dict["templates_dir"])
        config_dict["languages_dir"] = Path(config_dict["languages_dir"])
        config_dict["projects_dir"] = Path(config_dict["projects_dir"])
        return cls(**config_dict)
