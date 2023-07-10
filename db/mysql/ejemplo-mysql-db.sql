# Creando la base de datos
CREATE DATABASE reto_mysql;

# Seleccionando la base de datos creada
USE reto_mysql;

# Creando las tablas
CREATE TABLE estados (
    id_estado INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nombre_estado VARCHAR(50),
    fundacion DATE,
    longitud FLOAT,
    latitud FLOAT
);

CREATE TABLE poblacion (
    id_poblacion INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nombre_estado VARCHAR(50) NOT NULL,
    anio INT,
    cantidad INT,
    id_estado INT,
    FOREIGN KEY (id_estado) REFERENCES estados(id_estado)
);

CREATE TABLE muertes (
    id_muertes INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nombre_estado VARCHAR(50),
    anio INT,
    cantidad INT,
    id_poblacion INT,
    FOREIGN KEY (id_poblacion) REFERENCES poblacion(id_poblacion)
);

CREATE TABLE residentes_men65 (
    id_residentes_men65 INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nombre_estado VARCHAR(50),
    anio INT,
    cantidad INT,
    id_poblacion INT,
    FOREIGN KEY (id_poblacion) REFERENCES poblacion(id_poblacion)
);

# Insertando los datos en las tablas
INSERT INTO estados (id_estado, nombre_estado, fundacion, longitud, latitud) 
VALUES 
    (1, 'Alabama', '1819-12-14', -86.829534, 33.258882), 
    (2, 'Florida', '1845-03-03', -81.463983, 27.756767), 
    (3, 'Georgia', '1733-02-12', -83.113737, 32.329381), 
    (4, 'South Carolina', '1776-03-26', -80.436374, 33.687439);

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
    
## Código comentado para mostrar los datos en cada tabla ##    
#SELECT * FROM estados;
#SELECT * FROM poblacion;
#SELECT * FROM muertes;
#SELECT * FROM residentes_men65;