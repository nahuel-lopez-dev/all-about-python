# importando pymongo
import pymongo
# para que tome caracteres especiales y acentos
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

### Cadena de conexión de Mongo Atlas
MONGO_URL = "mongodb+srv://user:password@cluster0.hddmf7f.mongodb.net/?retryWrites=true&w=majority"
MONGO_BASEDATOS = "reto_mongo" # base de datos a utilizar
MONGO_COLECCION = "muertes" # coleccion a utilizar
MONGO_TIME_OUT=1000 #Por defecto necesita un time out para realizar la conexión

### Anticipando errores de ejecución usando 'TRY y EXCEPT'
try:
    ### Variable cliente que se va a conectar al cliente de Mongo
    cliente=pymongo.MongoClient(MONGO_URL,serverSelectionTimeoutMS=MONGO_TIME_OUT)
    db = cliente[MONGO_BASEDATOS]
    coleccion = db[MONGO_COLECCION]

    coleccion.insert_many([
        {"nombre_estado": "Alabama", "anio": 2000, "cantidad": 10622},
        {"nombre_estado": "Alabama", "anio": 2001, "cantidad": 15912},
        {"nombre_estado": "Florida", "anio": 2000, "cantidad": 38103},
        {"nombre_estado": "Florida", "anio": 2001, "cantidad": 166069},
        {"nombre_estado": "Georgia", "anio": 2000, "cantidad": 14804},
        {"nombre_estado": "Georgia", "anio": 2001, "cantidad": 15000},
        {"nombre_estado": "South Carolina", "anio": 2000, "cantidad": 8581},
        {"nombre_estado": "South Carolina", "anio": 2001, "cantidad": 9500}
    ])

    cliente.close()
    
# Error por exceso de tiempo de respuesta    
except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
    print("Tiempo excedido de carga")

# Error de conexión    
except pymongo.errors.ConnectionFailure as errorConexion:
    print("Fallo al conectarse a mongodb"+errorConexion)