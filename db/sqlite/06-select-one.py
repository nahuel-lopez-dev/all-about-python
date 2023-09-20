import sqlite3

with sqlite3.connect("db/sqlite/app.db") as con:
    cursor = con.cursor()
    cursor.execute("SELECT * FROM usuarios") # no hace falta asignarlo a una variable
    # se guarda dentro de cursor
    print(cursor.fetchone()) # devuelve el primer registro
    