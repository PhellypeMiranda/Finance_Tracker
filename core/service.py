import os
import sys
from storage.file_handler import FileHandler
from models.ledger import Ledger
from utils import user_input
from cli import interface
from datetime import date
from utils import format
from models.transaction import Transaction

class Service:
    def __init__(self, month=date.today().month, year=date.today().year, category=None):
        self.service = None
        self.balance = True
        self.income = False
        self.expense = False
        self.month = month
        self.year = year
        self.category = category

    def filter_category(self, category):
        print("\n===========================EXPENSE===========================\n"
              f"{"Name":<20}{"Value":<15}{"Category":<15}{"Date":<10}")
        return list(i for i in self.service if i.category.value == category)

    def load_ledger(self):
        self.service = Ledger()
        self.service.convert_ledger_to_obj(FileHandler().load_data())

    def add_transaction(self, service):
        transaction_type = interface.transaction_type_menu(service)
        name = user_input.type_name("Type the name of the transaction: ")
        amount = user_input.type_amount("Type the value of the transaction: ")
        category = interface.category_type_menu(service, transaction_type)
        current_date = user_input.confirmation(f"Add today's date: {format.today()}?")
        if current_date:
             transaction_date = date.today()
        else:
            transaction_date = user_input.type_date(f"Enter other date (YYYY-MM-DD):")
        new_transaction = Transaction(name, transaction_type, amount, category, transaction_date)
        self.service.add_transaction(new_transaction)
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
