import configparser
import os

PATH = os.path.expanduser("~/.standingTimer")
FILE_NAME = "config.ini"
FILE_PATH = PATH + "/" + FILE_NAME

DEFAULT_AUTH_VALUES = {"server_url": "standing-timer.poleselli.com"}

config = configparser.ConfigParser()
config.read(FILE_PATH)


def has_auth_token():
    return "AUTH" in config and config["AUTH"]["token"] is not None


def reduce_auth_value(value, key):
    stripped_value = value.strip() if value is not None else ""

    if len(stripped_value) > 0:
        return stripped_value
    elif "AUTH" in config and config["AUTH"][key] is not None:
        return config["AUTH"][key]

    return DEFAULT_AUTH_VALUES[key]


def write_auth_config(token, server_url):
    reduced_token = reduce_auth_value(token, "token")
    reduced_url = reduce_auth_value(server_url, "server_url")

    if (
        not "AUTH" in config
        or config["AUTH"]["token"] != reduced_token
        or config["AUTH"]["server_url"] != reduced_url
    ):
        config["AUTH"] = {"token": reduced_token, "server_url": reduced_url}

        if not os.path.exists(PATH):
            os.makedirs(PATH)

        with open(FILE_PATH, "w+") as configfile:
            config.write(configfile)
