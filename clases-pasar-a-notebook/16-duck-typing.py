class Usuario():
    def guardar(self):
        print("guardando en BBDD")
        
class Sesion():
    def guardar(self):
        print("guardando en archivo")

# aplicacón de polimorfismo
# en este caso solo se revisa que sea un listado
# y que tenga el método de guardar
# por eso sigue funcionando. No revisa que herede de Modelo        
def guardar(entidades):
    for entidad in entidades:
        entidad.guardar()
    
usuario = Usuario()
sesion = Sesion()

guardar([sesion, usuario])

# Duck Typing
# si camina como pato y suena como pato, entonces es un pato
 

    
    