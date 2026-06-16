# Una frazione matematica ha numeratore e denominatore. 
# Al momento della creazione deve essere automaticamente semplificata (3/6 diventa 1/2). 
# I d((under permettono di sommare frazioni, confrontarle e stamparle con la sintassi degli operatori.

print()

import math

class Frazione:

    def __init__(self, numeratore, denominatore):
        if denominatore == 0:
            raise ValueError("Impossibile dividere per 0")
        mcd = math.gcd(numeratore, denominatore)
        self.numeratore = numeratore // mcd
        self.denominatore = denominatore // mcd

    def __str__(self):
        return f"({self.numeratore}/{self.denominatore})"
    
    def __eq__(self, altro):
        return self.numeratore == altro.numeratore and self.denominatore == altro.denominatore

    def __lt__(self, altro):
        return self.numeratore * altro.denominatore < altro.numeratore * self.denominatore

    def __gt__(self, altro):
        return self.numeratore * altro.denominatore > altro.numeratore * self.denominatore

    def __add__(self, altro):
        num = self.numeratore * altro.denominatore + altro.numeratore * self.denominatore
        den = self.denominatore * altro.denominatore
        return Frazione(num, den)


# Test

f1 = Frazione (10,5)
f2 = Frazione (20,5)
f3 = Frazione (15,6)

print("VISUALIZZATORE FRAZIONI SEMPLIFICATE:")
print(f1)
print(f2)
print()
print("VISUALIZZATORE ORDINATORI:")
print(f1>f2)
print(f1<f2)
lista_disordinata = [f1, f2, f3]
lista_ordinata = sorted(lista_disordinata)
print()
print("FRAZIONI ORDINATE:")
for f in lista_ordinata:
    print(f)
print()

# Test somme
print("TEST SOMME:")
print(Frazione(1,2) + Frazione(1,3)) 
print(Frazione(1,4) + Frazione(3,4))

print()
    