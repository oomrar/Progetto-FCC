# Stai gestendo una lista della spesa. Alcune funzioni agiscono su tutti gli elementi, altre solo su quelli in posizioni specifiche. 
# Usi enumerate per distinguere gli elementi in base a dove si trovano nella lista.

spesa = [
    "pane", "latte", "uova", "pasta", "pomodori",
    "formaggio", "mele", "olio", "sale", "caffè"
]
acquistati = ["latte", "uova", "sale"]

nuovi = ["vino", "lattuga"]


#Fase 1. Visualizzazione per posizione

def stampa_spesa(spesa, acquistati):
    for i, value in enumerate(spesa, 1):
        if value in acquistati:
            frase1 = f"{i}. [✓] {value}"
            print(frase1)
        else:
            frase2 = f"{i}. [ ] {value}"
            print(frase2)

stampa_spesa(spesa, acquistati)

print('-'*50)
print('-'*50)

def prodotti_in_posizione_pari(spesa):
    lista_pari = []
    for i, value in enumerate(spesa):
        if i % 2 == 0:
            lista_pari.append(value)
    return lista_pari

print(prodotti_in_posizione_pari(spesa))

print('-'*50)
print('-'*50)


#Fase 2. Modifica della lista.

def rimuovi_acquistati(spesa, acquistati):
    for value in acquistati:
        if value in spesa:
            spesa.remove(value)
    for i, value in enumerate(spesa, 1):
        print(f"{i}. {value}")

rimuovi_acquistati(spesa, acquistati)

print('-'*50)
print('-'*50)

def aggiungi_prodotti(spesa, nuovi):
    spesa.extend(nuovi)
    for i, value in enumerate(spesa, 1):
        print(f"{i}. {value}")

aggiungi_prodotti(spesa, nuovi)

print('-'*50)
print('-'*50)


#Fase 3. Riepilogo

def riepilogo (spesa, acquistati):
    totale_articoli = len(spesa)
    spuntati = 0
    da_acquistare = 0
    prod_da_acquistare = []
    for i, value in enumerate(spesa, 1):
        if value in acquistati:
            spuntati += 1
        else:
            da_acquistare += 1
            prod_da_acquistare.append(value)

    print (f"Totale articoli: {totale_articoli}\nArticoli comprati: {spuntati}\nArticoli da acquistare: {da_acquistare}")
    ord_da_acquistare = sorted(prod_da_acquistare)
    print(ord_da_acquistare)

riepilogo(spesa, acquistati)
