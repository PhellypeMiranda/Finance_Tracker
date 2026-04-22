import sys
from utils import user_input, validation as validation
from interface.cli import interface
from domain.entities.ledger import Ledger


class Service:
    def __init__(self, repository):
        self.repository = repository
        self.ledger = Ledger(self.repository.load_data())

    @staticmethod
    def exit():
        confirmation = user_input.confirmation("Are you sure you want to exit?")
        if confirmation:
            sys.exit(0)
