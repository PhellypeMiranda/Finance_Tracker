from enum import Enum
from domain.value_objetcs.transaction_type import TransactionType

class Category(Enum):
    # Expenses
    FOOD = ("food", TransactionType.EXPENSE)
    TRANSPORT = ("transport", TransactionType.EXPENSE)
    HOUSING = ("housing", TransactionType.EXPENSE)
    UTILITIES = ("utilities", TransactionType.EXPENSE)
    HEALTH = ("health", TransactionType.EXPENSE)
    ENTERTAINMENT = ("entertainment", TransactionType.EXPENSE)
    EDUCATION = ("education", TransactionType.EXPENSE)
    SHOPPING = ("shopping", TransactionType.EXPENSE)
    SUBSCRIPTIONS = ("subscriptions", TransactionType.EXPENSE)
    OTHER_EXPENSE = ("other_expense", TransactionType.EXPENSE)

    # Income
    SALARY = ("salary", TransactionType.INCOME)
    FREELANCE = ("freelance", TransactionType.INCOME)
    INVESTMENTS = ("investments", TransactionType.INCOME)
    BONUS = ("bonus", TransactionType.INCOME)
    OTHER_INCOME = ("other_income", TransactionType.INCOME)