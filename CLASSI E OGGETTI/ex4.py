# Creare una classe Impiegato che abbia gli attributi “nome”, “cognome”, “matricola” e “stipendio”. 
# Aggiungere un metodo “aumenta_stipendio” che aumenti lo stipendio dell’impiegato del 10% e un metodo “stampa_dettagli” che stampi tutti i dettagli dell’impiegato, ad esempio “Impiegato: Marco Rossi, matricola 12345, stipendio: 3000 Euro”.

class Impiegato:
    def __init__(self, nome, cognome, matricola, stipendio):
        self.nome = nome
        self.cognome = cognome
        self.matricola = matricola
        self.stipendio = stipendio

    def aumenta_stipendio(self):
        self.stipendio *= 1.1
        print("Stipendio aumentato!")
    
    def stampa_dettagli(self):
        print(f"Impiegato: {self.nome} {self.cognome}, matricola {self.matricola}, stipendio: {round(self.stipendio, 2)} Euro. ")

impiegato1 = Impiegato("Marco", "Rossi", 12345, 3000)

impiegato1.stampa_dettagli()
impiegato1.aumenta_stipendio()
impiegato1.stampa_dettagli()
