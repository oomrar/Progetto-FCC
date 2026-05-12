# Gestisci i risultati di una gara di atletica. Hai i nomi degli atleti e i loro tempi in secondi. 
# Devi costruire classifiche, trovare posizioni e simulare squalifiche senza alterare i dati originali.

atleti = ["Marco", "Sara", "Luca", "Anna", "Pietro", "Giulia", "Davide"]
tempi  = [58.3, 55.1, 61.7, 54.8, 57.2, 59.6, 56.4]
# tempi[i] corrisponde all'atleta atleti[i]


# Fase 1. Stampa classifica

def stampa_ordine_arrivo(atleti):
    for i, value in enumerate(atleti, 1):
        print(f"{i}° {value}")
print("Lista non ordinata:")
stampa_ordine_arrivo(atleti)
print("*"*50)
print("*"*50)

def classifica_per_tempo(atleti, tempi):
    coppie = []
    for i, value in enumerate(atleti):
        coppie.append([value, tempi[i]])
    classifica_ordinata = sorted(coppie, key=lambda x:x[1])
    return classifica_ordinata
print("Classifica per tempo:")
print(classifica_per_tempo(atleti, tempi))
print("*"*50)
print("*"*50)

# classifica_ordinata = [[Nome, tempo],[Nome, tempo],[Nome, tempo],[Nome, tempo]]

# Fase 2. Ricerca e selezione.

def posizione_in_classifica(atleti, tempi, nome):
    classifica = classifica_per_tempo(atleti, tempi)
   
    for i,value in enumerate(classifica, 1):
        if value[0] == nome:                    # value[0] è il primo elemento della lista, quindi il nome.
            return i
    return -1

nome = "Davide"
print(f"Posizione del candidato {nome}")
print(posizione_in_classifica(atleti, tempi, nome))
print("*"*50)
print("*"*50)

def podio(atleti, tempi):
    classifica = classifica_per_tempo(atleti, tempi)
    estrazione_podio = classifica[:3]
    for i, value in enumerate(estrazione_podio, 1):
        print (f"{i}. {value}")


print("Podio:")
podio(atleti, tempi)
print("*"*50)
print("*"*50)

# Fase 3. Simulazione con copy()

def simula_squalificati (atleti, tempi, nome):
    copia_atleti = atleti.copy()
    copia_tempi = tempi.copy()
    indice = 0
    for i, value in enumerate(copia_atleti):
        if value == nome:
            indice = i
    copia_atleti.pop(indice)
    copia_tempi.pop(indice)
    print(copia_atleti)
    print(atleti)


simula_squalificati(atleti, tempi, nome)



