import time # opción no recomendada
# import datetime # es mejor usar datetime

# una mejor opción con datetime
from datetime import datetime

# Devuelve un timestamp
# Es la cantidad de segundos que han ocurrido desde el 1° de Enero de 1970
print(time.time())
# Es con respecto a UTC (Coordinated Universal Time)
# UTC-0
# --> Greenwich England

# formato datetime(año, mes, día)

# importando datetime
# fecha = datetime.datetime(2023, 3, 26)

# ya no es necesario acceder con notación de punto usando from datetime import datetime 
fecha1 = datetime(2023, 3, 26)
fecha2 = datetime(2023, 10, 6)
fecha_actual = datetime.now()

print(fecha1)
print(fecha2)
print(fecha_actual)

# para más info ver las directivas de strptime en la página
fecha_str = datetime.strptime("2023-01-03", "%Y-%m-%d") # al segundo argumento se le llaman directivas
print(fecha_str)

# como crear un string a partir de una fecha
print(fecha1.strftime("%Y.%m.%d"))

# comparando fechas
print(fecha1 > fecha2)

# propiedades del objeto fecha1
print(
    fecha1.year,
    fecha1.month,
    fecha1.day,
    fecha1.hour,
    fecha1.minute
)


