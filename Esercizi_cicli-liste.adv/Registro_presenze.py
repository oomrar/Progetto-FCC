# Sei l'addetto alla segreteria di un corso serale. 
# Hai le presenze di 7 studenti nelle ultime 5 lezioni e devi produrre un report completo delle assenze e delle presenze.

# Dati:
studenti = ["Amati", "Belli", "Caruso", "De Luca", "Esteri", "Ferri", "Grasso"]

presenze = [
    [1, 1, 0, 1, 1],
    [1, 0, 0, 1, 0],
    [1, 1, 1, 1, 1],
    [0, 1, 1, 0, 1],
    [1, 1, 0, 0, 1],
    [0, 0, 1, 1, 0],
    [1, 1, 1, 1, 0],
]

promossi = []
a_rischio = []

for i in range(len(studenti)):
    conteggio_presenze = 0
    for j in range(len(presenze[i])):
        if presenze[i][j] == 1:
            conteggio_presenze += 1
    print(f"{studenti[i]} | {conteggio_presenze}/5 lezioni presenti.")
    if conteggio_presenze >=3:
        promossi.append(studenti[i])
    else:
        a_rischio.append(studenti[i])

print(f"Gli studenti promossi sono: {promossi}")
print(f"Gli studenti a rischio sono: {a_rischio}")

for i in range(len(presenze[0])):
    conteggio_studenti = 0
    for j in range(len(studenti)):
        if presenze [j][i] == 1:
            conteggio_studenti += 1
    print(f"Lezione {i+1}: {conteggio_studenti} studenti presenti.")

for i in range(len(studenti)-1,-1,-1):
    conteggio_presenze = 0
    for j in range(len(presenze[i])):
        if presenze[i][j] == 1:
            conteggio_presenze += 1

for i in range(0,len(studenti), 2):
    conteggio_presenze = 0
    for j in range(len(presenze[i])):
        if presenze[i][j] == 1:
            conteggio_presenze += 1
    print(f"{studenti[i]} | {conteggio_presenze}/5 lezioni presenti.")

print("-----------------------------------")

for i in range(1,len(studenti), 2):
    conteggio_presenze = 0
    for j in range(len(presenze[i])):
        if presenze[i][j] == 1:
            conteggio_presenze += 1
    print(f"{studenti[i]} | {conteggio_presenze}/5 lezioni presenti.")

