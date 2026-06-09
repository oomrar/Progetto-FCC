# Creare una classe Persona che abbia i seguenti attributi: nome, età, sesso. 
# Aggiungi un metodo “presentati” che stampi una frase di presentazione della persona, ad esempio “Ciao, mi chiamo Marco e ho 32 anni”.

class Persona:

    def __init__(self, nome, eta, sesso): # Costruttore
        self.nome = nome
        self.eta = eta
        self.sesso = sesso

    def presentati(self): # Funzione metodo
        print (f"Ciao, mi chiamo {self.nome} e ho {self.eta} anni.")

persona1 = Persona("Marco", 32, "M")
persona2 = Persona("Sofia", 70, "M")

persona1.presentati()
persona2.presentati() # Cosi stampo il metodo, oppure se ho impostato return nella funzione devo scrivere print qui.
print(persona1.nome) # Cosi stampo un attributo