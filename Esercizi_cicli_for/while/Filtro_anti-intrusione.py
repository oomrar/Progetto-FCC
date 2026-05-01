# Immagina di analizzare i tentativi di accesso a un database. Hai una stringa di log e devi bloccare tutto se rilevi troppe minacce.


accessi_raw = "USR10,USR12,HACK44,USR21,HACK99,USR05,HACK11,USR01, HACK45"

# Definisco il motore di controllo.
def analizza_codice (codice):
    if codice.strip().startswith("HACK"):
        return "MINACCIA" 
    if codice.strip().startswith ("USR"):
        return "SICURO"

# Variabili esterne al ciclo contatore e definizione lista.
minacce_rilevate = 0
lista_accessi = accessi_raw.split(",")

# Ciclo per la verifica degli accessi.
for accesso in lista_accessi:
    if analizza_codice (accesso) == "SICURO":
        print(f"Accesso {accesso} autorizzato.")
    elif analizza_codice (accesso) == "MINACCIA":
        minacce_rilevate +=1
        if minacce_rilevate == 3:
            print ("Sistema bloccato per sicurezza!")
            break
        print (f"ATTENZIONE: Rilevato {accesso}.")
    
