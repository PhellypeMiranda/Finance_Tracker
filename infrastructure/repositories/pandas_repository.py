import pandas as pd
from infrastructure.config.config import DATA_DIR
from domain.entities.ledger import Ledger
from domain.repositories.transaction_repositories import TransactionRepository

class PandasRepository(TransactionRepository):
    def __init__(self, json_file="data.csv"):
        self.file = DATA_DIR / json_file
        self.file.parent.mkdir(parents=True, exist_ok=True)

    def save_data(self, ledger: Ledger) -> None:
        pd.

    def load_data(self, ledger: Ledger) -> pd.DataFrame: