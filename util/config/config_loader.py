import configparser, os
from util.error.MissingConfigurationError import MissingConfigurationError


def load_section_to_env(section_name):
    config = configparser.ConfigParser()
    print(os.getcwd())
    config.read('./config.ini')
    if not config.sections():
        raise MissingConfigurationError("No config.ini file found. Could not load configuration.")
    elif not section_name in config:
        raise MissingConfigurationError(
            "No EMAIL section found in configuration. Make sure username & app_key are set.")

    for item in config[section_name].items():
        os.environ[item[0]] = item[1]
