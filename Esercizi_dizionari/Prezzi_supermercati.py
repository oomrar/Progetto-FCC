# Due supermercati vendono gli stessi prodotti a prezzi diversi, con alcune differenze nel catalogo. 
# Vuoi sapere dove conviene ogni singolo prodotto, costruire una lista della spesa ottimale prendendo sempre il prezzo più basso disponibile e quantificare il risparmio totale.

prezzi_A = {
    "pane":1.20,"latte":0.95,"uova":2.50,
    "pasta":0.89,"riso":1.10,"olio":4.50,
    "pomodori":1.80,"formaggio":3.20,
}
prezzi_B = {
    "pane":1.10,"latte":1.05,"uova":2.30,
    "pasta":0.99,"riso":0.95,"olio":4.80,
    "pomodori":1.60,"formaggio":3.50,"yogurt":0.75,
}

print('')

# Fase 1. Confronto prodotto per prodotto


for prodotto, prezzo in prezzi_A.items():
    prezzoB = prezzi_B.get(prodotto)
    if prezzoB is None:
        print("Prodotto non presente in B")
    else:
        risparmio = abs(prezzo-prezzoB)
        prezzo_conveniente = 0
        if prezzoB < prezzo:
            prezzo_conveniente = "B"
        else:
            prezzo_conveniente = "A"
        print (f"{prodotto} -> A: €{prezzo} , B: €{prezzoB} - Conviene {prezzo_conveniente}")
        print(f"Risparmio: €{round(risparmio, 3)}")
        print('')

lista_B = []
for prodotto in prezzi_B.keys():
    if prodotto not in prezzi_A:
        lista_B.append(prodotto)

print(f"Prodotti disponibili solo nel supermercato B: {lista_B}")
print('')

print('')
print('='*50)
print('')


# Fase 2. Costruire il catalogo al prezzo migliore

migliori_prezzi = prezzi_A.copy()

for prodotto, prezzi in prezzi_B.items():
    if prodotto not in migliori_prezzi:
        migliori_prezzi[prodotto] = prezzi
    elif prezzi < migliori_prezzi[prodotto]:
        migliori_prezzi[prodotto] = prezzi

print("--- CATALOGO CON I MIGLIORI PREZZI ---")
for prodotto, prezzo in migliori_prezzi.items():
    print(f"- {prodotto}: €{prezzo:.2f}")
print('')

print('')
print('='*50)
print('')

# Fase 3. Risparmio totale

def costo_totale(dizionario):
    spesa = 0
    for prezzo in dizionario.values():
        spesa += prezzo
    return spesa

spesa_A = costo_totale(prezzi_A)
spesa_B = costo_totale(prezzi_B)
spesa_migliori = costo_totale(migliori_prezzi)


prezzo_migliore = min(spesa_A, spesa_B, spesa_migliori)

prezzo_peggiore = max(spesa_A, spesa_B, spesa_migliori)

risparmio_perc = ((prezzo_peggiore - prezzo_migliore)/prezzo_peggiore) * 100
print("--- RIEPILOGO SPESA ---")
print('')
print(f"Spesa supermercato A: {spesa_A}\nSpesa supermercato B: {spesa_B}\nSpesa combinata due supermercati: {spesa_migliori}")
print(f"Prezzo migliore: {prezzo_migliore}")
print(f"Prezzo peggiore: {prezzo_peggiore}")
print('')
print(f"Percentuale di risparmio: {risparmio_perc:.2f} %")

print('')