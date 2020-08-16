import json
from dataclasses import asdict, dataclass, field, is_dataclass
from pathlib import Path
from typing import List

from .constants import (CONFIG_DIR, CONFIG_FILE, DEFAULT_GITIGNORE,
                        DEFAULT_PROJECTS_DIR, DEFINITIONS_DIR, GITIGNORE_URL,
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
    definitions_dir: Path = DEFINITIONS_DIR
    gitignore: List[str] = field(default_factory=lambda: DEFAULT_GITIGNORE)
    projects_dir: Path = DEFAULT_PROJECTS_DIR
    gitignore_url: str = GITIGNORE_URL

    def save(self):
        """Save the configuration."""
        CONFIG_DIR.mkdir(exist_ok=True, parents=True)
        with open(CONFIG_FILE, mode="w") as f:
            json.dump(self, f, cls=_ConfigJSONEncoder)
        return self

    @classmethod
    def load_config(cls):

        if not CONFIG_FILE.exists():
            return cls().save()
        try:
            with open(CONFIG_FILE, mode="r") as f:
                config_dict = json.load(f)
            config_dict["templates_dir"] = Path(config_dict["templates_dir"])
            config_dict["definitions_dir"] = Path(
                config_dict["definitions_dir"])
            config_dict["projects_dir"] = Path(config_dict["projects_dir"])
            return cls(**config_dict)
        except KeyError:
            return cls().save()
