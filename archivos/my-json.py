import json
from pathlib import Path

# JSON
# JavaScript Object Notation
# Este es el formato más común por el cual las APIs, sobre todo
# las APIs REST, comparten o brindan información cuando se las
# consume. "Te envían un JSON".

# escribir json
# productos = [
#     {"id":1, "name": "Surfboard"},
#     {"id":2, "name": "Bicicleta"},
#     {"id":3, "name": "Skate"},
# ]

# data = json.dumps(productos)
# print(data)

# Path("archivos/productos.json").write_text(data)

# leer json
data = Path("archivos/productos.json").read_text(encoding="utf-8")
productos = json.loads(data)
print(productos)

# modificar json
productos[0]["name"] = "Medialunas"
Path("archivos/productos.json").write_text(json.dumps(productos))
print(productos)









