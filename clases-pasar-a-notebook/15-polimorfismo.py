from abc import ABC, abstractmethod

class Model(ABC):
    @abstractmethod
    def guardar(self):
        pass
    
class Usuario(Model):
    def guardar(self):
        print("guardando en BBDD")
        
class Sesion(Model):
    def guardar(self):
        print("guardando en archivo")

# aplicacón de polimorfismo        
def guardar(entidades):
    for entidad in entidades:
        entidad.guardar()
    
usuario = Usuario()
sesion = Sesion()

# polimorfismo
# para ahorrar trabajo
# Creamos varios objetos que tengan una interfaz muy similar
# en este caso sería el método de guardar, y luego se los 
# pasamos a una función que se va a encargar que se llamar
# a la función de guardar de cada uno de estos objetos sin
# necesidad de tener que llamar a sesion.guardar y 
# usuario.guardar
guardar([sesion, usuario])





    
    