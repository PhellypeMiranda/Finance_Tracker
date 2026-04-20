from datetime import date, datetime
from decimal import Decimal
from domain.entities.category import Category
from domain.entities.transaction_type import TransactionType

class Transaction:
    def __init__(self, name, transaction_type, amount, category, transaction_date=date.today()):
        self.name = name
        self.transaction_type = transaction_type
        self.amount = Decimal(amount)
        self.category = category
        self.transaction_date = transaction_date

    def __str__(self):
        return (f'{self.name:<20}$:{+self.amount:<13.2f}'
                f'{self.category.value[0]:<15}{self.transaction_date.strftime("%d-%m-%Y")}')

    def __repr__(self):
        return f'{self.name} | {self.transaction_type} | {self.amount} | {self.category} | {self.transaction_date}'

    def convert_to_dict(self):
        dict_transaction = {
            "name": self.name,
            "transaction_type": self.transaction_type.value,
            "amount": str(self.amount),
            "transaction_date": self.transaction_date.strftime("%Y-%m-%d"),
            "category": self.category.value[0]
        }
        return dict_transaction

    @staticmethod
    def convert_to_obt(dict_transaction):
        return Transaction(
        name = dict_transaction["name"],
        transaction_type = TransactionType(dict_transaction["transaction_type"]),
        amount = Decimal(dict_transaction["amount"]),
        transaction_date = datetime.strptime(dict_transaction["transaction_date"], "%Y-%m-%d").date(),
        category=Category(dict_transaction["category"], TransactionType(dict_transaction["transaction_type"])),
        )