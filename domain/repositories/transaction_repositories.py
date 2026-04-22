from abc import ABC, abstractmethod
from domain.entities.ledger import Ledger

class TransactionRepository(ABC):

    @abstractmethod
    def load_data(self) -> Ledger:
        pass

    @abstractmethod
    def save_data(self, ledger: Ledger) -> None:
        pass