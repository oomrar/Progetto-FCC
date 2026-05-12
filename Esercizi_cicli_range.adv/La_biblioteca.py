# Lavori in una piccola biblioteca e devi stampare il catalogo dei libri disponibili, poi separare quelli con titoli più lunghi per una vetrina speciale.

# Dati
libri = ["Dune", "Neuromante", "Fondazione", "1984", "Hyperion", "Io Robot", "Solaris"]


vetrina = []

for titolo in libri:
    print (f"📖 {titolo}")
    if len(titolo) > 5:
        vetrina.append(titolo)
        
print (len(libri))
print (f"Libri in vetrina: {len(vetrina)}")
print (vetrina[0])
print (vetrina[-1])
