# Gestisci i turni settimanali di un negozio. 
# Hai una lista di dipendenti e devi assegnare i turni automaticamente, analizzare la distribuzione e permettere modifiche mirate.

dipendenti = [
    "Alice", "Bruno", "Carla", "Diego",
    "Elena", "Fabio", "Giulia", "Hassan"
]
turni_disponibili = ["mattina", "pomeriggio", "sera"]

def assegna_turni (dipendenti, turni_disponibili):
    lista_turni = []
    for i, nome in enumerate (dipendenti):
        indice_turno = i % len(turni_disponibili)
        turno_scelto = turni_disponibili[indice_turno]
        lista_turni.append([nome, turno_scelto])
    return lista_turni

assegnazioni = assegna_turni(dipendenti, turni_disponibili)

def stampa_turni(assegnazioni):
    for i, value in enumerate(assegnazioni, 1):
        print(f"{i}. {value[0]} {value[1]}")
stampa_turni(assegnazioni)
print("*"*50)
print("*"*50)


# Fase 2. Analisi con count()

def quanti_per_turno(assegnazioni):
    lista_turni = []
    for i, value in enumerate (assegnazioni):
        lista_turni.append(value[1])
    m = lista_turni.count("mattina")
    p = lista_turni.count("pomeriggio")
    s = lista_turni.count("sera")
    print(f"Distribuzione turni: \nMattina: {m}\nPomeriggio: {p}\nSera: {s}")

quanti_per_turno(assegnazioni)
print("*"*50)
print("*"*50)

def dipendenti_del_turno (assegnazioni, turno_cercato):
    dipendenti_turno = []
    for i, value in enumerate(assegnazioni):
        if value[1] == turno_cercato:
            dipendenti_turno.append(value[0])
    return dipendenti_turno

turno_cercato = "mattina"
print(dipendenti_del_turno(assegnazioni, turno_cercato))
print("*"*50)
print("*"*50)


# Fase 3. Modifica mirata

def scambia_turno (assegnazioni, nome,nuovo_turno):
    for i, value in enumerate(assegnazioni):
        if value[0] == nome:
            assegnazioni[i][1] = nuovo_turno
            return assegnazioni
    return "Errore"

def report_finale(assegnazioni):
    print("\n" + "="*30)
    print("   REPORT GESTIONALE TURNI")
    print("="*30)
    
    totale = len(assegnazioni)
    print(f"Numero totale dipendenti: {totale}")
    
    print("\n--- Distribuzione Carichi ---")
    quanti_per_turno(assegnazioni)
    
    print("\n--- Responsabili ---")
    print(f"Primo dipendente in lista: {assegnazioni[0][0]}")
    print(f"Ultimo dipendente in lista: {assegnazioni[-1][0]}")
    
    print("\n--- Elenco Completo Turni ---")
    stampa_turni(assegnazioni)
    print("="*30)

report_finale(assegnazioni)
    


        





