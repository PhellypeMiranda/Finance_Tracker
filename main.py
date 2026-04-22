from domain.repositories.transaction_repositories import TransactionRepository
from interface.cli import interface
from infrastructure.repositories.json_repository import JsonRepository
from use_cases.add_transaction import AddTransactionUseCase
from use_cases.remove_transaction import RemoveTransactionUseCase
from use_cases.get_transactions import GetTransactionsUseCase

def run():
    repository: TransactionRepository = JsonRepository()

    add_transaction = AddTransactionUseCase(repository)
    remove_transaction = RemoveTransactionUseCase(repository)
    get_transactions = GetTransactionsUseCase(repository)

    interface.main_menu(add_transaction, remove_transaction, get_transactions)

if __name__ == "__main__":
    run()