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
    def __init__(self, month=date.today().month, year=date.today().year):
        self.list = None
        self.balance = True
        self.income = True
        self.expense = True
        self.month = month
        self.year = year
        self.category = None
        self.sort = "date"
        self.increasing = True
        self.by_month = True

    def apply_filter(self, transaction_type):
        transaction_list = []
        for item in self.list:
            if item.transaction_type != transaction_type:
                continue
            if self.category and self.category != item.category:
                continue
            if self.by_month and item.transaction_date.month != self.month:
                continue
            if not self.month and item.transaction_date.year != self.year:
                continue
            transaction_list.append(item)
        return transaction_list

    def sort_list(self, transaction_list):
        sort_map = {
            "date": lambda x: x.transaction_date,
            "name": lambda x: x.name,
            "value": lambda x: x.amount
        }
        key_func = sort_map.get(self.sort)
        transaction_list.sort(key=key_func, reverse=not self.increasing)
        return transaction_list

    def date_setter(self, service):
        while True:
            try:
                dates_with_items = {} # create a dic to avoid duplicate items
                for i in self.list: # this shit gets all months that there's items without duplications
                    if self.by_month:
                        dates_with_items.update({i.transaction_date.month: i.transaction_date})
                    else:
                        dates_with_items.update({i.transaction_date.year: i.transaction_date})
                date_list = [] #create a list to get the items by index
                for i in dates_with_items.values():
                    date_list.append(i)
                not_empty = validation.check_if_not_empty(date_list)
                if not_empty:
                    index = user_input.change_date(service, date_list)
                    selected = date_list[index - 1]
                    self.month = selected.month
                    self.year = selected.year
                    if self.by_month:
                        input(f"Month changed to {format.month_year(selected)}")
                    else:
                        input(f"Year changed to {format.year(selected)}")
                interface.date_menu(service)
            except (ValueError, IndexError):
                print("Please enter a valid month!")

    def toggle_increasing(self):
        self.increasing = not self.increasing

    def load_ledger(self):
        self.list = Ledger()
        self.list.convert_ledger_to_obj(FileHandler().load_data())

    def add_transaction(self, service):
        transaction_type = interface.transaction_type_menu(service, "add")
        name = user_input.type_name(f"\nType the name of the {transaction_type.value}: ")
        amount = user_input.type_amount(f"Type the value of the {transaction_type.value}: ")
        category = interface.category_menu(service, transaction_type)
        current_date = user_input.confirmation(f"Add today's date: {format.today_date()}?")
        if current_date:
             transaction_date = date.today()
        else:
            transaction_date = user_input.type_date(f"Enter other date (YYYY-MM-DD):")
        new_transaction = Transaction(name, transaction_type, amount, category, transaction_date)
        self.list.add_item(new_transaction)
        self.save_ledger()
        interface.main_menu(service)

    def remove_transaction(self, service):
        transaction_type = interface.transaction_type_menu(service, "remove")
        transactions_list = self.apply_filter(transaction_type)
        not_empty = validation.check_if_not_empty(transactions_list)
        if not_empty:
            index = user_input.type_index(f"\nType the id of the {transaction_type.value} you want to remove: ", len(transactions_list))
            confirm = user_input.confirmation(f"Remove the {transaction_type.value}?")
            if confirm:
                for i in self.list:
                    if i == transactions_list[index - 1]:
                        self.list.remove_item(i)
                        input(f"{i.name} has been removed!")
            else:
                input("operation cancelled, press any key to continue...")
            self.save_ledger()
        interface.main_menu(service)

    def modify_transaction(self, service):
        transaction_type = interface.transaction_type_menu(service, "modify")
        transactions_list = self.apply_filter(transaction_type)
        not_empty = validation.check_if_not_empty(transactions_list)
        if not_empty:
            index = user_input.type_index(f"\nType the id of the {transaction_type.value} you want to modify: ",
                                          len(transactions_list))
            for i in self.list:
                if i == transactions_list[index - 1]:
                    interface.modify_menu(service, i)
            self.save_ledger()
        self.income = True
        self.expense = True
        self.balance = True
        interface.main_menu(service)

    def save_ledger(self):
        dict_transactions = self.list.convert_ledger_to_dict()
        saver = FileHandler()
        saver.save_data(dict_transactions)

    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def exit():
        confirmation = user_input.confirmation("Are you sure you want to exit?")
        if confirmation:
            sys.exit(0)
