# Mouredev
# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=10872

### Lists ###
# Definición de listas
my_list = list()
my_other_list = [] # una lista vacía

print(len(my_list))
my_list = [35, 24, 62, 52, 30, 30, 17]
print(my_list)
print(len(my_list))

my_other_list = [35, 1.77, "Brais", "Moure"]
print(type(my_list))
print(type(my_other_list))

# Acceso a elementos y búsqueda

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1]) # toma el último elemento
print(my_other_list[-4]) # cuenta desde el final empezando el último en -1, luego -2, -3 hasta llegar a -4
print(my_list.count(30)) # método count para contar cuántas veces se repite un valor en el array

# va a dar error porque los índices no existen
# print(my_other_list[4]) IndexError
# print(my_other_list[-5]) IndexError

# Buscando el índice de un elemento por su valor
print(my_other_list.index("Brais")) # retorna la posición

# list unpacking
age, height, name, surname = my_other_list
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)

# list unpacking again, con Andrei
a,b,c, *other,d  = [1,2,3,4,5,6,7,8,9]
print(a) # 1
print(b) # 2
print(c) # 3
print(other) # [4,5,6,7,8]
print(d) # 9

# Concatenación de listas
print(my_list + my_other_list)
#print(my_list - my_other_list)

# Creación, inserción, actualización y eliminación

# append agrega al final
my_other_list.append("MoureDev")
print(my_other_list)

# insert usa dos parámetros, el primero indica el indice 
# donde se agrega, el segundo el elemento a agregar
my_other_list.insert(1, "Rojo")
print(my_other_list)

# indicando la posición del elemento
my_other_list[1] = "Azul"
print(my_other_list)

# eliminando un elemento por su valor
my_other_list.remove("Azul")
print(my_other_list)

my_list.remove(30)
print(my_list)

# eliminando el último elemento. Retorna el elemento borrado
print(my_list.pop())
print(my_list)

# eliminando un elemento por su posición. Retorna el elemento borrado
my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

# eliminando un elemento por su posición, de otra manera
del my_list[2]
print(my_list)

# Operaciones con listas

# copia una lista y la retorna. Útil para guardarla en una variable
my_new_list = my_list.copy()

# elimina todos los elementos de una lista
my_list.clear()

print(my_list)
print(my_new_list)

# invierte todos los elementos de la lista, del final al principio
my_new_list.reverse()
print(my_new_list)

# ordena todos los elementos de la lista
my_new_list.sort()
print(my_new_list)

# Sublistas. Slicing
print(my_new_list[1:3])

# Andrei Neagoie
basket = [1,2,3,4,5]
# adding con extend, no retorna una nueva lista, modifica la original
basket.extend([100, 101]) # basket = [1,2,3,4,5,100,101]

# Cambio de tipo
my_list = "Hola Python"
print(my_list)
print(type(my_list))

# UNSAM
# test de pertenencia (in, not in)
frutas = ['manzanas', 'peras', 'bananas', 'naranjas']
'melon' in frutas # False
'melon' not in frutas # True
'peras' in frutas # False

# usando in
basket = ['a','b','c','c','c','d','e']
print('d' in basket) # True

# usando el método count
print(basket.count('c')) # 3

# copiando una lista de una forma muy útil
other_basket = basket[:]
print(other_basket)

# método sorted, retorna una nueva lista, no modifica la original
basket = ['a', 'x', 'b', 'c', 'd', 'e', 'd']
print(sorted(basket))
print(basket) # esta lista no fue modificada

# más sobre slicing, que es muy útil
# [inicio, fin, valor en el que avanza]
string = 'Hellooo' # se puede usar para strings que son cadenas de caracteres
print(string[0:2:1]) # he

# string[0] = 'z' da error, porque los strings son inmutables

# se puede usar para listas
# las listas son mutables
amazon_cart = ['notebook', 'sunglasses', 'toys', 'grapes']
amazon_cart[0] = 'laptop'

print(amazon_cart[0:2]) # ['laptop', 'sunglasses']
# [0::2] desde la posición 0 hasta el final, tomando de a dos
print(amazon_cart[0::2]) # ['laptop', 'toys']

# ojo estos dos apuntan al mismo lugar en memoria
# para no modificar uno y alterar el otro, hay que hacer una copia

# new_cart = amazon_cart 

new_cart = amazon_cart[:]
new_cart[0] = 'gum'
print(new_cart) # ['gum', 'sunglasses', 'toys', 'grapes']
print(amazon_cart) # ['laptop', 'sunglasses', 'toys', 'grapes']

basket = ['a', 'x', 'b', 'c', 'd', 'e', 'd']
basket.sort() # la ordena
basket.reverse() # invierte de final al princpio
# [::-1] invierte de final al principio, deshaciendo los cambios del reverse, 
# pero sin modificar la lista original
print(basket[::-1]) 

# llenando una lista con range
print(list(range(101))) # desde el 0 al 100 (hay 101 números)
print(list(range(1,100))) # desde el 1 al 99 (hay 99 números, 100-1)

# método join
sentence = ' '
new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'Nahuel'])
print(new_sentence)

# matrix bidimensional
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix[0][1]) # 2
print(matrix[1][2]) # 6

