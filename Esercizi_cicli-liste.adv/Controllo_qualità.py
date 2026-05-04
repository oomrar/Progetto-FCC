# Lavori in una fabbrica che produce componenti elettronici. 
# Hai una lista che contiene i punteggi di qualità (da 1 a 100) di una serie di lotti appena prodotti.

lotti_qualita = [85, 42, 90, 55, 30, 95, 60]

def verifica_standard(punteggio):
    if punteggio >= 60:
        return "APPROVATO"
    else:
        return "SCARTATO"
    
for i in range(len(lotti_qualita)-1, -1, -1):
    punteggio = lotti_qualita[i]

    if verifica_standard(punteggio) == "SCARTATO":
        lotti_qualita.pop(i)
        print(f"All'indice: {i} | Rimosso: {punteggio}")

for indice, punteggio in enumerate(lotti_qualita):
    print(f"Indice: {indice} | Punteggio: {punteggio}")
        

