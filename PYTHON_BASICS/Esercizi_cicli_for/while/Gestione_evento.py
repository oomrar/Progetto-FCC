# Invece di avere una lista ordini pronta, usiamo un while per simulare una biglietteria che lavora finché ci sono posti.

posti_disponibili = [1,2,3,4,5]

while posti_disponibili:
    risposta = int(input(f"Quale posto vuoi prenotare?(Disponibili {posti_disponibili})"))
    if risposta in posti_disponibili:
        posti_disponibili.remove(risposta)
        print (f"Posto {risposta} prenotato con successo!")
    else:
        print (f"Spiacente, il posto {risposta} non esiste o è già occupato.")


print("Tutti i posti sono esauriti")