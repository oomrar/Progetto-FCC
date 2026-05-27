# Devi scrivere un programma che riceve una stringa "sporca" rappresentante un ordine e decide 
# se la transazione può essere approvata o se deve essere segnalata.
# Esempio: ORD774#mario_rossi#Smartphone_X#250.00#2

def processa_ordine(dati_ordine):
    dati = dati_ordine.split("#")
    ordine_id = dati[0]
    anagrafe = dati[1]
    prodotto = dati[2]
    prezzo = float(dati [3])
    quantità = int(dati[4])
    parti = anagrafe.split("_") #qua avresti potuto scrivere nome, cognome = anagrafe.split("_") invece di creare due variabili separatamente.
    nome = parti[0]  
    cognome = parti [1]
    client_name = nome [0].upper() + ". " + cognome.upper()
    total = prezzo * quantità

    if total > 1000:
        return "DA REVISIONARE", ordine_id, client_name, total, prodotto
    if total and quantità > 5:
        return "CONTROLLO QUANTITÀ", ordine_id, client_name, total, prodotto
    else:
        return "APPROVATO", ordine_id, client_name, total, prodotto
    
stringa_utente = input("Inserire stringa ordine:")
stato, ordine, nome_pulito, totale, prodotto = processa_ordine(stringa_utente)

print(f"Ordine {ordine} di {prodotto} per {nome_pulito} - Totale: {totale}€ - Stato: {stato}")

