class Coordenadas:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
    # método para comparar objetos, equal  
    def __eq__(self, otro):
        return self.lat == otro.lat and self.lon == otro.lon
    # este método not equal, de alguna forma está contemplado con __eq__
    def __ne__(self, otro):
        return self.lat != otro.lat or self.lon != otro.lon
    # método less than
    def __lt__(self, otro):
        return self.lat + self.lon < otro.lat + otro.lon
    # less or equal
    def __le__(self, otro):
        return self.lat + self.lon <= otro.lat + otro.lon
            

coords = Coordenadas(42, 27)
coords2 = Coordenadas(45, 27)

print(coords, coords2) # están guardadas en distintos lugares de la memoria RAM
print(coords == coords2) # True por el método __eq__ sino sería False
print(coords != coords2) # False porque los objetos son iguales

print(coords > coords2)
print(coords <= coords2)

        
        
        