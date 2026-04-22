from domain.entities.transaction import Transaction

class AddTransaction:
    def __init__(self, service, repository):
        self.repository = repository
        self.service = service

    def execute(self, name, transaction_type, amount, category, transaction_date):
        new_transaction = Transaction(name, transaction_type, amount, category, transaction_date)
        self.service.add_transaction(new_transaction)
        self.repository.save_data(self.service.ledger)