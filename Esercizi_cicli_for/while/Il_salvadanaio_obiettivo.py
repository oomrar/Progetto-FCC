# Immagina di voler risparmiare per comprare un nuovo computer che costa 1000 euro. 
# Hai un salvadanaio vuoto e ogni settimana ci metti dentro dei soldi, ma la cifra cambia a seconda di quanto ti resta in tasca.

risparmi_totali = 0
obiettivo = 1000

while risparmi_totali < obiettivo:
    risposta = input ("Quanti soldi vuoi inserire? ")
    if risposta == "stop":
        break
    cifra = float(risposta)
    risparmi_totali += cifra
    if risparmi_totali >= obiettivo:
        break
    print (f"Hai risparmiato €{risparmi_totali}. Ti mancano ancora €{obiettivo - risparmi_totali}")

if risparmi_totali >= obiettivo:
    print(f"Obiettivo raggiunto! Hai messo da parte un totale di €{risparmi_totali}")
else:
    print(f"Obiettivo fallito, ma hai comunque messo da parte €{risparmi_totali}") 