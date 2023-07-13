# importando mysql connector
import mysql.connector
# importando sys para trabajar caracteres especiales
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Crear conexión a la base de datos
conexion = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    port='3306',
    chartset='utf-8'
)

# Crear el cursor
cursor = conexion.cursor()

# Imprimiendo la conexion, para ver si fue exitosa
print(conexion)

# ejecutando la query
cursor.execute("CREATE DATABASE IF NOT EXISTS mysql_connector;")

