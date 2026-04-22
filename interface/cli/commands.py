from domain.services import service
from interface.cli import interface
from domain.entities.transaction_type import TransactionType
from domain.entities.category import Category
from utils import user_input, format
from decimal import Decimal
from datetime import date

def main_commands(option, add_transaction, remove_transaction, get_transactions):
    match option:
        case 1:
            transaction_type = interface.transaction_type_menu("add")
            name = user_input.type_name(f"\nType the name of the {transaction_type.value}: ")
            amount = user_input.type_amount(f"Type the value of the {transaction_type.value}: ")
            category = interface.category_menu(transaction_type)
            current_date = user_input.confirmation(f"Add today's date: {format.today_date()}?")
            if current_date:
                transaction_date = date.today()
            else:
                transaction_date = user_input.type_date(f"Enter other date (YYYY-MM-DD):")
            add_transaction.execute(name, transaction_type, amount, category, transaction_date)
        case 2:
            transaction_list = get_transactions.execute()
            lenght - len(transaction_list)
            index = user_input.type_index("Which transaction do you want to remove?", 2)
            remove_transaction.execute(index - 1)
        case 3:
            service.modify_transaction(service)
        case 4:
            interface.search_menu(service)
        case 5:
            interface.date_menu(service)
        case 0:
            service.exit()
        case _:
            input("Invalid input! try again...")

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
                transaction.amount = Decimal(new_amount)
                input("Value changed, press any key to continue...")
            else:
                input("Value not changed, press any key to continue...")
        case 3:
            new_type = None
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
                input("Category changed, press any key to continue...")
            else:
                input("Category not changed, press any key to continue...")
        case 5:
            new_date = user_input.type_date("Type the new date (YYYY-MM-DD): ")
            confirmation = user_input.confirmation(f"Change the date to {new_date}?")
            if confirmation:
                transaction.transaction_date = new_date
                input("Date changed, press any key to continue...")
            else:
                input("Date not changed, press any key to continue...")
        case _:
            print("Invalid input! try again...")

def transaction_type_commands(option):
    match option:
        case 1:
            return TransactionType.INCOME
        case 2:
            return TransactionType.EXPENSE
        case _:
            print("Invalid input! try again...")
            return None

def category_type_commands(option, transaction_type):
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
            case _:
                input("Invalid input! try again...")

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
            case _:
                input("Invalid input! try again...")
    else:
        print("ERROR! try again...")
        return None

def search_commands(option, service):
    match option:
        case 1:
            service.balance = False
            service.income = True
            service.expense = True
            service.category = None
        case 2:
            service.balance = False
            service.income = True
            service.expense = False
        case 3:
            service.income = False
            service.expense = True
        case 4:
            transaction_type = interface.transaction_type_menu(service, "show")
            if transaction_type == TransactionType.INCOME:
                service.income = True
                service.expense = False
            elif transaction_type == TransactionType.EXPENSE:
                service.expense = True
                service.income = False
            category = interface.category_menu(service, transaction_type)
            service.category = category
        case 5:
            interface.main_menu(service)
        case _:
            input("Invalid input! try again...")
    return None

def sort_commands(option, service):
    match option:
        case 1:
            service.sort = "name"
        case 2:
            service.sort = "value"
        case 3:
            service.sort = "date"
        case 4:
            service.toggle_increasing()
        case _:
            print("Invalid input! try again...")
    return None

def date_commands(option, service):
    match option:
        case 1:
            service.by_month = True
            service.date_setter(service)
        case 2:
            service.by_month = False
            service.date_setter(service)
        case 3:
            service.by_month = True
            input("Showing transactions by month...")
        case 4:
            service.by_month = False
            input("Showing transactions by year...")
        case 5:
            service.by_month = True
            service.month = date.today().month
            service.year = date.today().year
            input(f"Date set to {format.month_year(date.today())}")
        case _:
            print("Invalid input! try again...")
    return None