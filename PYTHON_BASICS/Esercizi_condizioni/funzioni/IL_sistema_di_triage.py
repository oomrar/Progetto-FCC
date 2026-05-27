#Dobbiamo creare un programma che assegna un codice di priorità ai pazienti in base a una stringa 
# di dati grezzi che arriva dall'accettazione.
# stringa di esempio: "99-mario_rossi-38.5-110"

def analizza_paziente(dati_grezzi):
    parti = dati_grezzi.split("-")
    nome_cogn = parti[1].replace("_"," ").upper()
    temperatura = float(parti[2])
    battiti = int(parti[3])
    if temperatura > 39.0 or battiti > 120:
        return "CODICE ROSSO", nome_cogn
    if temperatura > 37.5:
        return "CODICE GIALLO", nome_cogn
    else:
        return "CODICE VERDE", nome_cogn
    
   
stringa_paziente = input("Inserire stringa: ")
esito, nome_pulito = analizza_paziente(stringa_paziente)

print(f"{nome_pulito} - Esito: {esito}")
