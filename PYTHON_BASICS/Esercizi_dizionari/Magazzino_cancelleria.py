# Gestisci il magazzino di una cartolibreria. 
# Il catalogo attuale è un dizionario di dizionari: ogni chiave è il nome del prodotto e il valore è un sotto-dizionario con quantità e prezzo. 
# Le modifiche arrivano in blocchi separati: nuovi arrivi, variazioni di prezzo, riassortimenti.

magazzino = {
    "penna biro":    {"qty": 150, "prezzo": 0.50},
    "quaderno A4":   {"qty": 80,  "prezzo": 2.20},
    "matita HB":     {"qty": 200, "prezzo": 0.30},
    "gomma":         {"qty": 60,  "prezzo": 0.80},
    "righello 30cm": {"qty": 45,  "prezzo": 1.10},
}
nuovi_arrivi = {
    "evidenziatore": {"qty": 100, "prezzo": 1.50},
    "post-it":       {"qty": 75,  "prezzo": 2.80},
    "temperino":     {"qty": 90,  "prezzo": 0.60},
}
aggiornamenti_prezzi = {
    "penna biro": 0.60,
    "gomma":      0.90,
    "matita HB":  0.35,
}


print('')
print(len(magazzino))
magazzino.update(nuovi_arrivi)
print(len(magazzino))
print('')

for prodotto, info in magazzino.items():
    quantita = info["qty"]
    prezzo = info ["prezzo"]
    print(f"{prodotto} | Quantità: {quantita} ; Prezzo: {prezzo}")
print('')


for prodotto, nuovo_prezzo in aggiornamenti_prezzi.items():
    if prodotto in magazzino:
        prezzo_vecchio = magazzino[prodotto]["prezzo"]
        magazzino[prodotto]["prezzo"] = nuovo_prezzo
        print(f"{prodotto}: {prezzo_vecchio} -> {nuovo_prezzo}")

prodotti_scarsi = []
for prodotto, info in magazzino.items():
    if info["qty"] < 70:
        prodotti_scarsi.append(prodotto)

valore_totale = 0
for dati in magazzino.values():
    valore_totale += dati["qty"] * dati["prezzo"]

print('')
print(f"Prodotti da riordinare: {', '.join(prodotti_scarsi)}")
print(f"Valore totale magazzino: {valore_totale}")
print('')
