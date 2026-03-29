from cli import interface
from core.service import Service

def main():
    service = Service()
    service.load_ledger()
    interface.main_menu(service)

if __name__ == "__main__":
    main()