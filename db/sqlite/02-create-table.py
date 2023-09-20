import sqlite3

con = sqlite3.connect("db/sqlite/app.db")
# para poder realizar consultas, objeto cursor
cursor = con.cursor()

cursor.execute(
    """
    CREATE TABLE if not exists usuarios
    (id INTEGER primary key, nombre VARCHAR(50));
    """
)

# para realizar los cambios, si o si
# la consulta no se va a realizar si no se realiza el commit()
con.commit()

# para cerrar la conexión
con.close()



