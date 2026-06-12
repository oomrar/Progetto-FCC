# Programmazione ad oggetti: EREDITARIETÀ.
# Modella una gerarchia di animali. 
# La classe base definisce le caratteristiche comuni; ogni sottoclasse aggiunge comportamenti specifici e può ridefinire quelli ereditati.


print()

class Animale:

    def __init__(self, nome, eta, peso):
        self.nome = nome
        self.eta = eta
        self.peso = peso

    def mangia(self, cibo):
        print(f"{self.nome} ha mangiato {cibo}")

    def dormi(self):
        print(f"{self.nome} sta dormendo")

    def descrizione(self):
        print(f"Nome: {self.nome}\nEtà: {self.eta}\nPeso: {self.peso}")


class Cane(Animale):

    def __init__(self, nome, eta, peso, razza):
        super().__init__(nome, eta, peso)
        self.razza = razza

    def mangia(self, cibo):
        print(f"{self.nome}, il cane di razza {self.razza}, sgranocchia felice {cibo}")

    def abbaia (self):
        print(f"{self.nome} dice wof wof!")

    def porta_la_palla(self):
        print(f"{self.nome} porta la palla!")


class Gatto(Animale):

    def __init__(self, nome, eta, peso, indoor):
        super().__init__(nome, eta, peso)
        self.indoor = indoor
    
    def dormi(self):
        print(f"Il gatto {self.nome} sta dormendo beato")

    def miagola(self):
        print("Il gatto sta miagolando")

    def fa_le_fusa(self):
        print("Il gatto fa le fusa")


cane1 = Cane("Lucio", 5, 8, "Golden")
gatto1 = Gatto("Arturo", 6, 10, True)
cane2 = Cane("Sasso", 7, 4, "Chiwawa")
gatto2= Gatto("Bob", 3, 5, False)



animali = [cane1, gatto1, cane2, gatto2]

for animale in animali:
    animale.descrizione()
    animale.mangia("Croccantini")
    if isinstance(animale, Cane):
        animale.abbaia()
        animale.porta_la_palla()
    elif isinstance(animale, Gatto):
        animale.miagola()
        animale.fa_le_fusa()
    print()

print()


    