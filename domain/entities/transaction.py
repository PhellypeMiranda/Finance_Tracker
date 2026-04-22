from datetime import date
from decimal import Decimal

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