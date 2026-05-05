# Stai preparando un sistema di lancio per un razzo giocattolo. Devi costruire e manipolare una sequenza di conteggio con range, poi modificarla.

# Dati:
messaggi_lancio = ["Motori accesi", "Rilascio morsetti", "Decollo"]

for num in range(10,0,-1):
    print(f"\n{num}")
    if num == 1:
        print ("\n🚀 LANCIO!")

sequenza = []

for num in range(1,11):
    sequenza.append(num)

sequenza.insert(0,0)

ultimo = sequenza.pop(-1)
print (f"Ultimo valore rimosso: {ultimo}")

for i in range(len(messaggi_lancio)):
    print(f"Fase {i+1}: {messaggi_lancio[i]}")