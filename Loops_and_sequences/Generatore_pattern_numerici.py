#App che genera pattern numerici, in questo caso una sequenza di numeri da 1 a n, dove n è un numero intero positivo passato come argomento alla funzione.

def number_pattern (n):

    #Controllo se l'argomento è un intero e se è maggiore di 0, altrimenti restituisco un messaggio di errore.
    if not isinstance(n, int):
        return "Argument must be an integer value."
    if n < 1:
        return "Argument must be an integer greater than 0."
    
#Se l'argomento è valido, genero la sequenza di numeri da 1 a n e la restituisco come stringa.
    risultato=""
    for variable in range(1, n+1):
        risultato += str(variable) + " "
    
 #Rimuovo l'ultimo spazio (strip) e restituisco la stringa con la sequenza di numeri.   
    return risultato.strip()

print (number_pattern(3))

#Finish

