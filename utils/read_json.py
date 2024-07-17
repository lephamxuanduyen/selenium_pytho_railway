import json

def readJson(jsonFilePath):
    with open(jsonFilePath, 'r', encoding='utf-8') as f:
        jsonFile = json.load(f)

    return jsonFile