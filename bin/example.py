import json

from automatelife import Config, discover_supported_languages

if __name__ == "__main__":
    config = Config()
    print(discover_supported_languages(config.languages_dir))
    print(json.dumps(config))
