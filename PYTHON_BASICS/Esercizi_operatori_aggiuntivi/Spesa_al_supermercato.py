# Stai calcolando il costo di una spesa al mercato. 
# Hai le liste degli articoli e dei prezzi. 
# Il tuo obiettivo è sperimentare sum() e la list comprehension per trasformare e analizzare i prezzi senza scrivere cicli espliciti.


articoli = ["pane","latte","uova","pasta","olio","formaggio","frutta","verdura"]
prezzi   = [1.20, 0.95, 2.50, 0.89, 4.50, 3.20, 2.80, 1.60]
sconti   = [0,    10,   0,    5,    0,    15,   10,   0  ]  # percentuale di sconto

print('')

# Fase 1. SUM per totali e sottoliste

totale_spesa = sum(prezzi)
prima_meta = sum(prezzi[:4])
seconda_meta = sum(prezzi[4:])

if totale_spesa == (prima_meta + seconda_meta):
    print(f"Il totale della spesa è giusto ({totale_spesa})")
else:
    print("Il totale della spesa è sbagliato")

print('')

media_prezzo_articolo = round(totale_spesa/len(prezzi), 2)
print(f"Il prezzo medio per articolo è: €{media_prezzo_articolo}.")
print('')


# Fase 2. List comprehension per trasformare prezzi

prezzi_scontati = [round(prezzo * (1-sconto/100), 2) for prezzo, sconto in zip(prezzi, sconti)]
print(f"Lista scontata:\n{prezzi_scontati}")
print('')


# Fase 3. Comprehension con condizione e sum combinati

cari = [prodotto for prodotto, prezzo in zip(articoli, prezzi) if prezzo > 2]
prezzi_cari = [prezzo for prezzo in  prezzi if prezzo > 2]

peso_cari = sum(prezzi_cari)
percentuale_cari = (peso_cari / totale_spesa)*100

for prodotto, prezzo in zip(cari, prezzi_cari):
    print(f"Prodotto caro: {prodotto} al prezzo di €{prezzo}")

print('')
print(f"Peso prodotto caro sul totale: {percentuale_cari:.2f}%")
print('')