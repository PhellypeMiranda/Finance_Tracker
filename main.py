from domain.repositories.transaction_repositories import TransactionRepository
from interface.cli import interface, commands
from domain.services.service import Service
from infrastructure.repositories.json_repository import JsonRepository
from use_cases.add_transaction import AddTransaction
from use_cases.remove_transaction import RemoveTransaction
from use_cases.get_transactions import GetTransactions

def run():
    #Loads the service, repository and data
    repository: TransactionRepository = JsonRepository()
    service = Service(repository)

    #load the use cases
    add_transaction = AddTransaction(service, repository)
    remove_transaction = RemoveTransaction(service, repository)
    get_transactions = GetTransactions(service)

    interface.main_menu(add_transaction, remove_transaction, get_transactions)

if __name__ == "__main__":
    run()