# Una stazione meteo ha registrato le temperature di 14 giorni (due settimane) in Celsius. 
# Devi convertirle in Fahrenheit, analizzare le giornate calde e fredde, e calcolare statistiche settimanali. 
# Tutto usando list comprehension e sum() senza cicli for espliciti dove possibile.

giorni = ["Lun","Mar","Mer","Gio","Ven","Sab","Dom",
          "Lun","Mar","Mer","Gio","Ven","Sab","Dom"]
temp_celsius = [12, 15, 18, 22, 25, 28, 24,
                10, 13, 17, 20, 23, 19, 14]
soglia_calda  = 22   # gradi Celsius
soglia_fredda = 15

print('')

# Fase 1. Conversione con list comprehension

temp_fahrenheit = [celsius * 9/5 + 32 for celsius in temp_celsius]
report = [f"{giorno}: {grado_celsius}°C / {grado_fah}°F" for giorno, grado_celsius, grado_fah in zip(giorni, temp_celsius,temp_fahrenheit)]

print("--- LISTA TEMPERATURE ---")
print('')
for riga in report:
    print(f"{riga}")
print('')


# Fase 2. Filtro con condizione

giorni_caldi = [giorno for giorno, temperatura in zip(giorni, temp_celsius) if temperatura >= soglia_calda]
giorno_freddi = [giorno for giorno, temperatura in zip(giorni, temp_celsius) if temperatura <= soglia_fredda]
temp_miti = [temperatura for temperatura in temp_celsius if temperatura > soglia_fredda and temperatura < soglia_calda]


# Fase 3. Statistiche settimanali con SUM e COMPREHENSION

sett1 = temp_celsius[:7]
sett2 = temp_celsius [7:]

media_sett1 = sum(sett1) / len(sett1)
media_sett2 = sum(sett2) / len(sett2)

temp_min_sett1 = sorted(sett1)[0]
temp_max_sett1 = sorted(sett1)[-1]

temp_min_sett2 = sorted(sett2)[0]
temp_max_sett2 = sorted(sett2)[-1]

print('')
print('='*50)
print("--- RIEPILOGO ---")
print('')

print(f"Temperature settimana 1: {sett1}")
print(f"Temperatura massima: {temp_max_sett1}")
print(f"Temperatura minima: {temp_min_sett1}")
print(f"Temperatura media settimana 1: {media_sett1:.2f}")
print('')
print(f"Temperature settimana 2: {sett2}")
print(f"Temperatura massima: {temp_max_sett2}")
print(f"Temperatura minima: {temp_min_sett2}")
print(f"Temperatura media settimana 2: {media_sett2:.2f}")

print('')