from cli import commands
from models.category import Category
from models.transaction_type import TransactionType


def main_menu(service):
    while True:
        try:
            service.clear_screen()
            service.balance = True
            service.balance = True
            service.income = True
            show_transactions(service)
            option = int(input("\n===========MENU===========\n"
                               "1 - Add new transaction\n"
                               "2 - Remove a transaction\n"
                               "3 - Modify a transaction\n"
                               "4 - Organize transactions\n"
                               "5 - Change date\n"
                               "6 - Show statistics\n"
                               "0 - Exit\n"
                               "Select an option: "))

            commands.main_commands(option, service)

        except ValueError:
            input("Invalid input, type a number!")

def transactions_menu(service):
    while True:
        try:
            service.clear_screen()
            show_transactions(service)
            option = int(input("\n===========MENU===========\n"
                               "1 - See all transactions\n"
                               "2 - See only income\n"
                               "3 - See only expenses\n"
                               "4 - Change the month\n"
                               "5 - See by year\n"
                               "6 - See statistics\n"
                               "0 - Return\n"
                               "Select an option: "))

            commands.transactions_commands(option, service)
        except ValueError:
            input("Invalid input, Try again...")


def modify_menu(service, transaction):
    while True:
        try:
            service.clear_screen()
            show_transactions(service)
            option = int(input("\n===========MENU===========\n"
                               "Which would you like to modify?\n"
                               "1 - Name\n"
                               "2 - Value\n"
                               "3 - Type and category\n"
                               "4 - Category\n"
                               "5 - Date\n"
                               "0 - Return\n"
                               "Select an option: "))

            commands.modify_commands(option, service, transaction)
            break

        except ValueError:
            input("Invalid input, Try again...")


def transaction_type_menu(service, operation_type):
    while True:
        try:
            service.clear_screen()
            show_transactions(service)
            option = int(input("\n===========MENU===========\n"
                               f"Which kind of transaction do you want to {operation_type}?\n"
                               f"1 - {operation_type} income\n"
                               f"2 - {operation_type} expense\n"
                               f"0 - Return\n"
                               "Select an option: "))

            if 0 <= option <= 2:
                return commands.transaction_type_commands(option, service)
            else:
                input("Invalid input, Try again...")

        except ValueError:
            input("Invalid input, Try again...")


def category_menu(service, transaction_type):
    while True:
        try:
            service.clear_screen()
            show_transactions(service)
            print("\n===========MENU===========\n"
                  "Select a category for your transaction:")
            count = 1
            for i in Category:
                if i.value[1] == transaction_type:
                    print(f"{count} - {i.value[0].capitalize()}")
                    count += 1
            option = int(input("Select an option: "))
            category = (commands.category_type_commands(option, service, transaction_type))
            return category

        except ValueError:
            input("Invalid input, Try again...")


def show_transactions(service):
    if service.balance:
        total_income = 0
        for i in service.list:
            if i.transaction_type.value == "income":
                total_income += i.amount

        total_expense = 0
        for i in service.list:
            if i.transaction_type.value == "expense":
                total_expense += i.amount

        print("\n==============================BALANCE============================="
              f"\n{'Total income: $:':>37}{total_income:.2f}\n"
              f"{'Total expense: $':>37}{total_expense:.2f}\n"
              f"{'Total Balance: $:':>38}{total_income - total_expense:.2f}")

    if service.income:
        print("\n==============================INCOME==============================\n"
              f"{"Id":<5}{"Name":<20}{"Value":<15}{"Category":<15}{"Date":<10}")
        income_list = service.create_list(TransactionType.INCOME)
        if income_list:
            income_list = service.create_list(TransactionType.INCOME)
            for c, i in enumerate(income_list, start=1):
                print(f"{c}    {i}")
        else:
            print(f"{'\nLIST EMPTY! try adding new transactions...':^70}")

    if service.expense:
        print("\n=============================EXPENSES=============================\n"
              f"{"Id":<5}{"Name":<20}{"Value":<15}{"Category":<15}{"Date":<10}")
        expense_list = service.create_list(TransactionType.EXPENSE)
        if expense_list:
            expense_list = service.create_list(TransactionType.EXPENSE)
            for c, i in enumerate(expense_list, start=1):
                print(f"{c}    {i}")
        else:
            print(f"{'\nLIST EMPTY! try adding new transactions...':^70}")


def search_menu(service):
    while True:
        try:
            service.clear_screen()
            show_transactions(service)
            option = int(input("\n===========MENU===========\n"
                               "1 - Show all transactions\n"
                               "2 - Show income\n"
                               "3 - Show expenses\n"
                               "4 - Show by category\n"
                               "5 - Sort by...\n"
                               "0 - Return\n"
                               "Select an option: "))

            commands.search_commands(option, service)

        except ValueError:
            input("Invalid input, Try again...")

def sort_menu(service):
    while True:
        try:
            service.clear_screen()
            show_transactions(service)
            option = int(input("\n===========MENU===========\n"
                               "Which would you like to modify?\n"
                               "1 - Sort by name\n"
                               "2 - Sort by value\n"
                               "3 - Sort By data\n"
                               "4 - Increasing/Decreasing\n"
                               "0 - Return\n"
                               "Select an option: "))

            commands.sort_commands(option, service)

        except ValueError:
            input("Invalid input, Try again...")

def date_menu(service):
    while True:
        try:
            service.clear_screen()
            show_transactions(service)
            option = int(input("\n===========MENU===========\n"
                               "Which would you like to modify?\n"
                               "1 - Change month\n"
                               "2 - Change year\n"
                               "3 - Show by month\n"
                               "4 - Show by year\n"
                               "5 - Return to current date\n"
                               "0 - Return\n"
                               "Select an option: "))

            commands.date_commands(option, service)

        except ValueError:
            input("Invalid input, Try again...")

