# importando el conector a MySQL
import pymysql
# importando sys para trabajar con caracteres especiales como acentos
import sys
sys.stdout.reconfigure(encoding='utf-8')

CREATE_DB = """CREATE DATABASE IF NOT EXISTS python_pymysql"""

# creando la conexión
if __name__ == '__main':
    
    try:
        connect = pymysql.Connect(
            host='localhost',
            port=3306,
            user='root',
            passwd=''
        )
        # creando el cursor    
        cursor = connect.cursor()
        # ejecutando la query
        cursor.execute(CREATE_DB)
        # imprimiendo mensaje de conexión exitosa y db creada
        print('Conexión realizada de forma exitosa y database creada')
    
    except pymysql.err.OperationalError as err:
        print('No fue posible realizar la conexión')
        print(err)
    
    finally:
        cursor.close()
        connect.close()
        print('Conexión finalizada de forma exitosa')