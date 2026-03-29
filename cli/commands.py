from cli import interface
from models.transaction_type import TransactionType
from models.category import Category


def main_menu_commands(option, service):
    match option:
        case 1:
            service.add_transaction(service)
        case 2:
            print("aqui vou remover items")
        case 3:
            print("aqui vou modificar items")
        case 4:
            service.income = True
            service.expense = True
            service.balance = False
            interface.transactions_menu(service)
        case 5:
            print("aqui vou ver as estatistica items")
        case 0:
            service.exit()
        case _:
            print("Invalid input! try again...")

def transactions_menu_commands(option, service):
    match option:
        case 1:
            service.income = False
            service.expense = False
        case 2:
            service.income = True
            service.expense = False
        case 3:
            service.income = False
            service.expense = True
        case 4:
            print("aqui vou ver todos os items")
        case 5:
            print("aqui vou ver as estatistica items")
        case 6:
            print("aqui vou ver as estatistica items")
        case 0:
            interface.main_menu(service)
        case _:
            print("Invalid input! try again...")
    interface.transactions_menu(service)

def transaction_type_commands(option, services):
    match option:
        case 1:
            return TransactionType.INCOME
        case 2:
            return TransactionType.EXPENSE
        case 0:
            interface.main_menu(services)
            return None
        case _:
            print("Invalid input! try again...")
            return None

def category_type_commands(option, services, transaction_type):
    if transaction_type == TransactionType.INCOME:
        match option:
            case 1:
                return Category.SALARY
            case 2:
                return Category.FREELANCE
            case 3:
                return Category.INVESTMENTS
            case 4:
                return Category.BONUS
            case 5:
                return Category.OTHER_INCOME
            case 0:
                interface.main_menu(services)
                return None
            case _:
                print("Invalid input! try again...")
                return None

    elif transaction_type == TransactionType.EXPENSE:
        match option:
            case 1:
                return Category.FOOD
            case 2:
                return Category.TRANSPORT
            case 3:
                return Category.HOUSING
            case 4:
                return Category.UTILITIES
            case 5:
                return Category.HEALTH
            case 6:
                return Category.ENTERTAINMENT
            case 7:
                return Category.EDUCATION
            case 8:
                return Category.SHOPPING
            case 9:
                return Category.SUBSCRIPTIONS
            case 10:
                return Category.OTHER_EXPENSE
            case 0:
                interface.main_menu(services)
                return None
            case _:
                print("Invalid input! try again...")
                return None
    else:
        print("ERROR! try again...")
        interface.main_menu(services)
        return None