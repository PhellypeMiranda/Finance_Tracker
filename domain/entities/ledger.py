from domain.entities.transaction import Transaction

class Ledger:
    def __init__(self, transactions: list[Transaction]):
        self.transactions = transactions

    def __str__(self):
        return str(self.transactions)

    def __repr__(self):
        return str(self.transactions)

    def __iter__(self):
        return iter(self.transactions)

    def __getitem__(self, item):
        return self.transactions[item]

    def __setitem__(self, key, value):
        self.transactions[key] = value

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def remove_transaction(self, item):
        self.transactions.remove(item)