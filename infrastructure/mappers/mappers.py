from domain.entities.transaction import Transaction
from domain.entities.category import Category
from domain.entities.transaction_type import TransactionType
from decimal import Decimal
from datetime import datetime

def convert_to_dict(data):
    converted_data = []
    for i in data:
        dict_transaction = {
            "name": i.name,
            "transaction_type": i.transaction_type.value,
            "amount": str(i.amount),
            "transaction_date": i.transaction_date.strftime("%Y-%m-%d"),
            "category": i.category.value[0]}
        converted_data.append(dict_transaction)
    return converted_data

def convert_to_obt(data):
    converted_data = []
    for i in data:
        new_transaction = Transaction(
        name=i["name"],
        transaction_type=TransactionType(i["transaction_type"]),
        amount=Decimal(i["amount"]),
        transaction_date=datetime.strptime(i["transaction_date"], "%Y-%m-%d").date(),
        category=Category(i["category"], TransactionType(i["transaction_type"]))
        )
        converted_data.append(new_transaction)
    return converted_data