import os
import sys
from storage.file_handler import FileHandler
from models.ledger import Ledger
from utils import user_input
from cli import interface
from datetime import date
from utils import format
from models.transaction import Transaction
from utils import validation as validation

class Service:
    def __init__(self, month=date.today().month, year=date.today().year, category=None):
        self.service = None
        self.balance = True
        self.income = False
        self.expense = False
        self.month = month
        self.year = year
        self.category = category

    def create_list(self, transaction_type):
        new_list = [i for i in self.service  if i.transaction_type == transaction_type]
        return new_list

    def load_ledger(self):
        self.service = Ledger()
        self.service.convert_ledger_to_obj(FileHandler().load_data())

    def add_transaction(self, service):
        transaction_type = interface.transaction_type_menu(service, "add")
        name = user_input.type_name(f"\nType the name of the {transaction_type.value}: ")
        amount = user_input.type_amount(f"Type the value of the {transaction_type.value}: ")
        category = interface.category_type_menu(service, transaction_type)
        current_date = user_input.confirmation(f"Add today's date: {format.today()}?")
        if current_date:
             transaction_date = date.today()
        else:
            transaction_date = user_input.type_date(f"Enter other date (YYYY-MM-DD):")
        new_transaction = Transaction(name, transaction_type, amount, category, transaction_date)
        self.service.add_item(new_transaction)
        self.save_ledger()
        interface.main_menu(service)

    def remove_transaction(self, service):
        transaction_type = interface.transaction_type_menu(service, "remove")
        transactions_list = self.create_list(transaction_type)
        not_empty = validation.check_if_not_empty(transactions_list)
        if not_empty:
            index = user_input.type_index(f"\nType the id of the {transaction_type.value} you want to remove: ", len(transactions_list))
            confirm = user_input.confirmation(f"Remove the {transaction_type.value}?")
            if confirm:
                for i in self.service:
                    if i == transactions_list[index - 1]:
                        self.service.remove_item(i)
                        input(f"{i.name} has been removed!")
            else:
                input("operation cancelled, press any key to continue...")
            self.save_ledger()
        interface.main_menu(service)

    def save_ledger(self):
        dict_transactions = self.service.convert_ledger_to_dict()
        saver = FileHandler()
        saver.save_data(dict_transactions)

    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def exit():
        user_input.confirmation("Are you sure you want to exit?")
        sys.exit(0)
