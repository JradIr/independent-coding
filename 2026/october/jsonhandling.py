import json
import logging

logging.basicConfig(level = logging.INFO, format='%(levelname)s, %(message)s')

data_save = [
    {"id": 1, "name": "raven"},
    {"id": 2, "name": "lianne"},
    {"id": 3, "name": "aaron"}
]
with open("users.json", "w") as file:
    json.dump(data_save, file, indent=4)

logging.info("the data use successfully changed in users.json")

try:
    with open("users.json", "r") as file:
        loaded_data = json.load(file)
    logging.info(f"The loaded data are {len(loaded_data)}")
except FileNotFoundError:
    logging.info("The file users.json is not found.")