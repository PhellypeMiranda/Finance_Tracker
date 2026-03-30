from decimal import Decimal
from datetime import date

def confirmation(message):
    while True:
        confirm = input(f"{message} (y/n): ").lower().strip()
        if confirm == "y":
            return True
        elif confirm == "n":
            return False
        else:
            print("Please respond with 'y' or 'n'")

def type_name(message):
    while True:
        try:
            name = input(message).lower().strip()
            return name
        except EOFError:
            print("Invalid input, please try again")

def type_amount(message):
    while True:
        try:
            value = float(input(message))
            Decimal(value)
            return value
        except ValueError:
            print("Invalid input, please try again")

def type_date(message):
    while True:
        try:
            new_date = date.fromisoformat(input(message))
            input("New date add successfully, press any key to continue...")
            return new_date
        except (ValueError, TypeError):
            print("Invalid date, please try again")

def type_index(message, length):
    while True:
        try:
            index = int(input(message))
            if index < 1 or index > length:
                print("Invalid input, please try again")
                continue
            else:
                return index
        except ValueError:
            print("Invalid input, please try again")

def change_date(service, dates_with_items):
    while True:
        try:
            count = 1
            print("\nChoose a date:")
            for i in dates_with_items:
                if service.by_month:
                    print(f"{count} - {i.strftime('%B/%Y')}")
                else:
                    print(f"{count} - {i.strftime('%Y')}")
                count += 1
            option = int(input("Select a option: "))
            return option
        except ValueError:
            input("Invalid input, Try again...")
