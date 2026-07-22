# Un serbatoio di carburante ha una capacità massima fissa (non modificabile dopo la creazione) e un livello corrente.
# Il livello non può mai essere negativo né superare la capacità. 
# Aggiungiamo anche una soglia di riserva: quando il livello scende sotto il 15% della capacità, il serbatoio segnala un avviso.

print()

class Serbatoio:

    def __init__(self, capacita_max, livello_iniziale):
        self._capacita = capacita_max
        self.livello = livello_iniziale

    @property
    def livello(self):
        return self._livello
    
    @livello.setter
    def livello(self, new_livello):
        if new_livello < 0 or new_livello > self._capacita:
            raise ValueError("Livello non valido")
        self._livello = new_livello

    @property
    def percentuale(self):
        return (self._livello/self._capacita * 100)

    @property
    def in_riserva(self):
        return self.percentuale < 15

    @property
    def spazio_disponibile(self):
        return self._capacita - self.livello
    
    def rifornisci(self, litri): 
        if litri <= 0:
            raise ValueError("I litri da rifornire devono essere positivi")
        if litri > self.spazio_disponibile:
            self.livello = self._capacita
            return
        self.livello = self.livello + litri

    def consuma(self, litri):
        if litri <= 0:
            raise ValueError("I litri da consumare devono essere positivi")
        if litri > self._livello:
            self.livello = 0
            return
        self.livello = self.livello - litri
    
    def stato(self):
        print("SERBATOIO AUTO")
        print("=" * 50)
        print(f"Livello attuale: {self.livello}")
        print(f"Capacità serbatoio: {self._capacita}")
        print(f"Percentuale serbatoio: {self.percentuale}")
        if self.in_riserva:
            print("ATTENZIONE! Veicolo in riserva")

s = Serbatoio(capacita_max=60.0, livello_iniziale=45.0)
s.stato()
print()