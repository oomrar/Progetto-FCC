# La mensa ha un menù settimanale ma alcuni piatti sono stati segnalati come non disponibili oggi. 
# Devi aggiornare il menù e produrre alcune statistiche.

# Dati
menu = ["pasta", "pizza", "insalata", "pizza", "minestra", "pasta", "frutta", "pizza"]
non_disponibili = ["pizza"]

for piatto in menu:
    if piatto in non_disponibili:
        print(f"{piatto} non disponibile oggi.")
    else:
        print(piatto)

print(f"Pasta c'è {menu.count("pasta")} volte")

for piatto in non_disponibili:
    while piatto in menu:
        menu.remove(piatto)
        print (menu)

print (f"{menu}\n{len(menu)}")