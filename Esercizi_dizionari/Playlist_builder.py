# Un'applicazione musicale conserva i dati delle canzoni in liste separate. 
# Il tuo compito è costruire progressivamente un catalogo dizionario, arricchirlo con informazioni aggiuntive provenienti da un secondo dizionario e rispondere a query che richiedono sia ricerche dirette che inverse.

titoli  = ["Bohemian Rhapsody","Hotel California","Smells Like Teen Spirit","Imagine","Purple Rain"]
artisti = ["Queen","Eagles","Nirvana","John Lennon","Prince"]
durate  = [354, 391, 301, 187, 520]   # durata in secondi

generi = {
    "Queen":       "Rock",
    "Eagles":      "Rock",
    "Nirvana":     "Grunge",
    "John Lennon": "Pop",
    "Prince":      "Funk",
}

# Fase 1. Costruzione catalogo.
print("")
catalogo = {}
for titolo, artista, durata in zip(titoli, artisti, durate):
    catalogo[titolo] = [artista, durata]

print("CATALOGO")
print("")
for titolo, info in catalogo.items():
    minuti = info[1] // 60
    secondi = info[1] % 60
    print (f"Canzone: {titolo} | Artista: {info[0]} | Durata: {minuti}m e {secondi}s")
print("")

print ('=============================================')
print("")


# Fase 2. Arricchire con un secondo dizionario

for titolo, info in catalogo.items():
    genere = generi.get(info[0], "Sconosciuto")
    info.append(genere)

print("CATALOGO AGGIORNATO")
print('')
print(catalogo)
print('')


print ('=============================================')
print("")


# Fase 3. Ricerca diretta e inversa
durata_max = 0
for info in catalogo.values():
    if info[1] > durata_max:
        durata_max = info[1]

titolo_durata_max = ""
for titolo, info in catalogo.items():
    if info[1] == durata_max:
        titolo_durata_max = titolo

print(f"Durata max: {durata_max // 60}m e {durata_max % 60}s | {titolo_durata_max}")
print("")

def lista_canzoni (catalogo, artista_cercato):
    lista_titoli = []
    for titolo, info in catalogo.items():
            if info[0] == artista_cercato:
                lista_titoli.append(titolo)
    return lista_titoli

artista_cercato = 'Queen'
print(f"Canzoni nel catalogo per {artista_cercato}:")
print(lista_canzoni(catalogo, artista_cercato))
print("")
