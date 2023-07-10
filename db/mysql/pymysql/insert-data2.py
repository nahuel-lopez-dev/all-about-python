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
            # usando el método format (forma no recomendada)            
            # query = "INSERT INTO users(username, password, email) VALUES('{}', '{}', '{}')".format(
            #     "user1",
            #     "password123",
            #     "user1@gmail.com"
            # )
            
            # usando f-strings (más recomendada que la anterior)
            username = "user1"
            password = "password123"
            email = "user1@gmail.com"
            
            query = f"INSERT INTO users(username, password, email) VALUES('{username}', '{password}', '{email}')"
            
            # ejecutando con execute la query
            cursor.execute(query)
            # para poder persistir todos los cambios realizados
            connect.commit()   
            
    except pymysql.err.OperationalError as err:
        print('No fue posible realizar la conexión')
        print(err)
    
    
    finally:
        # cursor.close() # No hace falta indicar que el cursor se cierre ahora
        connect.close()    
        print('Conexión finalizada de forma exitosa')        