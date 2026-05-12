# Sei il responsabile del sistema di prenotazione di un piccolo cinema. 
# Hai i dati di 6 film in programmazione: titolo, sala, posti totali e posti prenotati. 
# Devi produrre la situazione delle sale e la classifica di riempimento.

film         = ["Interstellar", "Il Padrino", "Dune", "Matrix", "Oppenheimer", "Inception"]
sala         = [1, 2, 3, 1, 2, 3]
posti_totali = [120, 80, 150, 120, 80, 150]
prenotati    = [95, 80, 43, 117, 52, 138]

# Fase 1: situazione sale

def stampa_situazione(film, posti_totali, prenotati):
    for i in range(len(film)):
        messaggio = f"{film[i]} |  Posti liberi: {posti_totali[i]-prenotati[i]} | Posti prenotati: {prenotati[i]}"
        if posti_totali[i]- prenotati[i] == 0:
            messaggio += "🔴 SOLD OUT"
        print(messaggio)

stampa_situazione(film, posti_totali, prenotati)

print("+"*100)

# Fase 2: percentuale riempimento

def calcola_riempimento(posti_totali, prenotati):
    percentuali= []
    for i in range(len(film)):
        dato = (prenotati[i] / posti_totali[i]) * 100
        percentuali.append(dato)
    return percentuali
    
percentuali = calcola_riempimento(posti_totali, prenotati)

for i in range(len(film)):
    print(f"{film[i]} | {percentuali[i]}% pieno")

print("+"*100)

# Fase 3: Film per sala

for i in range(1,4):
    for j in range(len(film)):
        if sala[j]== i:
            print (f"{film[j]} | {percentuali[j]}")

print("+"*100)



