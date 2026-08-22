# In questo laboratorio risolverai il rompicapo matematico noto come torre di Hanoi. Il rompicapo consiste in tre aste e un numero di dischi di diametri diversi.
# Il rompicapo inizia con i dischi impilati sulla prima asta, in ordine decrescente di dimensione, con il disco più piccolo in cima e il disco più grande in fondo.
# L'obiettivo del rompicapo della torre di Hanoi è spostare tutti i dischi sull'ultima asta.


def hanoi_solver(n):
    asta_1 = []
    asta_2 = []
    asta_3 = []
    for num in range(n, 0, -1):
        asta_1.append(num)
    mosse = []
    mosse.append(f"{asta_1} {asta_2} {asta_3}")
    
    def muovi(k, origine, destinazione, ausiliaria):
        if k == 0:
            return
        muovi(k-1, origine, ausiliaria, destinazione)

        disco = origine.pop()
        destinazione.append(disco)
        mosse.append(f"{asta_1} {asta_3} {asta_2}")

        muovi(k-1, ausiliaria, destinazione, origine)
    
    muovi(n, asta_1, asta_2, asta_3)
    

    return '\n'.join(mosse)
        
    

print(hanoi_solver(4))