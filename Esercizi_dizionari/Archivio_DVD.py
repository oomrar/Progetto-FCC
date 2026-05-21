# Gestisci un archivio di DVD da noleggiare. 
# Una coda di clienti aspetta di ricevere i propri film; devi processarla svuotandola progressivamente, poi azzerare il catalogo e ricostruirlo a partire da due liste di nuovi titoli.


catalogo = {
    "Inception":    2010,
    "Interstellar": 2014,
    "The Matrix":   1999,
    "Dune":         2021,
    "Blade Runner": 1982,
}
coda_noleggio = {
    "Mario Rossi":   "Inception",
    "Lucia Bianchi": "Dune",
    "Piero Verdi":   "The Matrix",
}
titoli_nuovi = ["Oppenheimer", "Poor Things", "Past Lives", "All Quiet on the Western Front"]
anni_uscita  = [2023, 2023, 2022, 2022]

print('')
while len(coda_noleggio) > 0:
    nome_cliente, titolo_film = coda_noleggio.popitem()
    print(f"DVD {titolo_film} consegnato a {nome_cliente}")

print(coda_noleggio)
print('')

catalogo.clear()
print(catalogo)

print('')
catalogo = dict(zip(titoli_nuovi, anni_uscita))
print(catalogo)
print('')


titoli_vecchi = ["Inception", "Interstellar", "The Matrix", "Dune", "Blade Runner"]
anni_vecchi = [2010, 2014, 1999, 2021, 1982]

catalogo_ripristinato = dict(zip(titoli_vecchi, anni_vecchi))
catalogo_ripristinato.update(catalogo)


for film,anno in sorted(catalogo_ripristinato.items(), key = lambda x: x[1]):
    print(f"{film} | {anno}")