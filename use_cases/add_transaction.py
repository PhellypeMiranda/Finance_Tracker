from domain.entities.transaction import Transaction

class AddTransactionUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, name, transaction_type, amount, category, transaction_date):
        new_transaction = Transaction(name, transaction_type, amount, category, transaction_date)
        ledger = self.repository.load_data()
        ledger.add_transaction(new_transaction)
        self.repository.save_data(ledger)