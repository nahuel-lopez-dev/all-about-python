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

############### Creando las tablas ###############
# Guardando cada query en una variable, por buenas prácticas
crear_tabla_estados = """
CREATE TABLE estados (
    id_estado INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nombre_estado VARCHAR(50),
    fundacion DATE,
    longitud FLOAT,
    latitud FLOAT
);
"""

crear_tabla_poblaciones = """
CREATE TABLE poblacion (
    id_poblacion INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nombre_estado VARCHAR(50) NOT NULL,
    anio INT,
    cantidad INT,
    id_estado INT,
    FOREIGN KEY (id_estado) REFERENCES estados(id_estado)
);
"""

crear_tabla_muertes = """
CREATE TABLE muertes (
    id_muertes INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nombre_estado VARCHAR(50),
    anio INT,
    cantidad INT,
    id_poblacion INT,
    FOREIGN KEY (id_poblacion) REFERENCES poblacion(id_poblacion)
);
"""

crear_tabla_residentes_men65 = """
CREATE TABLE residentes_men65 (
    id_residentes_men65 INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nombre_estado VARCHAR(50),
    anio INT,
    cantidad INT,
    id_poblacion INT,
    FOREIGN KEY (id_poblacion) REFERENCES poblacion(id_poblacion)
);
"""

# Ejecutando las querys
cursor.execute(crear_tabla_estados)
cursor.execute(crear_tabla_poblaciones)
cursor.execute(crear_tabla_muertes)
cursor.execute(crear_tabla_residentes_men65)

# Guardando los cambios
conexion.commit()