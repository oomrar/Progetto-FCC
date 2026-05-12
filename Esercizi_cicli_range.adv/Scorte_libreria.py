# Sei il responsabile informatico di una piccola libreria. Devi costruire un sistema base per analizzare le scorte di libri disponibili.

# Dati
titoli = ["Il Nome della Rosa", "1984", "Dune", "Neuromante", "Fondazione", "Fahrenheit 451", "Il Signore degli Anelli"]
copie =  [3, 0, 5, 2, 0, 1, 4]

# 1. Analizza magazzino

def analizza_magazzino (titoli, copie):
    for i in range(len(titoli)):
        print(f"{i+1} {titoli[i]} - {copie[i]}")

def conta_esauriti (copie):
    contatore = 0
    for i in range(len(copie)):
        if copie[i] == 0:
            contatore += 1
    return contatore

print("--- Situazione Iniziale ---")
analizza_magazzino(titoli, copie)
print(f"Libri esauriti: {conta_esauriti(copie)}")


# 2. Aggiornamento scorte

def rifornisci (titoli, copie, quantità):
    for i in range(len(titoli)):
        if copie[i] == 0:
            copie[i] += quantità
    return copie
copie = rifornisci(titoli, copie, 0)

def rimuovi_esauriti(titoli, copie):
    for i in range(len(titoli)-1, -1, -1):
        if copie[i] == 0:
            titoli.pop(i)
            copie.pop(i)
rimuovi_esauriti(titoli, copie)

# 3. Report finale

def report (titoli, copie):
    print(f"Totale dei libri: {len(titoli)}")
    totale_copie = 0
    for i in range(len(copie)):
        totale_copie += copie[i]
    indice_max = 0
    copie_max = 0
    for i in range(len(titoli)):
        if copie[i] > copie_max:
            copie_max = copie[i]
            indice_max = i
    print(f"Libro con più copie: {titoli[indice_max]}")

print("\n--- Report Finale ---")
report(titoli, copie)
    
