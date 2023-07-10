# importando pymongo
import pymongo
# para que tome caracteres especiales y acentos
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

### Cadena de conexión de Mongo Atlas
MONGO_URL = "mongodb+srv://user:password@cluster0.hddmf7f.mongodb.net/?retryWrites=true&w=majority"
MONGO_BASEDATOS = "reto_mongo" # base de datos a utilizar
MONGO_COLECCION = "estados" # coleccion a utilizar
MONGO_TIME_OUT=1000 #Por defecto necesita un time out para realizar la conexión

### Anticipando errores de ejecución usando 'TRY y EXCEPT'
try:
    ### Variable cliente que se va a conectar al cliente de Mongo
    cliente=pymongo.MongoClient(MONGO_URL,serverSelectionTimeoutMS=MONGO_TIME_OUT)
    db = cliente[MONGO_BASEDATOS]
    coleccion = db[MONGO_COLECCION]
      
    coleccion.insert_many([
    {"nombre_estado": "Alabama", "fundacion": "1819-12-14", "longitud": -86.829534, "latitud": 33.258882},
    {"nombre_estado": "Florida", "fundacion": "1845-03-03", "longitud": -81.463983, "latitud": 27.756767},
    {"nombre_estado": "Georgia", "fundacion": "1733-02-12", "longitud": -83.113737, "latitud": 32.329381},
    {"nombre_estado": "South Carolina", "fundacion": "1776-03-26", "longitud": -80.436374, "latitud": 33.687439}
    ])   
        
    cliente.close()
    
# Error por exceso de tiempo de respuesta    
except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
    print("Tiempo excedido de carga")

# Error de conexión    
except pymongo.errors.ConnectionFailure as errorConexion:
    print("Fallo al conectarse a mongodb"+errorConexion)