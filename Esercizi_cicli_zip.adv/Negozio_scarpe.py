# Un negozio di scarpe ha un catalogo di modelli, ciascuno disponibile in una certa taglia e con un prezzo. 
# Le tre informazioni sono memorizzate in tre liste parallele. 
# Devi costruire visualizzazioni e filtri del catalogo usando zip.

modelli  = ["Runner X", "Urban Step", "Trail Boost", "Classic Fit", "SlimWalk", "AirFlex"]
taglie   = [42, 38, 44, 40, 37, 43]
prezzi   = [89.90, 74.50, 112.00, 65.00, 58.00, 97.50]

# Fase 1. Visualizzazione del catalogo

def stampa_catalogo(modelli,taglie,prezzi): 
    print("---- CATALOGO ----")
    for modello, taglia, prezzo in zip(modelli, taglie, prezzi):
        print (f"{modello} | {taglia} | {prezzo}")

def catalogo_ordinato(modelli, taglie, prezzi):
    print ("---- CATALOGO ORDINATO ----")
    lista_triple = []
    for modello, taglia, prezzo in zip(modelli, taglie, prezzi):
        lista_triple.append([modello, taglia, prezzo])
    lista_ordinata = sorted(lista_triple, key = lambda x: x[2])
    for i, value in enumerate(lista_ordinata, 1):
        print (f"{i}. {value}")


# Fase 2. Filtri con condizioni

def scarpe_sotto_soglia(modelli, prezzi):
    lista_modelli = []
    for modello, prezzo in zip(modelli, prezzi):
        if prezzo < 80:
            lista_modelli.append(modello)
    numero_modelli = len(lista_modelli)
    print(f"I modelli sotto soglia sono {numero_modelli}: {lista_modelli} ")

def ricerca_taglia(modelli, taglie, prezzi, taglia_cercata):
    modelli_disponibili = []
    for modello, taglia in zip(modelli, taglie):
        if taglia == taglia_cercata:
            modelli_disponibili.append(modello)
    if not modelli_disponibili:
        print(f"Nessun modello disponibile con la taglia {taglia_cercata}")
    return modelli_disponibili


# Fase 3. Aggiornamento listino

sconti = [10, 5, 15, 20, 10, 0]  # percentuali di sconto

def applica_sconto(prezzi, sconti):
    prezzi_scontati = []
    for prezzo, sconto in zip(prezzi, sconti):
        prezzo_scontato = prezzo - (prezzo * (sconto/100))
        prezzi_scontati.append(prezzo_scontato)
    return prezzi_scontati

def stampa_sconti(modelli, prezzi, prezzi_scontati):
    print("---- NUOVO LISTINO SCONTATO ----")
    for modello, prezzo, prezzo_scontato in zip(modelli, prezzi, prezzi_scontati):
        print(f"{modello} | {prezzo} → {prezzo_scontato}")


