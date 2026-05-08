# Sei un tecnico che elabora i dati di una stazione meteo. 
# Hai le temperature rilevate ogni 6 ore per 7 giorni (4 rilevazioni al giorno).

giorni = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica"]
temperature = [
    [12, 18, 21, 15],
    [10, 15, 19, 13],
    [8,  11, 14, 9 ],
    [14, 22, 25, 18],
    [16, 24, 27, 20],
    [13, 20, 23, 17],
    [9,  13, 16, 11]
]

# 1. Analisi giornaliera

def escursione_termica (lista_temperature):
    indice_min = 0
    indice_max = 0
    for i in range(len(lista_temperature)):
        if lista_temperature[i] < lista_temperature [indice_min]:
            indice_min = i
        elif lista_temperature [i] > lista_temperature [indice_max]:
            indice_max = i
        
    escursione = lista_temperature[indice_max] - lista_temperature[indice_min]
    temp_min = lista_temperature [indice_min]
    temp_max = lista_temperature [indice_max]

    return escursione, temp_min, temp_max

def escursione_termica (lista_temperature):
    temp_min = lista_temperature[0]
    temp_max = lista_temperature [0]
    for t in lista_temperature:
        if t < temp_min:
            temp_min = t
        elif t > temp_max:
            temp_max = t
    escursione = temp_max - temp_min
    return escursione, temp_max, temp_min


def riepilogo_settimana(giorni, temperature):
    for i in range(len(giorni)):
        escursione, temp_max, temp_min = escursione_termica(temperature[i])
        print(f"Giorno {i+1}: {giorni[i]} | {temp_max}, {temp_min} | Escursione termica: {escursione}")


# 2. Ricerca e selezione
def giorni_sopra_soglia (giorni, temperature, soglia):
    giorni_sopra = []
    for i in range(len(giorni)):
        for t in temperature[i]:
            if t > soglia:
                giorni_sopra.append(giorni[i])
                break
    return giorni_sopra

soglia = 20
giorni_sopra_soglia = giorni_sopra_soglia(giorni, temperature, soglia)

orari = ["00:00", "06:00", "12:00", "18:00"]

def ore_fredde (orari, temperature):
    contatore_ore = [0, 0, 0, 0]
    for i in range(len(temperature)):
        for j in range (len(temperature[i])):
            if temperature[i][j] < 12:
                contatore_ore [j] += 1
    orario = 0
    for i in range(len(contatore_ore)):
        if contatore_ore[i] > orario:
            orario = i
    
    orario_magg = orari[orario]
    return orario_magg
ore_fredde = ore_fredde(orari, temperature)

# 3. Trasformazione dati

def converti_farhrenheit (temperature):
    temp_conv = [

    ]
    for i in range(len(temperature)):
        riga_giornaliera = []

        for t in temperature[i]:
            valore_f = t * 9/5 +32
            riga_giornaliera.append(valore_f)
        
        temp_conv.append(riga_giornaliera)

    return temp_conv
temperature_convertite = converti_farhrenheit(temperature)

def inserisci_giorno (nome, lista_temperature, giorni, temperature):
    giorni.insert(1, nome)
    temperature.insert(1, lista_temperature)
    
lista_temperature = [14,15,15,15]
nome = "MIO"

print( " ----- SETTIMANA AGGIORNATA -----")
inserisci_giorno (nome,lista_temperature, giorni, temperature)
riepilogo_settimana(giorni, temperature)

print(temperature_convertite)
print("-"* 50)
print(ore_fredde)
print("-"* 50)
print(giorni_sopra_soglia)


    




                

