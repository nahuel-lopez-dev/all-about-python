# class Animal:
#     # este método es común a todos los animales, como Perro y Chanchito
#     def comer(self):
#         print("comiendo")
    
#     # los métodos no deben repetirse para evitar problemas en las implementaciones
#     # def pasear(self):
#     #     print("paseando animales")
        
        
# class Perro:
#     def pasear(self):
#         print("paseando al perro")
        
# # herencia múltiple
# class Chanchito(Perro, Animal):
#     def programar(self):
#         print("programando")
        
# perro = Perro()
# chanchito = Chanchito()
# chanchito.comer

class Caminador:
    def caminar(self):
        print("Caminando")

class Volador:
    def volar(self):
        print("volando")

class Nadador:
    def nadar(self):
        print("nadando")

class Pato(Caminador, Volador, Nadador):
    def programar(self):
        print("programando")
        
pato = Pato()
pato.caminar()
pato.nadar()
pato.volar()
pato.programar()



