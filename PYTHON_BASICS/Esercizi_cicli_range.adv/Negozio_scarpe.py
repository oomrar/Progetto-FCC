# Lavori in un negozio di scarpe e devi gestire il magazzino: stampare il catalogo, trovare i prezzi e aggiornare le quantità rimaste.

modelli   = ["Air Max", "Stan Smith", "Chuck Taylor", "Superstar", "Old Skool", "Forum"]
prezzi    = [129.90, 89.90, 75.00, 95.00, 70.00, 110.00]
quantita  = [3, 0, 5, 2, 0, 4]

for i in range(len(modelli)):
    print(f"{i+1}. {modelli[i]} - {prezzi[i]} | Disponibili: {quantita[i]}")

for i in range (len(quantita)):
    if quantita[i] == 0:
        print (f"{modelli[i]}: esaurito")

economic = 0
for i in range(len(modelli)):
    if prezzi[i] < prezzi [economic]:
        economic = i
    
print(f"Modello più economico: {modelli[economic]} a {prezzi[economic]}")

disponibili = []
for i in range(len(modelli)):
    if quantita[i] > 0:
        disponibili.append(modelli[i])
print(disponibili)

valore_magazzino = 0
for i in range(len(modelli)):
    valore_magazzino += prezzi[i] * quantita[i]

print (f"Valore totale magazzino: {valore_magazzino}.")


