
def prenota_posto():
    user_tick = input("Inserire la prenotazione (fila, numero_posto, età):")
    try:
        dati = user_tick.split(',')
        fila = dati[0]
        numero_posto = int(dati[1])
        eta = int(dati[2])
        if eta < 0 or eta > 120:
            raise ValueError("Età non valida.")
    except IndexError:
        print("Errore! Inserisci tutti i dati richiesti per terminare.")
        return
    except ValueError as e:
        if str(e) == "Età non valida.":
            print(e)
        else:
            print("Errore! Il numero del posto e l'età devono essere numeri")
        return
    print(f"Prenotazione effettuata con successo! Posto {numero_posto} fila {fila}.")

prenota_posto()

