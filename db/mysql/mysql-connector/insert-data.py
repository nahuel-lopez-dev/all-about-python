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
    database='reto_mysql',
    charset='utf8') 

# Crear el cursor
cursor = conexion.cursor()

############# Insertando los datos ##############

insertar_datos_estados = """
INSERT INTO estados (id_estado, nombre_estado, fundacion, longitud, latitud) 
VALUES 
    (1, 'Alabama', '1819-12-14', -86.829534, 33.258882), 
    (2, 'Florida', '1845-03-03', -81.463983, 27.756767), 
    (3, 'Georgia', '1733-02-12', -83.113737, 32.329381), 
    (4, 'South Carolina', '1776-03-26', -80.436374, 33.687439);    
"""

insertar_datos_poblacion = """
INSERT INTO poblacion (id_poblacion, nombre_estado, anio, cantidad, id_estado)
VALUES
    (1, 'Alabama', 2000, 4447100, 1),
    (2, 'Alabama', 2001, 4451493, 1),
    (3, 'Florida', 2000, 15982378, 2),
    (4, 'Florida', 2001, 17054000, 2),
    (5, 'Georgia', 2000, 8186453, 3),
    (6, 'Georgia', 2001, 8229823, 3),
    (7, 'South Carolina', 2000, 4012012, 4),
    (8, 'South Carolina', 2001, 4023438, 4);
"""

insertar_datos_muertes = """
INSERT INTO muertes (id_muertes, nombre_estado, anio, cantidad, id_poblacion)
VALUES
    (1, 'Alabama', 2000, 10622, 1),
    (2, 'Alabama', 2001, 15912, 2),
    (3, 'Florida', 2000, 38103, 3),
    (4, 'Florida', 2001, 166069, 4),
    (5, 'Georgia', 2000, 14804, 5),
    (6, 'Georgia', 2001, 15000, 6),
    (7, 'South Carolina', 2000, 8581, 7),
    (8, 'South Carolina', 2001, 9500, 8);
"""

insertar_datos_residentes_men65 = """
INSERT INTO residentes_men65 (id_residentes_men65, nombre_estado, anio, cantidad, id_poblacion)
VALUES
    (1, 'Alabama', 2000, 3870598, 1),
    (2, 'Alabama', 2001, 3880476, 2),
    (3, 'Florida', 2000, 13237167, 3),
    (4, 'Florida', 2001, 13548077, 4),
    (5, 'Georgia', 2000, 7440877, 5),
    (6, 'Georgia', 2001, 7582146, 6),
    (7, 'South Carolina', '2000', 3535770, 7),
    (8, 'South Carolina', '2001', 3567172, 8);
"""

# Ejecutando las querys
cursor.execute(insertar_datos_estados)
cursor.execute(insertar_datos_poblacion)
cursor.execute(insertar_datos_muertes)
cursor.execute(insertar_datos_residentes_men65)

# Guardando los cambios
conexion.commit()    
# Cerrando el cursor y la conexion
cursor.close()
conexion.close()