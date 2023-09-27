class Perro:
    def __init__(self, nombre, edad): 
        self.__nombre = nombre
        self.edad = edad
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def habla(self):
        print(f"{self.__nombre} dice: Guau!")    
        
    @classmethod # factory method
    def factory(cls):
        return cls("Chanchito feliz", 4)


perro1 = Perro.factory()
perro1.habla()
# Ya no se puede acceder así porque es una propiedad privada
# print(perro1.__nombre)
print(perro1.get_nombre())

# accediendo a las propiedades privadas, no se debería.
print(perro1.__dict__)
print(perro1._Perro__nombre)