from cli import commands
from models.category import Category

def main_menu(service):
    service.clear_screen()
    show_transactions(service)
    option = int(input("\n===========MENU===========\n"
          "1 - Add new transaction\n"
          "2 - Remove a transaction\n"
          "3 - Modify a transaction\n"
          "4 - See all transactions\n"
          "5 - Show statistics\n"
          "0 - Exit\n"
          "Select an option: "))

    commands.main_menu_commands(option, service)

def transactions_menu(service):
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

    commands.transactions_menu_commands(option, service)

def transaction_type_menu(service):
    service.clear_screen()
    show_transactions(service)
    option = int(input("\n===========MENU===========\n"
          "What kind of transaction do you want to add?\n"
          "1 - Add an income\n"
          "2 - Add an expense\n"
          "0 - Return\n"
          "Select an option: "))

    return commands.transaction_type_commands(option, service)

def category_type_menu(service, transaction_type):
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
    return commands.category_type_commands(option, service, transaction_type)

def show_transactions(service):
    if service.balance:
        total_income = 0
        for i in service.service:
            if i.transaction_type.value == "income":
                total_income += i.amount

        total_expense = 0
        for i in service.service:
            if i.transaction_type.value == "expense":
                total_expense += i.amount

        print("\n============BALANCE============\n"
              f"\nTotal income: $:{total_income:.2f}\n"
              f"Total expense: $:{total_expense:.2f}\n"
              f"Total Balance: $:{total_income - total_expense:.2f}")

    if service.income:
        print("\n===========================INCOME===========================\n"
              f"{"Name":<20}{"Value":<15}{"Category":<15}{"Date":<10}")
        for i in service.service:
            if i.transaction_type.value == "income":
                print(i)

    if service.expense:
        print("\n==========================EXPENSES===========================\n"
              f"{"Name":<20}{"Value":<15}{"Category":<15}{"Date":<10}")
        for i in service.service:
            if i.transaction_type.value == "expense":
                print(i)

