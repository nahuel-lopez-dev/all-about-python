# importando el conector 
import pymysql
# Para  agregar caracteres especiales
import sys
sys.stdout.reconfigure(encoding='utf-8')

CREATE_DB = """CREATE DATABASE IF NOT EXISTS pythondb"""

if __name__ == '__main__':
    
    try:
        connect = pymysql.Connect(
            host = 'localhost',
            port = 3306,
            user = 'root',
            passwd = ''
        )
        
        cursor = connect.cursor()
        
        cursor.execute(CREATE_DB)
        
        print('Conexión realizada de forma exitosa, database creada')
        
    except pymysql.err.OperationalError as err:
        print('No fue posible realizar la conexión')
        print(err)
    
    finally:
        cursor.close()
        connect.close()    
        print('Conexión finalizada de forma exitosa')    