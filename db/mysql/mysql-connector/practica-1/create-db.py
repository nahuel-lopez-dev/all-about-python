# Configuración de la conexión Python y MySQL
# Importando connector de mysql
import mysql.connector
# Para  agregar caracteres especiales
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Crear conexión a la base de datos
conexion=mysql.connector.connect(
    host='localhost',
    user='root', 
    password='password',
    port='3306',
    charset='utf8') 

# Crear el cursor
cursor = conexion.cursor()

# Imprimiendo la conexion, para ver si fue exitosa
print(conexion)

###### Creando la base de datos reto_mysql ######
cursor.execute("CREATE DATABASE reto_mysql;")
