import sqlite3

with sqlite3.connect("db/sqlite/app.db") as con:
    cursor = con.cursor()
    cursor.execute(
        """
        CREATE TABLE if not exists usuarios
        (id INTEGER primary key, nombre VARCHAR(50));
        """
    )

# no necesita el método commit() ni cerrar la conexión()
# con with se llama a los objetos que se devuelven en la conexión
# que en este caso contienen al método __exit__ que se encarga de
# hacer el commit si no hay errores, y de cerrar la conexión



    




