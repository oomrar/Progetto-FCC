# Lavori per la segreteria di una scuola media. Hai i voti di tre materie per ogni studente e devi produrre elaborazioni automatiche.

studenti = ["Alice", "Bruno", "Carla", "Diego", "Elena", "Fabio"]
voti = [
    [7, 8, 6],
    [5, 5, 4],
    [9, 10, 8],
    [6, 7, 7],
    [4, 5, 3],
    [8, 9, 9]
]
materie = ["Matematica", "Italiano", "Scienze"]

# 1. Calcolo medie

def calcola_media (lista_voti):
    somma = 0
    for i in range(len(lista_voti)):
        somma += lista_voti[i]
    media = somma / len(lista_voti)
    return media

def medie_classe (voti):
    medie_studenti = []
    for i in range(len(voti)):
        media = calcola_media(voti[i])
        medie_studenti.append(media)
    return medie_studenti

medie_attuali = medie_classe(voti)

# 2. Classificazione

def classifica_studenti (medie_studenti):
    promossi = []
    bocciati = []
    for i in range(len(medie_studenti)):
        if medie_studenti[i] >= 6:
            promossi.append(studenti[i])
        else:
            bocciati.append(studenti[i])
    return promossi, bocciati

def materia_critica (studenti, medie_studenti, voti, materie):
    for i in range(len(studenti)):
        if medie_studenti[i] < 6:
            indice_min = 0
            for j in range (len(materie)):
                if voti[i][j] < voti [i][indice_min]:
                    indice_min = j
            print(f"{studenti[i]} - materia critica: {materie[indice_min]}")    

print("--- Analisi Materie Critiche ---")
materia_critica(studenti, medie_attuali, voti, materie)

#3. Modifica e riepilogo

def applica_bonus (studenti, medie_studenti, voti):
    for i in range(len(studenti)):
        if medie_studenti[i] < 6:
            for j in range(len(materie)):
                if voti[i][j] < 10:
                    voti[i][j] += 1

applica_bonus(studenti, medie_attuali, voti)

nuove_medie = medie_classe(voti)
promossi, bocciati = classifica_studenti(nuove_medie)

somma_totale = 0
for m in nuove_medie:
    somma_totale += m
media_generale = somma_totale / len(studenti)

print("\n" + "="*30)
print("      RIEPILOGO FINALE")
print("="*30)
print(f"Studenti Promossi: {len(promossi)} {promossi}")
print(f"Studenti Bocciati: {len(bocciati)} {bocciati}")
print(f"Media Generale: {round(media_generale, 2)}")
print("="*30)
