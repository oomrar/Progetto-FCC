# Programmazione ad oggetti: COMPOSIZIONE.
# Un e-commerce ha prodotti con nome, prezzo e disponibilità.
# Il carrello raccoglie i prodotti selezionati dall'utente, tiene traccia delle quantità e calcola i totali. 
# Queste due entità sono modellate come classi separate che collaborano.

print()

class Prodotto:

    def __init__(self, nome, prezzo, disponibilita):
        self.nome = nome
        self.prezzo = prezzo
        self.disponibilita = disponibilita

    def is_disponibile(self):
        return self.disponibilita > 0
        
    def descrizione(self):
        print("Descrizione prodotto:")
        print(f"{self.nome} | {self.prezzo} | Disponibilità: {self.disponibilita}")
        print()
        

class Carrello:

    def __init__(self, utente):
        self.utente = utente
        self.articoli = []

    def aggiungi(self, prodotto, quantita = 1):
        if prodotto.disponibilita == 0:
            print(f"Prodotto '{prodotto.nome}' non disponibile")
            return
        if prodotto.disponibilita < quantita:
            print(f"Prodotto '{prodotto.nome}' non disponibile")
            return
        else:
            for item in self.articoli:
                if item[0] is prodotto:
                        item[1] += quantita
                        break
            else:
                self.articoli.append([prodotto, quantita])
            
            

    def totale(self):
        somma = 0
        for prodotto, quantita in self.articoli:
            somma += prodotto.prezzo * quantita
        return somma


    def rimuovi(self, prodotto):
        for item in self.articoli:
            if item[0] is prodotto:
                self.articoli.remove(item)
                return

    def checkout(self):
        print("RIEPILOGO ORDINE")
        print()
        for prodotto, quantita in self.articoli:
            subtotale = round(prodotto.prezzo * quantita, 2)
            print(f"Prodotto: {prodotto.nome} | Quantità: {quantita} | Subtotale: {subtotale}")
            totale_finale = self.totale()
        print()
        print(f"Totale finale: {round(totale_finale, 2)}")
        print()
        self.articoli = []



p1 = Prodotto("Cuffie Wireless", 89.99, 10)
p2 = Prodotto("Mouse Gaming", 45.00, 10)
p3 = Prodotto("Tastiera Meccanica", 120.00, 4) 
p4 = Prodotto("Tappetino RGB", 25.50, 3)

mio_carrello = Carrello("Omar")


mio_carrello.aggiungi(p1, 2)  # Aggiunge 2 unità di p1
mio_carrello.aggiungi(p2, 1)  # Aggiunge 1 unità di p2
mio_carrello.aggiungi(p4, 1)  # Aggiunge 1 unità di p4

# 3. Modifica quantità
# Aggiungendo di nuovo lo stesso prodotto, il metodo deve aggiornare la quantità esistente
mio_carrello.aggiungi(p1, 1)  # Porta la quantità di p1 da 2 a 3

# 4. Rimuovi uno
# Rimuove la riga corrispondente a un prodotto (ad esempio p4)
mio_carrello.rimuovi(p4)

# 5. Chiama il checkout
# Stampa il riepilogo con i subtotali, il totale finale e svuota il carrello
mio_carrello.checkout()