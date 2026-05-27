# Un quiz serale ha prodotto un dizionario con i punteggi finali di tutti i partecipanti. 
# La chiave è il nome del partecipante, il valore è il suo punteggio intero da 0 a 100. 
# Devi analizzare i risultati, costruire una classifica ordinata e assegnare categorie di merito.

punteggi = {
    "Martina": 87,
    "Lorenzo": 63,
    "Paola":   95,
    "Gianni":  71,
    "Sofia":   88,
    "Nico":    55,
    "Bea":     92,
    "Omar":    78
}


# Fase 1. Visualizzazione e conteggio con items

print('')
punt_sup = 0
punt_inf = 0
print("LISTA PUNTEGGI")
print('')
for nome, pt in punteggi.items():
    print(f"{nome} → {pt}")
    if pt > 80:
        punt_sup += 1
    if pt < 70:
        punt_inf += 1

print('')
print(f"Partecipanti con punteggio superiore a 80: {punt_sup}")
print(f"Partecipanti con punteggio inferiore a 70: {punt_inf}")
print('')


# Fase 2. Costrire classifica ordinata

lista = []
for nome, pt in punteggi.items():
    lista.append([nome, pt])

lista_ordinata = sorted(lista, key = lambda x:x[1], reverse = True)

print('')
print("CLASSIFICA:")
print('')
for i, value in enumerate(lista_ordinata, 1):
    print(f"{i}° {value[0]} - {value[1]} punti.")
print('')


# Fase 3. Categorie di risultato

eccellente = []
buono = []
sufficiente = []
insufficiente = []
for nome, pt in punteggi.items():
    if pt >= 90:
        eccellente.append(nome)
    if pt >= 70 and pt <= 89:
        buono.append(nome)
    if pt >= 55 and pt <= 69:
        sufficiente.append(nome)
    if pt < 55:
        insufficiente.append(nome)

print("CATEGORIE:")
print('')
print(f"Eccellenti ({len(eccellente)}): {eccellente}")
print(f"Buoni ({len(buono)}): {buono}")
print(f"Sufficienti ({len(sufficiente)}): {sufficiente}")
print(f"Insufficienti ({len(insufficiente)}): {insufficiente}")
print('')

