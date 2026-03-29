import json
from config import DATA_DIR

class FileHandler:
    def __init__(self, json_file="data.json"):
        self.file = DATA_DIR / json_file
        self.file.parent.mkdir(parents=True, exist_ok=True)

    def save_data(self, data):
        with open(self.file, "w") as f:
            json.dump(data, f, indent=4)
        return 0

    def load_data(self):
        try:
            with open(self.file, "r") as f:
                data = json.load(f)
            return data
        except (FileNotFoundError, json.JSONDecodeError):
            return []