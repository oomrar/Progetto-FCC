# Gestisci l'inventario di un piccolo negozio di elettronica. 
# Devi processare ordini in entrata, aggiornare quantità, identificare prodotti esauriti e produrre report ordinati per criteri diversi.

prodotti  = ["Cuffie", "Tastiera", "Mouse", "Monitor", "Webcam", "Hub USB"]
quantita  = [5, 0, 12, 3, 0, 8]
prezzi    = [45.0, 29.0, 15.0, 189.0, 35.0, 22.0]

ordini_in_entrata = [
    ["Tastiera", 10],
    ["Webcam", 6],
    ["Monitor", 2],
    ["Salsa", 7]
]

# Fase 1. Stato magazzino

print(" ")
def stampa_inventario (prodotti, quantita, prezzi):
    for i, value in enumerate(prodotti, 1):
        frase = f"{i}. {value} | {quantita[i-1]} | {prezzi[i-1]}"
        if quantita[i-1] == 0:
            frase += " [ESAURITO]"
        print(frase)
print("---- SITUAZIONE INVENTARIO ----")
stampa_inventario(prodotti, quantita, prezzi)
print(" ")

def valore_totale_magazzino(quantita, prezzi):
    valore_totale = 0
    for i, value in enumerate(quantita):
        valore_totale += quantita [i] * prezzi [i]
    return round(valore_totale, 2)


print("---- VALORE TOTALE MAGAZZINO ----")
print(valore_totale_magazzino(quantita, prezzi))
print(" ")


# Fase 2. Elaborazione ordini.

def applica_ordini(prodotti, quantita, ordini_in_entrata):
    for ordini in ordini_in_entrata:
        nome, qty = ordini
        trovato = False
        for i, value in enumerate(prodotti):
            if nome == prodotti[i]:
                quantita [i]+= qty
                print(f"Aggiornamento eseguito: {nome} aggiunto.\nQuantità aggiornata: {quantita[i]}")
                trovato = True
                break
        if not trovato:    
            print(f"Prodotto {nome} non presente nell'inventario.")

print("---- ORDINI IN ENTRATA ----")
applica_ordini(prodotti, quantita, ordini_in_entrata)
print(" ")

def rimuovi_esauriti(prodotti, quantita, prezzi):
    indici = []
    for i, value in enumerate (prodotti):
        if quantita[i] == 0:
            indici.append(i)
    
    for i in range(len(indici)-1,-1,-1):
        bersaglio = indici[i]
        prodotti.pop(bersaglio)
        quantita.pop(bersaglio)
        prezzi.pop(bersaglio)
    return len(indici)

print("---- NUMERO PRODOTTI ESAURITI ----")
print(rimuovi_esauriti(prodotti, quantita, prezzi))
print(" ")


# Fase 3. Report e classifiche

def top3_per_valore (prodotti, quantita, prezzi):
    triple = []
    for i, value in enumerate(prodotti):
        valore_scorta = quantita [i] * prezzi [i]
        triple.append([value, quantita[i], valore_scorta])
    triple_ordinate = sorted(triple, key = lambda x: x[2], reverse = True)
    for i, (p,q,v) in enumerate(triple_ordinate[:3], 1):
        print(f"{i}. Prodotto: {p} | Quantità: {q} | Valore: {v}")

print("---- TOP 3 PRODOTTI PER VALORE ----")
top3_per_valore(prodotti, quantita, prezzi)
print(" ")


def report_completo():
    print("="*40)
    print("      GESTIONALE NEGOZIO ELETTRONICA")
    print("="*40)
    
    # Stato Iniziale
    print("\n1. SITUAZIONE INIZIALE:")
    stampa_inventario(prodotti, quantita, prezzi)
    print(f"Valore totale iniziale: €{valore_totale_magazzino(quantita, prezzi)}")
    
    # Elaborazione
    print("\n2. ELABORAZIONE ORDINI IN CORSO...")
    applica_ordini(prodotti, quantita, ordini_in_entrata)
    
    # Manutenzione
    print("\n3. MANUTENZIONE CATALOGO:")
    n_rimossi = rimuovi_esauriti(prodotti, quantita, prezzi)
    print(f"Operazione completata: {n_rimossi} prodotti obsoleti rimossi.")
    
    # Risultato Finale
    print("\n4. STATO FINALE MAGAZZINO:")
    stampa_inventario(prodotti, quantita, prezzi)
    
    # Analisi
    top3_per_valore(prodotti, quantita, prezzi)
    
    print("\n" + "="*40)
    print(f"VALORE FINALE MAGAZZINO: €{valore_totale_magazzino(quantita, prezzi)}")
    print("="*40)

# Lancio del programma
report_completo()
