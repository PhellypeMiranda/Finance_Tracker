from models.transaction import Transaction

class Ledger:
    def __init__(self):
        self.ledger = []

    def __str__(self):
        return str(self.ledger)

    def __repr__(self):
        return str(self.ledger)

    def __iter__(self):
        return iter(self.ledger)

    def __getitem__(self, item):
        return self.ledger[item]

    def __setitem__(self, key, value):
        self.ledger[key] = value

    def add_item(self, transaction):
        self.ledger.append(transaction)

    def remove_item(self, item):
        self.ledger.remove(item)

    def convert_ledger_to_dict(self):
        return [i.convert_to_dict() for i in self.ledger]

    def convert_ledger_to_obj(self, dict_transactions):
        self.ledger = [Transaction.convert_to_obt(i) for i in dict_transactions]