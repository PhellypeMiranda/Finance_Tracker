from interface.cli import interface, commands
from domain.services.service import Service


def run():
    service = Service()
    service.load_ledger()
    option = interface.main_menu(service)
    commands.main_commands(option, service)

if __name__ == "__main__":
    run()