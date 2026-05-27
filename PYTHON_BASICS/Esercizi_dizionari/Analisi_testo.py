# Hai due testi divisi in liste di parole già normalizzate (lowercase, senza punteggiatura). 
# Devi analizzare la frequenza delle parole in ciascun testo, filtrarle rimuovendo le parole comuni (stopwords) e confrontare i due testi per trovare somiglianze e differenze.

testo_A = [
    "il","gatto","si","siedeva","sul","tappeto","il","cane",
    "dormiva","sul","divano","il","gatto","guardava","il","cane",
    "il","tappeto","era","morbido","il","divano","era","comodo",
    "il","cane","si","svegliò","il","gatto","scappò","via",
]
testo_B = [
    "il","sole","splendeva","sul","mare","il","vento","soffiava",
    "il","mare","era","calmo","il","sole","tramontava","lentamente",
    "il","vento","portava","profumo","di","sale","il","mare",
]
stopwords = ["il","la","lo","le","i","gli","si","di","sul","su","era","via"]

print('')

# Fase 1. Costruire le frequenze.

freq_A = {}
for parola in testo_A:
    freq_A [parola] = freq_A.get(parola, 0) +1

for parola, freq in freq_A.items():
    print(f"Frequenza {parola} -> {freq}")
print('')
print(f"Parole totali: {len(freq_A)}")
print('')

print('')
print("="*50)
print('')


# Fase 2. Filtrare le stopwords e trovare le top parole

freq_filtrata = {}
for parola, frequenza in freq_A.items():
    if parola not in stopwords:
        freq_filtrata [parola] = frequenza

lista_filtrata = []
for parola, frequenza in freq_filtrata.items():
    lista_filtrata.append([parola, frequenza])

lista_filtrata_o = sorted(lista_filtrata, key = lambda x: x[1], reverse = True)

print("--- PAROLE PIU FREQUENTI ---")
for i, [parola, frequenza] in enumerate(lista_filtrata_o[:5],1):
    print(f"{i}. {parola} appare {frequenza} volte")

print('')

print('')
print("="*50)
print('')

# Fase 3. Confrontare i due testi.

freq_B = {}
for parola in testo_B:
    freq_B [parola] = freq_B.get(parola, 0) +1

def trova_coincidenze(dizionarioA, dizionarioB):
    parole_comune = []
    parole_no_comune = []
    for parola in dizionarioA.keys():
        if parola in dizionarioB:
            parole_comune.append(parola)
        else:
            parole_no_comune.append(parola)
    return parole_comune, parole_no_comune

parole_comune_A, parole_no_comune_A = trova_coincidenze(freq_A, freq_B)

print("PAROLE NON IN COMUNE DEL TESTO A:")
print(parole_no_comune_A)

print('')

parole_comune_B, parole_no_comune_B = trova_coincidenze(freq_B, freq_A)

print("PAROLE NON IN COMUNE DEL TESTO B:")
print(parole_no_comune_B)

print('')

print('PAROLE IN COMUNE TRA I DUE TESTI')
print(parole_comune_A)

print('')

