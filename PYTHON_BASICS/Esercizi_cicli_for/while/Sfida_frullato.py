# Passiamo all'esercizio del frullato. Qui impariamo a usare le liste come "contenitori" che riempiamo dinamicamente durante un ciclo.

dispensa = ["mela", "banana", "zenzero", "carota", "ghiaccio"]

frullato = []

for ingrediente in dispensa:
    if ingrediente.startswith("z"):
        print(f"Scarta {ingrediente}")
    else:
        frullato.append(ingrediente)
        print (f"{ingrediente} aggiunto al frullato")

print (frullato)