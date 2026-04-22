from datetime import date

def today_date():
    return date.today().strftime("%d/%m/%Y")

def month_year(transaction_date):
    return transaction_date.strftime("%B/%Y")

def year(transaction_date):
    return transaction_date.strftime("%Y")