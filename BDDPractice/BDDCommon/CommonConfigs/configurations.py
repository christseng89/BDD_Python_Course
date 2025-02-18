import configparser

def get_config():
    config = configparser.ConfigParser()
    config.read('properties.ini')
    return config
