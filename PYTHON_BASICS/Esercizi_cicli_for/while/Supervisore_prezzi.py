# Hai una lista di prodotti che arrivano da un catalogo estero. Ogni prodotto ha un codice finale che indica la valuta: _E per Euro e _D per Dollari.

catalogo = ["TV_E", "Radio_D", "PC_E", "Mouse_D", "Tastiera_E"]

prodotti_euro = []
prodotti_dollari = []

for prodotto in catalogo:
    if prodotto.endswith("_E"):
        prodotti_euro.append(prodotto[:-2])
    elif prodotto.endswith("_D"):
        prodotti_dollari.append(prodotto[:-2])

print(f"{prodotti_euro} \n {prodotti_dollari}")
