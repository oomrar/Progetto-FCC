# Modella un'automobile che può guidare, rifornirsi e mostrare il suo stato. 
# Il carburante si consuma guidando (0.08 litri/km) e non può scendere sotto zero. 
# L'odometro registra i km totali percorsi e non può mai decrementare.

print()

class Automobile:

    def __init__(self, marca, modello, anno, carburante=40.0):
        self.marca = marca
        self.modello = modello
        self.anno = anno
        self.carburante = carburante
        self.km_totali = 0
        self.accesa = False

    def accendi(self):
        self.accesa = True
        print("Auto accesa")
        print()

    def spegni(self):
        self.accesa = False
        print("Auto spenta")
        print()

    def stato(self):
        print("="*50)
        stato_veicolo = ""
        print("STATO VEICOLO")
        print()
        print(f"Marca: {self.marca}")
        print(f"Modello: {self.modello}")
        print(f"Anno: {self.anno}")
        print(f"Carburante: {self.carburante}")
        if self.accesa == True:
            stato_veicolo = "Accesa"
        else:
            stato_veicolo = "Spenta"
        print(f"Stato veicolo: {stato_veicolo}")

    def guida(self, km):
        print("="*50)
        print("RIEPILOGO VIAGGIO")
        print()
        if not self.accesa:
            print("Per guidare prima devi accendere il veicolo")
            print()
            return
        if km <= 0:
            print("Impossibile guidare per 0 km")
            return
        if (km * 0.08) > self.carburante:            
            print(f"{km} son troppi per il carburante, rifornire!")
            return
        self.carburante -= 0.08 * km
        self.km_totali += km
        print()
        print(f"Chilometri da percorrere: {km}")
        print(f"Carburante rimasto: {self.carburante}")
        print(f"Chilometri totali: {self.km_totali}")
        print()

    def rifornisci(self, litri):
        print("="*50)
        print()
        if litri <= 0:
            print("Impossibile rifornire importi negativi")
            return
        if (self.carburante + litri) <= 60:
            self.carburante += litri
            print(f"Riforniti {litri} litri!")
        else:
            litri_effettivi = 60 - self.carburante
            self.carburante = 60.0
            print(f"Capienza superata! Sono stati inseriti solo {litri_effettivi:.2f} litri per fare il pieno.")
        print()
            

    
auto1 = Automobile("Fiat", "Panda", anno=2020, carburante = 40.0)




# Test

auto1.accendi()
auto1.guida(100)
auto1.guida(200)
auto1.guida(1000)
print()
auto1.rifornisci(30)
auto1.guida(300)
auto1.spegni()

auto1.guida(100)
auto1.rifornisci(100)
auto1.accendi()
auto1.guida(0)



print()