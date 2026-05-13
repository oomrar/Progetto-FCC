# Una piccola sala cinematografica ha 5 file di 8 posti. 
# Il valore 0 indica posto libero, 1 indica posto occupato. 
# Le file sono identificate da lettere (A, B, C, D, E), i posti da numeri (1–8). 
# Un cliente vuole prenotare un certo numero di posti consecutivi nella fila che preferisce.

sala = [
    [0, 1, 1, 0, 0, 1, 0, 0],  # fila A
    [1, 1, 0, 0, 1, 1, 0, 1],  # fila B
    [0, 0, 0, 1, 0, 0, 0, 1],  # fila C
    [1, 0, 1, 1, 1, 0, 1, 0],  # fila D
    [0, 0, 0, 0, 0, 0, 0, 0],  # fila E
]
lettere_fila = ["A", "B", "C", "D", "E"]

prenotazione = ["C", 3]  # il cliente vuole 3 posti consecutivi in fila C


# Fase 1. Visualizzazione della sala

def stampa_posti(sala, lettere_fila):
    print("---- MAPPA DEI POSTI ----")
    for i, value in enumerate(sala):
        lettera_corrispondente = lettere_fila[i]
        fila_posti = []
        for p in value:
            if p:
                fila_posti.append("[X]")
            else:
                fila_posti.append("[ ]")
        print(f"{lettera_corrispondente} {' '.join(fila_posti)}")


# Fase 2. Analisi disponibilità

def conta_posti(sala, lettere_fila):
    posti_liberi_complessivi = 0
    print("---- Riepilogo posti liberi ----")
    for i, value in enumerate(sala):
        posti_liberi = 0
        for p in value:
            if not p:
                posti_liberi += 1
        posti_liberi_complessivi += posti_liberi
        print (f"Fila {lettere_fila[i]}: {posti_liberi} posti liberi")
    print (f"Posti liberi complessivi: {posti_liberi_complessivi}")

def trova_file(sala, prenotazione, lettere_fila):
    n_richiesti = prenotazione[1]
    file_compatibili = []
    print ("---- VERIFICA DISPONIBILITÀ PRENOTAZIONE ----")
    for i, fila in enumerate(sala):
        contatore = n_richiesti
        for posto in fila:
            if not posto:
                contatore -= 1
                if contatore == 0:
                    file_compatibili.append(lettere_fila[i])
                    break
            else:
                contatore = n_richiesti
    print (f"File compatibili: {file_compatibili}")
    return file_compatibili 





                




            