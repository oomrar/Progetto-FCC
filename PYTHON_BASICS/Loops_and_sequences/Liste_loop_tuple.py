#Liste semplici

playlist = ["Bohemian Rhapsody", "Stairway to Heaven", "Hotel California"]
playlist.append("Imagine")
playlist.append("Smells Like Teen Spirit")
playlist.insert(1, "Sweet Child O' Mine")
playlist[0] = "Hey Jude"
playlist.remove("Hotel California") 
playlist.pop(1)

print(len(playlist))
print(playlist)

print("-------------------------------------------------------------------------------" \
"" \
"" \
"")

#Esercizio con loop for e while.
#Hai una lista di prezzi (numeri) che rappresentano i prodotti nel tuo carrello. Alcuni prodotti sono difettosi (prezzo = 0) e il tuo budget è limitato.
carrello = [["Pane", 10], ["Pasta", 20], ["Mozzarella", 0], ["Vino", 15], ["Birra", 50], ["Coca Cola", 5], ["Acqua", 12]]
budget = 60
totale_spesa = 0
prodotti_acquistati = 0
prodotti_presi = []
for item in carrello:
    prodotto = item[0]
    prezzo = item[1]

    if prezzo == 0:
        print(f"Il prodotto {prodotto} è difettoso e non posso acquistarlo.")
        continue

    if totale_spesa + prezzo > budget:
        print(f"Ho superato il budget, non posso acquistare {prodotto}.")
        break

    totale_spesa += prezzo
    prodotti_acquistati += 1
    prodotti_presi.append(prodotto)
print("Ho speso in totale: €", totale_spesa, "e ho acquistato", prodotti_acquistati, "prodotti: ", prodotti_presi)
print("Il resto è: €", budget - totale_spesa)

print("-------------------------------------------------------------------------------" \
"" \
"" \
"")


#Caveau blindato
password_corretta= "Open Sesame"
tentativi_rimasti= 3

while tentativi_rimasti > 0:
    password_inserita = input("Inserisci la password per aprire il caveau:")
    if password_inserita == password_corretta:
        print("Caveau aperto")
        break
    else:
        tentativi_rimasti -=1
        print("Password errata. Tentativi rimasti:", tentativi_rimasti)
        if tentativi_rimasti == 0:
            print("Caveau bloccato. Contatta l'amministratore.")
            break
