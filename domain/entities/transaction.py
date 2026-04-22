from datetime import date
from decimal import Decimal
from dataclasses import dataclass, field
from domain.value_objetcs.transaction_type import TransactionType
from domain.value_objetcs.category import Category

@dataclass
class Transaction:
    name: str
    transaction_type: TransactionType
    amount: Decimal
    category: Category
    transaction_date: date = field(default_factory=date.today)

    def __post_init__(self):
        self.amount = Decimal(self.amount)

        if isinstance(self.transaction_type, str):
            self.transaction_type = TransactionType(self.transaction_type)

        if isinstance(self.category, str):
            self.category = Category(self.category)