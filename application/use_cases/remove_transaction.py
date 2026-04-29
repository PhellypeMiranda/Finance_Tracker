class RemoveTransactionUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, index):
        ledger = self.repository.load_data()
        ledger.remove_transaction(index)
        self.repository.save_data(ledger)