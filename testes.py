from datetime import date
hoy = date.today()
manana = date(2023,4,11)
print(manana.strftime("%d/%m/%Y"))