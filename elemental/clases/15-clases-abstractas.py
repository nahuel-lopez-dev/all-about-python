from abc import ABC, abstractmethod
# abstractclass, props métodos

class Model(ABC):
    # el constructor ya no es necesario siendo una clase abstracta
    # def __init__(self):
    #     if not self.tabla:
    #         print("Error, tienes que definir una tabla")
    
    @property
    @abstractmethod        
    def tabla(self):
        pass
    
    @abstractmethod
    def guardar(self):
        pass
        # print(f"Guardando {self.tabla} en BBDD")
    
    @classmethod # para que lo haga la clase y no el usuario
    def buscar_por_id(self, _id):
        print(f"buscando por id {_id} en la tabla {self.tabla}")    
    
class Usuario(Model):
    tabla = "Usuario"   
    
    def guardar(self):
        print("guardando usuario")
         
    
# ahora ya no se puede instanciar la clase Model, porque es abstracta
# model = Model()
# Model.buscar_por_id(123)

usuario = Usuario()
usuario.guardar()
Usuario.buscar_por_id(123)




        
        