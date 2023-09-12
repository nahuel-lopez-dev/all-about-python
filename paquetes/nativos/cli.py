import os
from pathlib import Path
import sys

print(sys.argv)
# en la terminal
# python paquetes/nativos/cli.py
# python paquetes/nativos/cli.py -a holamundo

def cli(args):
    if len(args) == 1:
        print("no se pasaron argumentos")
        return
    
    if len(args) != 3:
        print("se necesitan 2 argumentos")
        return
    
    origen = args[1]
    o = Path(origen)
    if not o.exists():
        print("Origen no existe")    
    
    destino = args[2]
    d = Path(destino)
    if d.exists():
        print("El destino no puede existir")
        return    
        
    os.rename(str(origen), str(destino))    
    print("Archivo renombrado con exito")

cli(sys.argv)

# probando el programa
# crear un archivo cualquiera: lala
# En la terminal:
# python paquetes/nativos/cli.py paquetes/nativos/lala paquetes/nativos/lala-destino.md

