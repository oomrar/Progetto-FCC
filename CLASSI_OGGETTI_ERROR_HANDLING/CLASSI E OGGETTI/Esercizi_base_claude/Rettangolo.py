# Modella un rettangolo geometrico. 
# I metodi devono calcolare proprietà geometriche, confrontare figure tra loro e produrre trasformazioni.
#  Questo esercizio consolida l'uso di return nei metodi e introduce l'idea di un metodo che riceve un'altra istanza come argomento.

print()

class Rettangolo:

    def __init__(self, larghezza, altezza):
        self.larghezza = larghezza
        self.altezza = altezza

    def area(self):
        return self.larghezza * self.altezza
    
    def perimetro(self):
        return (self.larghezza + self.altezza) * 2
    
    def is_quadrato(self):
        if self.larghezza == self.altezza:
            return True
        else:
            return False

    def scala(self, fattore):
        return Rettangolo(self.larghezza * fattore, self.altezza * fattore)

    def ruota(self):
        return Rettangolo(self.altezza, self.larghezza)
    
    def confronta(self, altro):
        area_self = self.area()
        area_altro = altro.area()
        if area_self > area_altro:
            print(f"Il rettangolo ({self.larghezza}*{self.altezza}) ha un area maggiore ({area_self}) rispetto al rettangolo ({altro.larghezza}*{altro.altezza}) con area {area_altro}.")
        elif area_altro > area_self:
            print(f"Il rettangolo scalato ({altro.larghezza}*{altro.altezza}) ha un area maggiore ({area_altro}) rispetto al rettangolo non scalato ({self.larghezza}*{self.altezza}) con area {area_self}.")
        else:
            print("Entrambi i rettangoli hanno la stessa area")
        
    def contiene(self, altro):
        condizione_larghezza = self.larghezza > altro.larghezza
        condizione_altezza = self.altezza > altro.altezza
        return condizione_larghezza and condizione_altezza


rettangolo_stretto = Rettangolo(3,7)
rettangolo_largo = Rettangolo(10,3)
quadrato = Rettangolo(5,5)

print("Figura 1")
print(rettangolo_stretto.area())
print(rettangolo_stretto.perimetro())
print()

print("Figura 2")
print(rettangolo_largo.area())
print(rettangolo_largo.perimetro())
print()

print("Figura 3")
print(quadrato.area())
print(quadrato.perimetro())
print()

print(quadrato.is_quadrato())
print(rettangolo_largo.is_quadrato())
print()

rettangolo_largo_mod = rettangolo_largo.scala(10)
print("Figura 1 scalata")
print(rettangolo_largo_mod.area())
print(rettangolo_largo_mod.perimetro())
print()

rettangolo_largo.confronta(rettangolo_largo_mod)
print()

print(f"Il rettangolo largo contiene il quadrato? {rettangolo_largo.contiene(quadrato)}")
print(f"Il rettangolo largo scalato contiene il quadrato? {rettangolo_largo_mod.contiene(quadrato)}")
print()


