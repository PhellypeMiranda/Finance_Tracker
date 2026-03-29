from datetime import date

def today():
    return date.today().strftime("%d/%m/%Y")