# Immagina di dover gestire la cantina di un ristorante. Hai una lista di prezzi di diverse bottiglie di vino e vuoi sapere
# quali puoi permetterti con il tuo budget.

prezzi_vini = [12.5, 15.8, 18, 23.5, 65]

def filtra_prezzi (lista_prezzi, budget_massimo):
    contatore = 0

    for prezzo in lista_prezzi:
        if prezzo <= budget_massimo:
            print(f"Puoi comprare la bottiglia da {prezzo}")
            contatore += 1
            budget_massimo -= prezzo
        else:
            print (f"Non puoi comprare la bottiglia da {prezzo}")

    return contatore
        
numero_bottiglie = filtra_prezzi(prezzi_vini, 40)

print(f"Puoi comprare {numero_bottiglie} bottiglie")