# Crea una classe GestoreMagazzino che gestisca un magazzino di prodotti. La classe dovrà avere i seguenti attributi:
# Un dizionario “prodotti” che mappa i nomi dei prodotti ai rispettivi oggetti “Prodotto” (che descriverai in seguito)
# Una variabile “costo_magazzinaggio” che indica il costo per magazzinare ogni prodotto per un mese
# La classe dovrà avere i seguenti metodi:
# Un metodo “aggiungi_prodotto” che aggiunga un nuovo prodotto al magazzino
# Un metodo “rimuovi_prodotto” che rimuova un prodotto dal magazzino
# Un metodo “calcola_costi_magazzinaggio” che calcoli i costi di magazzinaggio per tutti i prodotti presenti nel magazzino
# Crea inoltre una classe Prodotto che abbia gli attributi “nome”, “prezzo” e “scorta”.

class Prodotto:
        def __init__(self, nome, prezzo, scorte):
            self.nome = nome
            self.prezzo = prezzo
            self.scorte = scorte

class GestoreMagazzino:
    def __init__(self, costo_magazzinaggio):
        self.prodotti = {}
        self.costo_magazzinaggio = costo_magazzinaggio

    def aggiungi_prodotto(self, prodotto):
        self.prodotti[prodotto.nome] = prodotto

    def rimuovi_prodotto(self, prodotto_da_rim):
        self.prodotti.pop(prodotto_da_rim)

    def calcola_costi_magazzinaggio(self):
        costi = 0
        for prodotto in self.prodotti.values():
            costi += prodotto.scorte * self.costo_magazzinaggio
        return costi
    
    
prodotto1 = Prodotto("Telefono", 500, 10)
prodotto2 = Prodotto("Computer", 50, 100)

gest = GestoreMagazzino(10)

gest.aggiungi_prodotto(prodotto1)
gest.aggiungi_prodotto(prodotto2)

print(gest.calcola_costi_magazzinaggio())