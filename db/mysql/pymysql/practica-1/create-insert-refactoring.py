# importando el conector 
import pymysql
# Para  agregar caracteres especiales
import sys
sys.stdout.reconfigure(encoding='utf-8')

DROP_TABLE_USERS = """DROP TABLE IF EXISTS users"""

USERS_TABLE = """
CREATE TABLE users(
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL, 
    password VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
"""

if __name__ == '__main__':
    
    try:
        connect = pymysql.Connect(
            host = 'localhost',
            port = 3306,
            user = 'root',
            passwd = '',
            db = 'pythondb'
        )
        # para trabajar con el cursor bajo un contexto
        with connect.cursor() as cursor:
        
            cursor.execute(DROP_TABLE_USERS)
            cursor.execute(USERS_TABLE)
            # inserción usando placeholders %s (requiere dos argumentos)
            query = "INSERT INTO users(username, password, email) VALUES(%s, %s, %s)"
            values = ("Nahuel_DevOne", "password123", "nahuel.developer1@gmail.com")
            
            cursor.execute(query, values) 
            # para poder persistir todos los cambios realizados
            connect.commit()   
            
    except pymysql.err.OperationalError as err:
        print('No fue posible realizar la conexión')
        print(err)
    
    
    finally:
        # cursor.close() # No hace falta indicar que el cursor se cierre ahora
        connect.close()    
        print('Conexión finalizada de forma exitosa')        