from cli import interface
from core.service import Service
from cli import commands

def run():
    service = Service()
    service.load_ledger()
    option = interface.main_menu(service)
    commands.main_commands(option, service)

if __name__ == "__main__":
    run()