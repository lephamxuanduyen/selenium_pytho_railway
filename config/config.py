import os
import configparser

def read_config(key):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_name = 'config.ini'
    ini_file_path = os.path.join(current_dir, file_name)
    config = configparser.ConfigParser()
    config.read(ini_file_path)
    return config.get('pytest', key)
