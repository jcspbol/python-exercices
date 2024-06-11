import calendar
from datetime import date
from datetime import datetime
year=int(input("Ingrese el año: "))
month=int(input("Ingrese el mes(Numeral): "))
cal=calendar.month(year,month)
print("Calendario solicitado:")
print(cal)
#dia actual
today=date.today()
#fecha actual
now=datetime.now()
print(f"Dia Actual: ",today)
print("El dia Actual: {}".format(today.day))
print("El mes Actual: {}".format(today.month))
print("El año Actual: {}".format(today.year))
print(f"Fecha actual: ",now)
print("El dia Actual: {}".format(now.day))
print("El mes Actual: {}".format(now.month))
print("El año Actual: {}".format(now.year))
print("La hora Actual: {}".format(now.hour))
print("El minuto Actual: {}".format(now.minute))
print("El segundo Actual: {}".format(now.second))