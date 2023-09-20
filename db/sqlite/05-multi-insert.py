import sqlite3

with sqlite3.connect("db/sqlite/app.db") as con:
    cursor = con.cursor()
    usuarios = [
        (2, "Chanchito Feliz"),
        (3, "Chanchito Triste"),
    ]
    cursor.executemany(
        "insert into usuarios values(?, ?)",
        usuarios, 
    ) # para evitar una SQL Injection


