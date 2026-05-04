# Sei il supervisore di un radar che monitora i droni in volo in una zona riservata. 
# Hai una lista di rilevamenti. Ogni drone invia una stringa con questo formato esatto:"ID_DRONE|ALTITUDINE_METRI|DISTANZA_KM|STATO"

rilevamenti = [
    "DRN-01|600|8.2|ATTIVO",
    "DRN-02|150|18.5|SOSPESO",
    "DRN-03|1200|4.0|ATTIVO",
    "DRN-04|800|15.1|ATTIVO"
]

def calcola_rischio(altitudine, distanza):
    if altitudine > 1000 or distanza < 5:
        return "ALTO"
    elif altitudine < 200:
        return "INTERDETTO"
    else:
        return "REGOLARE"
    
altitudine_totale = 0
allerta_rossa = 0


for drone in rilevamenti:
    dati = drone.split("|")
    ID = dati [0]
    altitudine = int(dati[1])
    distanza = float(dati[2])
    stato = dati[3]
    if stato == "SOSPESO":
        continue
    elif stato == "ATTIVO":
        calcola_rischio(altitudine, distanza)
        altitudine_totale += altitudine
        if calcola_rischio (altitudine, distanza) == "ALTO":
            allerta_rossa += 1
        print (f"Drone {ID}: altitudine {altitudine}m - Rischio: {calcola_rischio(altitudine, distanza)}.")
    