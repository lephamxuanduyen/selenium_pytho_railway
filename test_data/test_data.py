import os
from utils.read_json import readJson

def get_message(page, key):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_name = 'message.json'
    file_path = os.path.join(current_dir, file_name)
    datas = readJson(file_path)
    return datas.get(page).get(key)

def get_info_user(key):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_name = 'user.json'
    file_path = os.path.join(current_dir, file_name)
    return readJson(file_path)[key]