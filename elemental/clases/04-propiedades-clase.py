class Perro:
    patas = 4
    
    def __init__(self, nombre, edad): 
        self.nombre = nombre
        self.edad = edad
        
    def habla(self):
        print(f" {self.nombre} dice: Guau!")
# propiedad = atributo
# Atención: en python hay una función que se llama propiedad
        
# se pueden cambiar las propiedades de clase, luego de haberlas definido
Perro.patas = 3 # cambia para todas las instancias
mi_perro = Perro("Chanchito", 1)
# cambiando la propiedad de patas solo para la instancia mi_perro
mi_perro.patas = 5
mi_perro2 = Perro("Felipe", 2)

print(Perro.patas) # se definio para todas las instancias 3 patas
print(mi_perro.patas) # se definió a esta instancia en específico 5 patas
print(mi_perro2.patas) # ahora tiene 3 patas por ser una instancia de la clase Perro que tiene 3 patas











