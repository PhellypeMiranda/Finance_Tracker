from cli import interface
from models.transaction_type import TransactionType
from models.category import Category
from utils import user_input


def main_commands(option, service):
    match option:
        case 1:
            service.add_transaction(service)
        case 2:
            service.remove_transaction(service)
        case 3:
            service.modify_transaction((service))
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

def modify_commands(option, service, transaction):
    match option:
        case 1:
            new_name = user_input.type_name("Type the new name: ")
            confirmation = user_input.confirmation(f"\nChange the name to {new_name}?")
            if confirmation:
                transaction.name = new_name
                input("Name changed, press any key to continue...")
            else:
                input("Name not changed, press any key to continue...")
        case 2:
            new_amount = user_input.type_amount("Type the new value: ")
            confirmation = user_input.confirmation(f"\nChange the value to {new_amount}?")
            if confirmation:
                transaction.amount = new_amount
                input("Value changed, press any key to continue...")
            else:
                input("Value not changed, press any key to continue...")
        case 3:
            if transaction.transaction_type == TransactionType.INCOME:
                new_type = TransactionType.EXPENSE
            elif transaction.transaction_type == TransactionType.EXPENSE:
                new_type = TransactionType.INCOME
            confirmation = user_input.confirmation(f"\nChange the type to {new_type.value}?")
            if confirmation:
                transaction.transaction_type = new_type
                input("Type changed, press any key to continue...")
            else:
                input("Type not changed, press any key to continue...")
            modify_commands(4, service, transaction)
        case 4:
            new_category = interface.category_menu(service, transaction.transaction_type)
            confirmation = user_input.confirmation(f"\nChange the category to {new_category.value[0]}?")
            if confirmation:
                transaction.category = new_category
                input("Type changed, press any key to continue...")
            else:
                input("Type not changed, press any key to continue...")
        case 5:
            new_date = user_input.type_date("Type the new date (YYYY-MM-DD): ")
            confirmation = user_input.confirmation(f"Change the date to {new_date}?")
            if confirmation:
                transaction.transaction_date = new_date
                input("Date changed, press any key to continue...")
            else:
                input("Date not changed, press any key to continue...")
        case 0:
            interface.main_menu(service)
        case _:
            print("Invalid input! try again...")

def transactions_commands(option, service):
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

def transaction_type_commands(option, service):
    match option:
        case 1:
            service.income = True
            service.expense = False
            service.balance = False
            service.clear_screen()
            interface.show_transactions(service)
            return TransactionType.INCOME
        case 2:
            service.income = False
            service.expense = True
            service.balance = False
            service.clear_screen()
            interface.show_transactions(service)
            return TransactionType.EXPENSE
        case 0:
            interface.main_menu(service)
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