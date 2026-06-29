# Un bibliotecario gestisce uno scaffale fisico con capacità limitata. 
# Ogni libro è identificato da titolo e autore. 
# Lo scaffale deve gestire aggiunte, rimozioni e ricerche, rispettando sempre il limite di posti disponibili.


class Scaffale:

    def __init__(self, nome, max_libri):
        self.nome = nome
        self.max_libri = max_libri
        self.libri = []

    def aggiungi(self, titolo, autore):
        if len(self.libri) >= self.max_libri:
            print("Errore")
            return
        elif [titolo, autore] in self.libri:
            print("Errore")
            return "Errore"
        self.libri.append([titolo, autore])

    def posti_liberi(self):
        return self.max_libri - len(self.libri)
    
    def rimuovi(self, titolo):
        for i, tit in enumerate(self.libri):
            if tit[0] == titolo:
                self.libri.pop(i)
                return
        print("Titolo non trovato!")

    def cerca(self, query):
        lista_pers = []
        for tit, aut in self.libri:
            if query.lower() in tit.lower() or query.lower() in aut.lower():
                lista_pers.append([tit, aut])
        if not lista_pers:
            return "Nessun risultato"
        return lista_pers
        

    def mostra(self):
        print(f"Nome: {self.nome}")
        print(f"Posti liberi: {self.posti_liberi()}")
        print("Elenco libri:")
        print()
        for i, libri in enumerate(self.libri, 1 ):
            print(f"{i}. {libri[0]} {libri[1]}")

    
    # Test

scaffale1 = Scaffale("Narrativa", 4)

scaffale1.aggiungi("Avventure di a", "a")
scaffale1.aggiungi("Avventure di b", "b")
scaffale1.aggiungi("Avventure di c", "c")       
scaffale1.aggiungi("Avventure di d", "d")
scaffale1.aggiungi("Avventure di e", "e") # OLTRE CAPIENZA SCAFFALE
scaffale1.aggiungi("Avventure di d", "d") # DUPLICATO
scaffale1.rimuovi("Avventure di a")
scaffale1.cerca("b")
print()
print()

scaffale1.mostra()