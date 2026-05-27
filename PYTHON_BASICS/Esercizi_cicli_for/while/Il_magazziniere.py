# Hai una lista di prodotti in magazzino e una lista di prodotti ordinati da un cliente. Devi verificare cosa puoi spedire e cosa manca.

# Dati:

magazzino = ["mela", "mela", "mela", "arancia", "kiwi", "kiwi"]
ordine_cliente = ["mela", "arancia", "banana", "mela"]

for frutto in ordine_cliente:
    if frutto in magazzino:
        print (f"Spedizione di {frutto} pronta!")
        magazzino.remove(frutto)
    else:
        print (f"ERRORE: {frutto} non disponibile in magazzino.")

print(magazzino)  