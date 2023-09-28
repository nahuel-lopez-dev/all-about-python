##### Métodos mágicos
# son métodos que se van a ejecutar cuando 
# no los estemos llamando directamente
# el constructor es un claro ejemplo. Se ejecuta indirectamente.
# Siempre todos comienzan con dos guiones bajos __ y terminan con dos guiones bajos __

class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def __str__(self):
        return f"Clase Perro: {self.nombre}"
        
    def habla(self):
        print(f"{self.nombre} dice: Guau!")
        

perro = Perro("Chanchito", 7)
print(perro)
texto = str(perro)
print(texto)




