class Animal:
    # este método es común a todos los animales, como Perro y Chanchito
    def comer(self):
        print("comiendo")
        
# hereda de la clase Animal
class Perro(Animal):
    def pasear(self):
        print("paseando")
        
# hereda de la clase Perro (herencia multinivel)        
class Chanchito(Perro):
    def programar(self):
        print("programando")
        

perro = Perro()
chanchito = Chanchito()
perro.comer()
chanchito.comer

# Nota:
# Tratar de evitar la herencia multinivel.
# De usarla, que no sea más de 2 o 3 niveles.
# De lo contrario, pueden surgir problemas con las clases.
