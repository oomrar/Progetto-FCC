# Una playlist musicale deve comportarsi il più possibile come una collezione Python nativa: si deve poter misurare con len(), cercare con in e scorrere con for. 
# I brani sono semplici stringhe nel formato "Artista - Titolo".

print()

class Playlist:

    def __init__(self, nome):
        self.nome = nome
        self.brani = []

    def aggiungi(self, brano):
        self.brani.append(brano)
    
    def rimuovi(self, brano):
        self.brani.remove(brano)
    
    def __str__(self):
        frase = f"Nome playlist: {self.nome}\n"
        for i, brano in enumerate(self.brani, 1):
            frase += f"{i}. {brano}\n"
        return frase
    
    def __len__(self):
        return len(self.brani)

    def __contains__(self, brano):
        condizione = brano in self.brani
        return condizione

    def is_vuota(self):
        return len(self) == 0
    
    def __iter__(self):
        return iter(self.brani)



# Test fase 1.
playlist = Playlist("Rock playlist")
playlist.aggiungi("Money - Gruppo a caso")
playlist.aggiungi("Sands")
playlist.rimuovi("Sands")

print(playlist)


# Test fase 2.
playlist.aggiungi("Queen - Bohemian Rhapsody")
print(len(playlist))
print("Queen - Bohemian Rhapsody" in playlist)
print(playlist.is_vuota())
print()

# Test fase 3.
for brano in playlist:
    print(brano)

print()
