# Un mazzo di carte francesi ha 52 carte: 4 semi × 13 valori. 
# Il mazzo deve poter essere mescolato, distribuire carte ai giocatori e tenere traccia di quante carte rimangono. 
# Questo esercizio mette insieme composizione, costruzione automatica in __init__ e logica di gioco.

import random

class Carta:

    def __init__(self, seme, valore):
        self.seme = seme
        self.valore = valore

    def mostra(self):
        print(f"{self.valore} {self.seme}")

    def valore_numerico(self):
        valore_numerico = 0
        if self.valore == "J" or self.valore == "Q" or self.valore == "K":
            valore_numerico = 10
        elif self.valore == "A":
            valore_numerico = 11
        else:
            if self.valore:
                valore_numerico = self.valore
        return valore_numerico
    


semi   = ["♠ Picche", "♥ Cuori", "♦ Quadri", "♣ Fiori"]
valori = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]

cart1 = Carta("♠ Picche", "4")
cart2 = Carta("♠ Picche", "A")
cart3 = Carta("♠ Picche", "Q")


cart1.mostra()
print(cart1.valore_numerico())
print(cart2.valore_numerico())
print(cart3.valore_numerico())


class Mazzo:

    def __init__(self):
        self.carte = []
        for seme in semi:
            for valore in valori:
                self.carte.append(Carta(seme, valore))
        
    
    def mischia(self):
        return random.shuffle(self.carte)

    def carte_rimanenti(self):
        return len(self.carte)
    
    def pesca(self):
        return self.carte.pop()
    
    def distribuisci(self, n_giocatori, carte_per_giocatore):
        totale_richiesto = n_giocatori * carte_per_giocatore
        if totale_richiesto > self.carte_rimanenti():
            print("Attenzione: Non ci sono abbastanza carte nel mazzo per tutti!")
        
        grandi_mani = [] 
        
        for i in range(n_giocatori):
            mano_giocatore = []
            for _ in range(carte_per_giocatore):
                carta_pescata = self.pesca()
                if carta_pescata:
                    mano_giocatore.append(carta_pescata)
            grandi_mani.append(mano_giocatore)
            
        return grandi_mani
    
    def reset(self):
        self.carte = []
        for seme in semi:
            for valore in valori:
                self.carte.append(Carta(seme, valore))
        return self.carte



mazzo_gioco = Mazzo()
mazzo_gioco.mischia()


mani_giocatori = mazzo_gioco.distribuisci(3, 5)


for i, mano in enumerate(mani_giocatori):
    print(f"\n--- MANO GIOCATORE {i+1} ---")
    for carta in mano:
        carta.mostra() 

print(f"\nCarte rimaste nel mazzo: {mazzo_gioco.carte_rimanenti()}")   
    
    