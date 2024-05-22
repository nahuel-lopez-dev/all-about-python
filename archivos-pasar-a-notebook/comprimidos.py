from pathlib import Path
from zipfile import ZipFile

# para comprimir archivos
with ZipFile("archivos/comprimidos.zip", "w") as zip:
    # el primer * es para cualquier nombre de archivo
    # el segundo * es para indicar cualquier extensión
    # cualquier archivo que tenga cualquier nombre y cualquier extensión: "*.*"
    for path in Path().rglob("*.*"):
         print(path)
         if str(path) != "archivos/comprimidos.zip":
             zip.write(path)
         

# para leer de archivos comprimidos
with ZipFile("archivos/comprimidos.zip") as zip:
    # print(zip.namelist())
    info = zip.getinfo("archivos/comprimidos.py")  
    print(
        info.file_size,
        info.compress_size
    )   
    zip.extractall("archivos/descomprimidos")



