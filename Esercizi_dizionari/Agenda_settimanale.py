# Un'agenda settimanale ha come chiavi i giorni della settimana e come valori le liste di impegni di quel giorno. 
# Le liste possono essere vuote se il giorno non ha impegni. 
# Devi gestire l'agenda modificando le liste-valore e rispondere a query che richiedono di cercare dentro di esse.


agenda = {
    "Lunedì":    ["Riunione 9:00", "Palestra 18:00"],
    "Martedì":   ["Dentista 10:30"],
    "Mercoledì": ["Riunione 9:00", "Pranzo con Marco 13:00", "Corso Python 20:00"],
    "Giovedì":   [],
    "Venerdì":   ["Call con cliente 15:00"],
    "Sabato":    ["Spesa", "Cinema 21:00"],
    "Domenica":  [],
}


print('')


# Fase 1. Visualizzazione e analisi

for giorno, impegni in agenda.items():
    if not impegni:
        print(f"{giorno} -> Giorno libero")
        print('')
        print('')
    else:
        print(f"Impegni {giorno}:")
        for i, v in enumerate(impegni, 1):
            print(f"{i}. {v}")
        print('')
        print('')

giorni_liberi = []
giorno_max = ''
lunghezza_impegni = 0


for giorno, impegni in agenda.items():
    if len(impegni) == 0:
        giorni_liberi.append(giorno)
    if len(impegni) > lunghezza_impegni:
        lunghezza_impegni = len(impegni)
        giorno_max = giorno
    

print(f"Giorni liberi nella settimana: {giorni_liberi}")
print(f"Giorno più pieno: {giorno_max}")

print('')
print('='*50)
print('')


# Fase 2. Modificare le liste-valore.

agenda["Giovedì"].append("Yoga 07:00")
agenda["Venerdì"].append("Colazione di lavoro 08:30")
agenda["Lunedì"].remove("Palestra 18:00")
agenda["Venerdì"].remove("Call con cliente 15:00")
agenda["Giovedì"].insert(0, "Call con cliente 06:00")

print("--- AGENDA AGGIORNATA DOPO LA FASE 2 ---")
for giorno, impegni in agenda.items():
    print(f"{giorno}: {impegni}")   


print('')
print('='*50)
print('')


# Fase 3. Ricerca testuale degli impegni.


for giorno, impegni in agenda.items():
    for impegno in impegni:
        if "Riunione" in impegno:
            print(f"{giorno} -> {impegno}")

print('')
totale_impegni = 0
for impegni in agenda.values():
    totale_impegni += len(impegni)
print(f"Totale degli impegni settimanali: {totale_impegni}")
print('')





