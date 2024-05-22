# Notación PascalCase o UpperCamelCase 
# (se refieren a la misma notación)
class Perro:
    # métodos: son funciones que se encuentran dentro de una clase
    # el primer parámetro siempre es self
    def habla(self):
        print("Guau")


mi_perro = Perro()
print(type(mi_perro))        
# __main__ el módulo desde donde se está creando la instancia de Perro

# llamando a un método
mi_perro.habla()
# para saber si un objeto es una instancia de una clase
print(isinstance(mi_perro, Perro))



