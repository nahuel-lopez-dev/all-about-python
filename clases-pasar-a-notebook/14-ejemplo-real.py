class Model():
    tabla = False
    def __init__(self):
        if not self.tabla:
            print("Error, tienes que definir una tabla")
    
    def guardar(self):
        print(f"Guardando {self.tabla} en BBDD")
    
    @classmethod # para que lo haga la clase y no el usuario
    def buscar_por_id(self, _id):
        print(f"buscando por id {_id} en la tabla {self.tabla}")    
    
class Usuario(Model):
    tabla = "Usuario"    
    

usuario = Usuario()

usuario.guardar()
Usuario.buscar_por_id(123)


        
        