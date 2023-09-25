
# self, palabra reservada que se utiliza dentro de todas 
# clases que se encuentran en python. Sirve para referenciar
# las instancias de las clases. 
# Va a cambiar dependiendo de cada instancia

# El constructor se define con la palabra reservada __init__
class Perro:
    def __init__(self, nombre, edad): 
        self.nombre = nombre
        self.edad = edad
        
    def habla(self):
        print(f" {self.nombre} dice: Guau!")
        
mi_perro = Perro("Chanchito", 1)
mi_perro2 = Perro("Felipe", 2)

# self hace referencia a la instancia de la clase
print(mi_perro.nombre)
mi_perro.habla()
print(mi_perro2.nombre)
mi_perro2.habla()









