# Un magazzino deve poter essere interrogato per indice numerico (il primo prodotto, l'ultimo) e deve valutarsi come False in un if quando è vuoto. 
# Questo lo rende utilizzabile con la sintassi naturale di Python.

print()

class Magazzino:

    def __init__(self, nome):
        self.nome = nome
        self.prodotti = []

    def carica(self, nome, quantita, prezzo):
        self.prodotti.append([nome, quantita, prezzo])

    def __len__(self):
        return len(self.prodotti)
    
    def __str__(self):
        frase = f"Nome magazzino: {self.nome}\n"
        for i, prod in enumerate(self.prodotti, 1):
            nome = prod[0]
            quantita = prod[1]
            prezzo = prod[2]
            frase += f"{i}. {nome} | Quantità: {quantita} | Prezzo: € {prezzo}\n"
        return frase
    
    def __getitem__(self, indice):
        return self.prodotti[indice]
    
    def __contains__(self, nome_prodotto):
        for p in self.prodotti:
            if p[0] == nome_prodotto:
                return True
        return False
    
    def __bool__(self):
        condizione = len(self.prodotti) > 0
        return condizione
    
    def svuota(self):
        self.prodotti.clear()

    


# Test fase 1.
magazzino = Magazzino("MIO STOCK")
magazzino.carica("Caffe", 5, "6,80")
magazzino.carica("Sale", 10, "3,50")
magazzino.carica("Pepe", 3, "5,50")

print(magazzino)


# Test fase 2.
print(magazzino[0])
print("Caffe" in magazzino)
print()

# Test fase 3.
if magazzino:
    print("Ha prodotti")
else:
    print("Magazzino vuoto")
magazzino.svuota()
if magazzino:
    print("Ha prodotti")
else:
    print("Magazzino vuoto")