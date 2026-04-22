from domain.entities.transaction import Transaction
from domain.services.service import Service


class RemoveTransaction:
    def __init__(self, service, repository):
        self.repository = repository
        self.service = service

    def execute(self, index):
        self.service.remove_transaction(self.service.ledger[index])
        self.repository.save_data(self.service.ledger)