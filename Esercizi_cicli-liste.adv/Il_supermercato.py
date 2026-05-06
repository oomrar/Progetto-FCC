# Sei il sistema gestionale di un supermercato. Hai i prodotti in magazzino, i movimenti di vendita della settimana (7 giorni) e un listino prezzi. Devi gestire le scorte, calcolare i ricavi, trovare i prodotti critici e produrre il report settimanale.

prodotti   = ["Pasta", "Riso", "Olio", "Farina", "Zucchero", "Sale", "Pomodori"]
prezzi     = [1.29, 1.10, 3.89, 0.95, 1.20, 0.49, 2.30]
scorte     = [80, 45, 30, 60, 55, 100, 40]

vendite_settimana = [
    # Pa  Ri  Ol  Fa  Zu  Sa  Po
    [12, 8,  5,  10, 6,  2,  9],
    [5,  3,  7,  4,  8,  1,  6],
    [3,  6,  2,  8,  4,  3,  5],
    [10, 4,  6,  7,  5,  2,  8],
    [8,  5,  4,  9,  7,  1,  6],
    [6,  2,  3,  5,  4,  0,  7],
    [9,  7,  8,  6,  5,  3,  4],
]

soglia_riordino = 20

# Fase 1: Vendite totali per prodotto

# La variabile i indica i prodotti
# La variabile j indica i giorni della settimana

# Quindi il ciclo esterro scorre i prodotti, il ciclo interno scorre i giorni della settimana.
# Prima vengono sondati tutti i giorni della settimana (j) per ogni singolo prodotto (i) e la somma delle vendite di ogni giorno (j) aggiunta alla lista vendite_totali.


def calcola_vendite_totali(vendite_settimana):
    vendite_totali = []
    for i in range(len(prodotti)):
        totali_giornalieri = 0
        for j in range(len(vendite_settimana)):
            totali_giornalieri += vendite_settimana[j][i]
        vendite_totali.append(totali_giornalieri)
    return vendite_totali

vendite_totali = calcola_vendite_totali(vendite_settimana)

for i in range(len(prodotti)):
    print(f"{prodotti[i]} | {vendite_totali[i]} unità vendute")


