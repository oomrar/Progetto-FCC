#Dobbiamo creare una funzione che decide il prezzo finale di un biglietto del cinema.


def calcola_prezzo(età, codice):
    prezzo = 10
    età = int(età)
    codice = str(codice)
    if età < 12 or età > 65:
        prezzo -= 3
    if codice and codice.upper() == "PROMO20":
        prezzo = prezzo * 0.8
    return prezzo

età_utente = int(input("Quanti anni hai? "))
codice_utente = input("Inserisci il codice sconto (se lo hai): ")

print(f"Il prezzo è: {calcola_prezzo(età_utente, codice_utente)}")