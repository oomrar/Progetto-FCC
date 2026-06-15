# Un vettore matematico nel piano 2D ha componenti x e y. 
# Implementando i metodi dunder, i vettori potranno essere stampati, sommati, sottratti e moltiplicati per uno scalare con la sintassi naturale degli operatori Python.

print()

class Vettore:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Vettore({self.x}, {self.y})"
    
    def __add__(self, altro):
        return Vettore(x = self.x + altro.x, y = self.y + altro.y)

    def __sub__(self, altro):
        return Vettore(x = self.x - altro.x, y = self.y - altro.y)
    
    def __mul__(self, scalare):
        return Vettore(x = self.x * scalare, y = self.y * scalare)
    

    def __eq__(self, altro):
        return self.x == altro.x and self.y == altro.y

    def modulo(self):
        return round((self.x**2 + self.y**2)**0.5, 2)

    def normalizza(self):
        m = self.modulo()
        return Vettore(self.x/m, self.y/m)

# Test fase 1.
v = Vettore(10, 27)
print(v)
print(repr(v))
print()

# Test fase 2.
v1 = Vettore(10, 6)
v2 = Vettore(5, 4)
v3 = v1 + v2
print(v3)
print()
print(v1 +v2 -v3)
print()

# Test fase 3.
print(repr(v1 * 3))
print(v1==v2)
print(f"Test del modulo: {v1.modulo()}")
print(f"Test normalizzazione: {v2.normalizza()}")
print()
