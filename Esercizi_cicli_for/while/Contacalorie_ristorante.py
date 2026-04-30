# Immagina di dover analizzare i piatti ordinati da un cliente per capire se ha superato il suo limite calorico giornaliero.
# Ogni elemento è una stringa così formata:"NOME_PIATTO:CALORIE:CATEGORIA".

ordine_cliente = ["Pizza:800:Piatto", "Insalata:150:Contorno", "Tiramisù:600:Dolce", "Mela:80:Frutta"]

def valuta_calorie (calorie):
    if calorie > 500:
        return "PESANTE"
    else:
        return "LEGGERO"

calorie_totali = 0
contatore_dolci = 0

for tipo in ordine_cliente:
    dati = tipo.split(":")
    nome = dati [0]
    calorie = int(dati [1])
    categoria = dati [2]
    calorie_totali += calorie

    if categoria == "Dolce":
        contatore_dolci += 1
    
    print (f"{nome} è un piatto {valuta_calorie(calorie)} ({calorie} kcal)")