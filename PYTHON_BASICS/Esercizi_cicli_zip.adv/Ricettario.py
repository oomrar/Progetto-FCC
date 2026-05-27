# Hai due ricette: una per la pasta al pomodoro e una per la pasta al pesto. 
# Ogni ricetta è descritta da tre liste parallele: gli ingredienti, le quantità e le unità di misura. 
# Le ricette sono per 2 persone. Devi visualizzarle, scalarle per un numero variabile di persone e confrontarle.

## Ricetta 1 — Pasta al Pomodoro (per 2 persone)
ing_pomodoro  = ["pasta", "pomodori", "aglio", "olio", "basilico", "sale"]
qty_pomodoro  = [200, 400, 2, 30, 10, 5]
unit_pomodoro = ["g", "g", "spicchi", "ml", "foglie", "g"]

## Ricetta 2 — Pasta al Pesto (per 2 persone)
ing_pesto  = ["pasta", "basilico", "pinoli", "parmigiano", "olio", "aglio"]
qty_pesto  = [200, 50, 30, 40, 60, 1]
unit_pesto = ["g", "g", "g", "g", "ml", "spicchio"]

porzioni_desiderate = 5

print('')

# Fase 1. Visualizzazione ricette

def visualizzatore_ricetta(ingredienti, quantita, unita):
    for ing, q, u in zip(ingredienti, quantita, unita):
        print(f"- {q} {u} di {ing}")
print("Ricetta pasta al pomodoro:")
visualizzatore_ricetta(ing_pomodoro, qty_pomodoro, unit_pomodoro)
print('')
print("Ricetta pasta al pesto:")
visualizzatore_ricetta(ing_pesto, qty_pesto, unit_pesto)

print('='*50)


# Fase 2. Scalare ricetta

def porzioni(ingredienti, quantita, unita, porzioni_desiderate):
    qty_scalate = []
    for ing, q, u in zip(ingredienti, quantita, unita):
        q = q * porzioni_desiderate /2
        qty_scalate.append(q)
    return qty_scalate

quantità_aggiornate_pom = porzioni(ing_pomodoro, qty_pomodoro, unit_pomodoro, porzioni_desiderate)
quantità_aggiornate_pest = porzioni(ing_pesto, qty_pesto, unit_pesto, porzioni_desiderate)

print(f"Quantità aggiornate per {porzioni_desiderate} persone.")
print('')
print("Quantità per ricetta pomodoro:")
visualizzatore_ricetta(ing_pomodoro, quantità_aggiornate_pom, unit_pomodoro)
print("Quantità per ricetta pesto:")
visualizzatore_ricetta(ing_pesto, quantità_aggiornate_pest, unit_pesto)
print('')


print('='*50)


# Fase 3. Confronto tra ricette

ing_in_comune = []
for ing in ing_pomodoro:
    if ing in ing_pesto:
        ing_in_comune.append(ing)

print(f'Ingredienti in comune fra le due ricette: {ing_in_comune}')

for ing in ing_in_comune:
    idx_pomodoro = ing_pomodoro.index(ing)
    q_pomodoro = qty_pomodoro[idx_pomodoro]
    unita_pomodoro = unit_pomodoro[idx_pomodoro]

    idx_pesto = ing_pesto.index(ing)
    q_pesto = qty_pesto[idx_pesto]
    unita_pesto = unit_pesto[idx_pesto]

    print (f"{ing}: {q_pomodoro}{unita_pomodoro} (pomodoro) vs {q_pesto}{unita_pesto} (pesto)")
