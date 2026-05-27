#Immagina di ricevere da un vecchio database una stringa di testo con questo formato fisso:"RECP-4321-QTY-05-PRC-12.50"
# Il tuo compito è estrarre i dati e ricalcolarli.

code = "RECP-4321-QTY-05-PRC-12.50"

id_code = code [5:9]
quantity = int(code [14:16])
unit_price = float(code [21:])

total_cost = quantity * unit_price
id_code = id_code [::-1]

print(f"Ordine elaborato. Codice: {id_code}. Totale: {total_cost}")