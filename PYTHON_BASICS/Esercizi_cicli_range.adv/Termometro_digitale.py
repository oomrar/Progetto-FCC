# Hai una serie di rilevazioni di temperatura giornaliera. Alcune sono errate perché il sensore ha dato valori impossibili. 
# Devi correggere i dati e produrre un'analisi.

# Dati:
temperature = [21.0, 19.5, -99.0, 23.1, 18.8, -99.0, 25.3, 22.7, -99.0, 20.1]
valore_errore = -99.0
valore_sostitutivo = 0.0

for i in range(len(temperature)):
    if temperature[i] == valore_errore:
        temperature[i] = valore_sostitutivo
        print (f"Valore corretto alla posizione {i}.")

print (temperature[:5])
print (temperature[-3:])

somma = 0
valide= 0

for i in range (len(temperature)):
    if temperature[i] != 0.0:
        somma += temperature[i]
        valide += 1

media = somma/valide
print(round(media, 2))
temperature_alte = []

for i in range (len(temperature)):
    if temperature[i] > 22.0:
        temperature_alte.append(temperature[i])
