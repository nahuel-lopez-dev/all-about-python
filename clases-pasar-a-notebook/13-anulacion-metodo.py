# method override o anulación de método
# tomamos un método heredado y lo cambiamos por otro para 
# cambiar su funcionalidad

class Ave:
    def __init__(self):
        self.volador = "volador"
    
    def vuela(self):
        print("vuela ave")
        
    
class Pato(Ave):
    def __init__(self):
        super().__init__() # ejecutando el constructor de la clase padre
        self.nada = "nadador"
    
    def vuela(self): # method override
        print("vuela pato")
        # super().vuela() # ejecuta el método del padre
    
pato = Pato()
pato.vuela()
print(pato.volador, pato.nada)





