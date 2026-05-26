# Hai il log completo dei punti segnati durante una partita di basket. 
# Ogni elemento della lista è una coppia [giocatore, punti_azione]. 
# Le azioni di ogni giocatore sono sparse in tutto il log nell'ordine in cui sono accadute. 
# Devi ricostruire le statistiche aggregando tutte le azioni di ogni giocatore.


log_partita = [
    ["Marco", 2], ["Sara", 3], ["Marco", 2], ["Luca", 2],
    ["Sara", 2],  ["Elena", 3],["Marco", 3], ["Luca", 2],
    ["Sara", 2],  ["Elena", 2],["Marco", 2], ["Sara", 3],
    ["Luca", 3],  ["Marco", 2],["Elena", 2], ["Sara", 2],
    ["Luca", 2],  ["Elena", 3],["Marco", 3], ["Luca", 2],
]

print('')

# Fase 1. Aggregare i punti totali.

totali = {}
for giocatore, punti in log_partita:
    totali[giocatore] = totali.get(giocatore, 0) + punti

for giocatore, punti in totali.items():
    print(f"Giocatore: {giocatore} | Punti: {punti}")

print('')
print('='*50)
print('')


# Fase 2. Statistiche più ricche

stats = {}
for giocatore, punti in log_partita:
    stats[giocatore] = stats.get(giocatore, [0, 0])
    stats[giocatore][0] += punti
    stats[giocatore][1] += 1

for giocatore, statistiche in stats.items():
    media_giocatore = statistiche[0]/statistiche[1]
    print(f"Giocatore: {giocatore} | Media punti: {round(media_giocatore, 2)}")


print('')
print('='*50)
print('')


# Fase 3. Classifica e MVP

statistiche_giocatore = []
for giocatore, statistiche in stats.items():
    punti_fatti = statistiche[0]
    canestri = statistiche [1]
    statistiche_giocatore.append([giocatore, punti_fatti, canestri])

statistiche_giocatore_o = sorted(statistiche_giocatore, key = lambda x: x[1], reverse = True)

print(" --- CLASSIFICA ---")
print('')
for i , [giocatore, punti_fatti, canestri] in enumerate(statistiche_giocatore_o, 1):
    if i == 1:
        print(f"MVP: {giocatore}")
        print('')
    print(f"{i}. {giocatore} | Punti fatti: {punti_fatti} | Canestri: {canestri}")

print('')

punti_totali = 0
for statistiche in stats.values():
    punti = statistiche[0]
    punti_totali += punti

print(f"Punti totali della squadra: {punti_totali}")

print('')
