# Modella una persona con le sue informazioni anagrafiche di base. 
# Questo primo esercizio ha un solo obiettivo: capire come si definisce una classe, cosa fa __init__, come si creano istanze e come si chiamano i metodi su di esse.

print()

class Persona:
    def __init__(self, nome, cognome, eta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta

    def presentati(self):
        print(f"Ciao io sono {self.nome} {self.cognome} e ho {self.eta}.")

    def nome_completo(self):
        return f"{self.nome} {self.cognome}"

    def is_adulto(self):
        if self.eta >= 18:
            return True
        else: 
            return False
    
    def compleanno(self):
        self.eta +=1


p1 = Persona("Alice", "Rossi", 30)
p2 = Persona("Bruno", "Verdi", 25)

print("PERSONA 1:")
print(p1.nome)
print(p1.cognome)
print(p1.eta)

print()

print("PERSONA 2:")
print(p2.nome)
print(p2.cognome)
print(p2.eta)

print()

p1.presentati()
p2.presentati()

print()

print(p1.nome_completo())
print(p2.nome_completo())

print()

print(p1.is_adulto())
print(p2.is_adulto())

print()

print(f"Età prima della funzione: {p1.eta}")
p1.compleanno()
p1.compleanno()
p1.compleanno()
print(f"Età dopo la funzione: {p1.eta}")



