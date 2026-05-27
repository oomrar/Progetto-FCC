# Il menu di una caffetteria è un dizionario dove le chiavi sono i nomi delle bevande e i valori i prezzi in euro. 
# Devi costruire visualizzazioni del menu, analizzare i prezzi e mantenere il listino aggiornato — senza mai ricorrere all'accesso per indice numerico, che non esiste nei dizionari.

menu = {
    "Espresso":        1.10,
    "Cappuccino":      1.40,
    "Caffè Latte":     1.60,
    "Macchiato":       1.20,
    "Cioccolata":      2.00,
    "Tè":              1.10,
    "Succo d'arancia": 2.50,
    "Acqua":           0.50
}

# Fase 1. Visualizzare con keys e calcolare con values

print(' ')
print("LISTA BEVANDE")
print(' ')
for i, bevanda in enumerate(menu.keys(), 1):
    print(f"{i}. {bevanda}")
print(' ')

somma = 0
for prezzo in menu.values():
    somma += prezzo
media = round(somma/len(menu), 2)

print(f"Somma totale prezzi: {round(somma, 2)}")
print(f"Media: {media}")
print(' ')


# Fase 2. Filtrare con iterazione sulle chiavi

prod_costosti = []
prod_economici = []
for k in menu:
    if menu[k] < 1.50:
        prod_economici.append(k)
    if menu[k] >= 1.50:
        prod_costosti.append(k)

cost_ordinata = sorted(prod_costosti)
eco_ordinata = sorted(prod_economici)

print(f"Bevande economiche: {eco_ordinata}")
print(f"Bevande premium: {cost_ordinata}")
print(' ')


# Fase 3. Trovare gli estremi e aggiornare il menu

prezzo_min = float('inf')
prezzo_max = 0
for v in menu.values():
    if v > prezzo_max:
        prezzo_max = v
    if v < prezzo_min:
        prezzo_min = v

for k in menu:
    if menu[k] == prezzo_min:
        bev_min = k
    if menu[k] == prezzo_max:
        bev_max = k

print(f"Più cara: {bev_max} ({prezzo_max}) | Più economica: {bev_min} ({prezzo_min}))")
print(' ')

menu["Frappuccino"] = 3.20
print(' ')
print("LISTA BEVANDE AGGIORNATA")
print(' ')
for i, bevanda in enumerate(menu.keys(), 1):
    print(f"{i}. {bevanda}")
print(' ')

somma = 0
for prezzo in menu.values():
    somma += prezzo
media = round(somma/len(menu), 2)

print(f"Somma totale prezzi: {round(somma, 2)}")
print(f"Media: {media}")
print(' ')

prezzo_min = float('inf')
prezzo_max = 0
for v in menu.values():
    if v > prezzo_max:
        prezzo_max = v
    if v < prezzo_min:
        prezzo_min = v

for k in menu:
    if menu[k] == prezzo_min:
        bev_min = k
    if menu[k] == prezzo_max:
        bev_max = k

print(f"Più cara: {bev_max} ({prezzo_max}) | Più economica: {bev_min} ({prezzo_min}))")
print(' ')


