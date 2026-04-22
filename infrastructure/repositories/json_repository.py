import json
from infrastructure.config.config import DATA_DIR
from infrastructure.mappers import mappers
from domain.entities.ledger import Ledger
from domain.repositories.transaction_repositories import TransactionRepository

class JsonRepository(TransactionRepository):
    def __init__(self, json_file="data.json"):
        self.file = DATA_DIR / json_file
        self.file.parent.mkdir(parents=True, exist_ok=True)

    def save_data(self, ledger: Ledger) ->None:
        converted_data = mappers.convert_to_dict(ledger)
        with open(self.file, "w") as f:
            json.dump(converted_data, f, indent=4)

    def load_data(self) -> Ledger:
        try:
            with open(self.file, "r") as f:
                data = json.load(f)
                converted_data = mappers.convert_to_obt(data)
            return converted_data
        except FileNotFoundError:
            return Ledger([])