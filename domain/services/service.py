import sys
from utils import user_input, validation as validation
from interface.cli import interface
from domain.entities.ledger import Ledger


class Service:
    def __init__(self, repository):
        self.repository = repository
        self.ledger = Ledger(self.repository.load_data())

    def add_transaction(self, new_transaction):
        self.ledger.add_item(new_transaction)

    def remove_transaction(self, transaction):
        self.ledger.remove_item(transaction)

    def modify_transaction(self, service):
        transaction_type = interface.transaction_type_menu(service, "modify")
        transactions_list = self.apply_filter(transaction_type)
        not_empty = validation.check_if_not_empty(transactions_list)
        if not_empty:
            index = user_input.type_index(f"\nType the id of the {transaction_type.value} you want to modify: ",
                                          len(transactions_list))
            for i in self.ledger:
                if i == transactions_list[index - 1]:
                    interface.modify_menu(service, i)
            self.save_ledger()
        self.income = True
        self.expense = True
        self.balance = True
        interface.main_menu(service)

    @staticmethod
    def exit():
        confirmation = user_input.confirmation("Are you sure you want to exit?")
        if confirmation:
            sys.exit(0)
