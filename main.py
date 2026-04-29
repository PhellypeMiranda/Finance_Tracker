import sys

from domain.repositories.transaction_repositories import TransactionRepository
from interface.cli import interface
from infrastructure.repositories.json_repository import JsonRepository
from application.use_cases.add_transaction import AddTransactionUseCase
from application.use_cases.remove_transaction import RemoveTransactionUseCase
from application.use_cases.get_transactions import GetTransactionsUseCase
from application.exceptions.exit_program import ExitProgram

def run():

    repository: TransactionRepository = JsonRepository()

    add_transaction = AddTransactionUseCase(repository)
    remove_transaction = RemoveTransactionUseCase(repository)
    get_transactions = GetTransactionsUseCase(repository)

    try:
        interface.main_menu(add_transaction, remove_transaction, get_transactions)
    except ExitProgram:
        print("Exiting program...")
        sys.exit(0)

if __name__ == "__main__":
    run()