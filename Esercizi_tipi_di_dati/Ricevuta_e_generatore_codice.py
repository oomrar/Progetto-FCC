#Crea un programma che gestisce l'acquisto di un libro e genera un codice promozionale personalizzato per il cliente.

titolo_libro = str(input("Titolo del libro: "))
prezzo = float(input ("Prezzo singola copia: "))
numero_copie = int(input ("Numero copie desidereate: "))
numero_pagine = 200

prezzo_totale = prezzo * numero_copie
codice_sconto = titolo_libro.upper()[0:4] + str(numero_pagine*numero_copie)

print (f"{titolo_libro.upper()}\n{prezzo_totale}\n{codice_sconto}")