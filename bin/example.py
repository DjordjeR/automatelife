import json

from automatelife import Config, discover_default_definitions

if __name__ == "__main__":
    config = Config()
    print(discover_default_definitions(config.definitions_dir))
    print(json.dumps(config))
