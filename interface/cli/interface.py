import os
from interface.cli import commands


def main_menu(add_transaction, remove_transaction, get_transactions):
    while True:
        try:
            show_transactions(get_transactions)
            option = int(input("\n===========MENU===========\n"
                               "1 - Add new transaction\n"
                               "2 - Remove a transaction\n"
                               "3 - Modify a transaction\n"
                               "4 - Organize transactions\n"
                               "5 - Change date\n"
                               "6 - Show statistics\n"
                               "0 - Exit\n"
                               "Select an option: "))

            commands.main_commands(option, add_transaction, remove_transaction, get_transactions)

        except ValueError:
            input("Invalid input, type a number!")

def modify_menu(service, transaction):
    while True:
        try:
            option = int(input("\n===========MENU===========\n"
                               "Which would you like to modify?\n"
                               "1 - Name\n"
                               "2 - Value\n"
                               "3 - Type and category\n"
                               "4 - Category\n"
                               "5 - Date\n"
                               "Select an option: "))

            commands.modify_commands(option, service, transaction)

        except ValueError:
            input("Invalid input, Try again...")

def transaction_type_menu(operation_type):
    while True:
        try:
            option = int(input("\n===========MENU===========\n"
                               f"Which kind of transaction do you want to {operation_type}?\n"
                               f"1 - {operation_type} income\n"
                               f"2 - {operation_type} expense\n"
                               "Select an option: "))

            if 1 <= option <= 2:
                return commands.transaction_type_commands(option)
            else:
                input("Invalid input, Try again...")

        except ValueError:
            input("Invalid input, Try again...")

def category_menu(transaction_type):
    while True:
        try:
            print("\n===========MENU===========\n"
                  "Select a category for your transaction:\n")
            if transaction_type.value == "income":
                option = int(input("1: Salary\n"
                                   "2: Freelance\n"
                                   "3: Investment\n"
                                   "4: Bonus\n"
                                   "5: Others\n"
                                   "Select an option: "))
                if 1 <= option <= 5:
                    return commands.category_type_commands(option, transaction_type)
                else:
                    input("Invalid input, Try again...")

            if transaction_type.value == "expense":
                option = int(input("1: Food\n"
                                   "2: Transport\n"
                                   "3: Housing\n"
                                   "4: Utilities\n"
                                   "5: Health\n"
                                   "6: Entertainment\n"
                                   "7: Education\n"
                                   "8: Shopping\n"
                                   "9: Subscription\n"
                                   "10: Others\n"
                                   "Select an option: "))

                if 1 <= option <= 10:
                    return commands.category_type_commands(option, transaction_type)
                else:
                    input("Invalid input, Try again...")

        except ValueError:
            input("Invalid input, Try again...")

def show_transactions(get_transactions):
    os.system('cls' if os.name == 'nt' else 'clear')

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
            if option == 0:
                return
            else:
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

            if option == 0:
                return
            else:
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

            if option == 0:
                return
            else:
                commands.date_commands(option, service)

        except ValueError:
            input("Invalid input, Try again...")

