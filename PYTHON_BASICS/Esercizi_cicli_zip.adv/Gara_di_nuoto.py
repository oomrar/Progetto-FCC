# Una competizione di nuoto ha due batterie con lo stesso numero di corsie. 
# Ogni batteria ha i nomi dei nuotatori e i loro tempi in secondi. Le corsie sono numerate da 1. 
# Il vincitore di ogni corsia è chi ha il tempo minore nelle rispettive batterie. 
# Alla fine si decide quale batteria è complessivamente più veloce.

batteria_A_nomi  = ["Luca", "Sara", "Marco", "Elena", "Pietro"]
batteria_A_tempi = [54.3, 52.1, 55.8, 51.7, 53.4]

batteria_B_nomi  = ["Giulia", "Davide", "Anna", "Fabio", "Chiara"]
batteria_B_tempi = [53.9, 52.8, 51.2, 54.1, 52.6]

# Fase 1. Risultati per batteria
print('')
print("RISULTATI BATTERIE")
print('')
print("="*50)

def stampa_risultati (batteria, tempi):
    for i, value in enumerate(batteria, 1):
        print(f"Corsia {i} | {value} - {tempi[i-1]}")

stampa_risultati(batteria_A_nomi, batteria_A_tempi)
print('')
print("="*50)
print('')
stampa_risultati(batteria_B_nomi, batteria_B_tempi)


# Fase 2. Confronto corsia per corsia
vinte_a = 0
vinte_b = 0
num_corsia = 0
margini = []
for corsia_a, tempo_a, corsia_b, tempo_b in zip(batteria_A_nomi, batteria_A_tempi, batteria_B_nomi, batteria_B_tempi):
    diff_ass = abs(tempo_a -tempo_b)
    margini.append(diff_ass)
    num_corsia += 1
    if tempo_a < tempo_b:
        vinte_a += 1
        differenza = round(tempo_b - tempo_a, 2)
        print(f"Corsia {num_corsia} - {corsia_a} vince su {corsia_b} di {differenza}s")
    elif tempo_b < tempo_a:
        vinte_b += 1
        differenza = round(tempo_a - tempo_b, 2)
        print(f"Corsia {num_corsia} - {corsia_b} vince su {corsia_a} di {differenza}s")

print('')



def corsia_vincente(vinte_a, vinte_b):
    corsia_top = ""
    if vinte_a > vinte_b:
        corsia_top = "A"
    elif vinte_b > vinte_a:
        corsia_top = "B"
    return corsia_top

vittorie_top = max(vinte_a, vinte_b)
corsia_migliore = corsia_vincente(vinte_a, vinte_b)

def margin_min(margini):
    marg_min = margini[0]
    indice_min = 0
    for i, m in enumerate(margini):
        if m < marg_min:
            marg_min = m
            indice_min = i
    return marg_min, indice_min

def margin_max(margini):
    marg_max = margini [0]
    for m in margini:
        if m > marg_max:
            marg_max = m
    return marg_max

marg_min, indice = margin_min(margini)

print('='*50)
print('')

print(f"Corsia più vincente: {corsia_migliore} con {vittorie_top} gare vinte su 5.")
print('')
print('='*50)
print('')
print(f"Corsia più combattuta: {indice+1} con margine di {marg_min}")
print('')


# Fase 3. Classifica finale unificata e media.

lista_nomi = batteria_A_nomi + batteria_B_nomi
lista_tempi = batteria_A_tempi + batteria_B_tempi

def classifica(lista_nomi, lista_tempi):
    classifica_finale = []
    for nome, tempo in zip(lista_nomi, lista_tempi):
        classifica_finale.append([nome, tempo])
    classifica_ordinata = sorted(classifica_finale, key= lambda x:x[1])
    return classifica_ordinata

classifica_ordinata = classifica(lista_nomi, lista_tempi)

print("---- CLASSIFICA FINALE ----")
print('')

for i, value in enumerate(classifica_ordinata, 1):
    print(f"{i}. {value[0]}")

def media_batterie(tempi):
    somma = 0
    for t in tempi:
        somma += t
    media = somma / len(tempi)
    return media

media_a = round(media_batterie(batteria_A_tempi),2)
media_b = round(media_batterie(batteria_B_tempi), 2)

print('')
print('='*50)
print('')
print("---- MEDIA PIÙ BASSA ----")
if media_a < media_b:
    print(f"Batteria A ha la media più bassa a {media_a}")
elif media_b < media_a:
    print(f"Batteria B ha la media più bassa a {media_b}")
print('')
