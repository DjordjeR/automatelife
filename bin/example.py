from automatelife import Config
from automatelife import discover_supported_languages

if __name__ == "__main__":
    config = Config()
    print(discover_supported_languages(config.languages_dir))
    conf = Config()
    print(conf.to_json())