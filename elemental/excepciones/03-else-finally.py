try:
    n1 = int(input("Ingresa primer número:"))
except Exception as e:
    print("Ocurrió un error!")
else:
    print("No ocurrió ningún error")
finally:
    print("Se ejecuta siempre")




