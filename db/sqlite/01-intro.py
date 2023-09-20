import sqlite3

# si el archivo no existe, python lo va a crear
con = sqlite3.connect("db/sqlite/app.db")
con.close()

