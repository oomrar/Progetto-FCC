# Modella un conto bancario con operazioni di deposito e prelievo. 
# Il conto deve impedire prelievi che portino il saldo in negativo e non accettare importi non positivi. 
# Ogni operazione deve essere tracciata.

class ContoBancario:
    def __init__(self, intestatario, saldo = 0.0):
        self.intestatario = intestatario
        self.saldo = saldo
        self.storico = []
    
    def estratto_conto(self):
        print(f"Intestatario conto: {self.intestatario}")
        print(f"Saldo attuale: {self.saldo}")
        print(f"Lista operazioni: {self.storico}")

    def deposita(self, importo):
        if importo <= 0:
            print("ERRORE! Impossibile depositare importi negativi.")
        else:
            self.saldo += importo
            self.storico.append(f"+ €{importo}")

    def preleva(self, importo):
        if importo <= 0:
            print("ERRORE! Impossibile prelevare importi negativi.")
        else:
            if self.saldo - importo < 0:
                print("ERRORE! Fondi insufficienti.")
            else:
                self.saldo -= importo
                self.storico.append(f"- €{importo}")


# Dati di test da usare per verificare la classe una volta scritta:
conto1 = ContoBancario("Alice Rossi", 500.0)
conto2 = ContoBancario("Bruno Verdi")   # saldo iniziale di default = 0

conto1.deposita(200)
conto1.preleva(100)
conto1.preleva(1000)
conto1.deposita(-50)
conto1.preleva(300)

print()
conto1.estratto_conto()

print()
conto2.deposita(150)
conto2.preleva(80)
conto2.estratto_conto()