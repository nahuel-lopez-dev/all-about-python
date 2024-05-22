from io import open

##### escritura, si no existe lo crea

texto = "Hola mundo"
archivo = open("archivos/hola-mundo.txt", "w")
archivo.write(texto)
archivo.close()


##### lectura

# archivo = open("archivos/hola-mundo.txt", "r")
# texto = archivo.read()
# archivo.close()
# print(texto)

##### lectura como lista
# archivo = open("archivos/hola-mundo.txt", "r")
# texto = archivo.readlines()
# archivo.close()
# print(texto)

##### with y seek
# with open("archivos/hola-mundo.txt", "r") as archivo:
    ##### cargar todo el archivo
    # print(archivo.readlines())
    ##### carga línea por línea
    # archivo.seek(0)
    # for linea in archivo:
    #     print(linea)


##### agregar
# archivo = open("archivos/hola-mundo.txt", "a+")
# archivo.write("Chao mundo")
# archivo.close()

##### lectura y escritura
# with open("archivos/hola-mundo.txt", "r+") as archivo:
#     texto = archivo.readlines()
#     archivo.seek(0)
#     texto[0] = "Chanchito feliz"
#     archivo.writelines(texto)
    
    





