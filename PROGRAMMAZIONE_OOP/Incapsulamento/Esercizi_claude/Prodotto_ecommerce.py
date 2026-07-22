# Un prodotto di un negozio online ha prezzo netto, aliquota IVA e quantità in stock. 
# Il prezzo con IVA è una property calcolata. 
# La quantità non può essere negativa. Se scende sotto la soglia di riordino, il prodotto entra in stato di "scorta bassa". 
# Il codice prodotto è immutabile dopo la creazione.

print()

class Prodotto:

    def __init__(self, codice, nome, prezzo_netto, iva_pct=22, stock = 0, soglia =10):
        self._codice = codice
        self.nome = nome
        self.prezzo_netto = prezzo_netto
        self.iva_pct = iva_pct
        self.stock = stock
        self._soglia = soglia

    @property
    def codice(self):
        return self._codice
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, new_nome):
        if not new_nome:
            raise ValueError("Il nome non può essere una stringa vuota")
        self._nome = new_nome

    @property
    def prezzo_netto(self):
        return self._prezzo_netto
    
    @prezzo_netto.setter
    def prezzo_netto(self, new_prezzo):
        if new_prezzo <= 1:
            raise ValueError("Il prezzo deve essere maggiore di 0")
        self._prezzo_netto = new_prezzo

    @property
    def stock(self):
        return self._stock
    
    @stock.setter
    def stock(self, new_stock):
        if new_stock < 0:
            raise ValueError("Lo stock non può essere negativo")
        self._stock = new_stock

    @property
    def iva_pct(self):
        return self._iva_pct
    
    @iva_pct.setter
    def iva_pct(self, new_iva):
        if 0 <= new_iva <= 100:
            self._iva_pct = new_iva
        else:
            raise ValueError("L'IVA dev'essere compresa fra 0 e 100")
        
    @property
    def prezzo_ivato(self):
        return f" {round(self._prezzo_netto * (1 + self._iva_pct / 100), 3)} €"

    @property
    def valore_magazzino(self):
        return self.prezzo_netto * self.stock

    @property
    def scorta_bassa(self):
        return self.stock < self._soglia
    
    def vendi(self, quantita):
        if quantita <= self.stock:
            self.stock = self.stock - quantita
        else:
            print("Quantità richiesta non disponibile")

    def rifornisci(self, quantita):
        self.stock = self.stock + quantita

    def scheda(self):
        print("RIEPILOGO PRODOTTO ECOMMERCE")
        print("-"*20)
        print(f"Nome prodotto: {self.nome}")
        print(f"Prezzo: {self.prezzo_netto}")
        print(f"Quantità: {self.stock}")
        print(f"Iva: {self.iva_pct}")
        print("-"*20)
        print(f"Valore magazzino: {self.valore_magazzino}")
        print(f"Scorta bassa? {self.scorta_bassa}")
        print(f"Prezzo del prodotto ivato: {self.prezzo_ivato}")
        print("-"*20)
        print("-"*20)
        print("Vendita di alcuni prodotti")
        self.vendi(4)
        print(f"Valore magazzino aggiornato: {self.valore_magazzino}")
        print(f"Scorta bassa? {self.scorta_bassa}")
        print("-"*20)
        print("-"*20)
        print("Rifornimento")
        self.rifornisci(67)
        print(f"Valore magazzino aggiornato: {self.valore_magazzino}")
        print(f"Scorta bassa? {self.scorta_bassa}")

    










# Test

prod1 = Prodotto(124556, "Computer", 450, 22, 23)
print(prod1.prezzo_ivato)
prod1._prezzo_netto = 460
print(prod1.prezzo_ivato)
print(prod1.valore_magazzino)
print(prod1.scorta_bassa)
prod1.stock = 9
print(prod1.scorta_bassa)
print()
print("Stampa della scheda")
prod1.scheda()




print()