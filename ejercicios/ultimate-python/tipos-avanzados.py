# para mejorar el formato de los iterables
from pprint import pprint
# Para  agregar caracteres especiales, como los acentos en los print
import sys
sys.stdout.reconfigure(encoding='utf-8')

##### Ejercicios
# 1. Eliminar los espacios en blanco de un string y devolver una lista con los caracteres restantes

# 2. Contar en un diccionario cuánto se repiten los caracteres de un string

# 3. Ordenar las llaves de un diccionario por el valor que tienen y devolver una lista que contiene tuplas [("a", 3), ("b", 2), ("c", 4), ("d", 4) ]

# 4. De un listado de tuplas, devolver las tuplas que tengan el mayor valor. [("a", 3), ("b", 2), ("c", 4)] -> [("c", 4)]

# 5. Crear un mensaje que diga: Los caracteres que más se repiten con 4 repeticiones son:
# - C
# - D

# 6. Juntar la solución de los ejercicios anteriores para encontrar los caracteres que más se repiten de un string.

##### Soluciones:

# Ejercicio 1
string = "Hola mundo este es mi string"
def quita_espacios(texto):
    # usando comprensión de listas
    return [char for char in texto if char != " "]


sin_espacios = quita_espacios(string)
print("Ejercicio 1:", sin_espacios)

# Ejercicio 2
# reutiliza código del ejercicio 1
def cuenta_caracteres(lista):
    chars_dict = {}
    for char in lista:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict


contados = cuenta_caracteres(sin_espacios)
print("Ejercicio 2:")
pprint(contados, width=1) # para este caso el width se puede sacar

# Ejercicio 3
# reutiliza código del ejercicio 2
def ordena(dict):
    # retorna una lista de tuplas con los caracteres que más se repiten al comienzo
    return sorted(
        dict.items(),
        key=lambda key: key[1],
        reverse=True, 
    )
    
    
ordenados = ordena(contados)
print("Ejercicio 3:")
pprint(ordenados)

# Ejercicio 4
# reutiliza código del ejercicio 3
def mayores_tuplas(lista):
    maximo = lista[0][1]
    respuesta = {}
    for orden in lista:
        if maximo > orden[1]:
            break
        respuesta[orden[0]] = orden[1]
    return respuesta   
    
mayores = mayores_tuplas(ordenados)
print("Ejercicio 4:\n", mayores)


# Ejercicio 5 
# reutiliza código del ejercicio 4
def crea_mensaje(diccionario):
    mensaje = "Los que más se repiten son: \n"
    for key, value in diccionario.items():
        mensaje += f"- {key} con {value} repeticiones \n"
    return mensaje
    
mensaje = crea_mensaje(mayores)
print("Ejercicio 5")
print(mensaje)    












