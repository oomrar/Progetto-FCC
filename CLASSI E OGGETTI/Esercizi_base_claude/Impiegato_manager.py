# Un'azienda tiene traccia di quanti impiegati ha assunto in totale. 
# Ogni impiegato ha uno stipendio e appartiene a un reparto. 
# I manager estendono gli impiegati e possono gestire un team di persone.


print()

class Impiegato:

    numero_impiegati = 0

    def __init__(self, nome, reparto, stipendio):
        self.nome = nome
        self.reparto = reparto
        self.stipendio = stipendio
        Impiegato.numero_impiegati += 1
    
    @classmethod  
    def quanti_impiegati(cls):
        print(f"Numero di impiegati: {cls.numero_impiegati}")
    
    def aumento(self, percentuale):
        self.stipendio += self.stipendio * percentuale

class Manager(Impiegato):
    def __init__(self, nome, reparto, stipendio, budget_team):
        super().__init__(nome, reparto, stipendio)
        self.budget_team = budget_team
        self.team = []

    def costo_team(self):
        somma = 0
        for impiegato in self.team:
            somma += impiegato.stipendio
        return somma
    
    def aggiungi_al_team(self, impiegato):
        for imp in self.team:
            if impiegato == imp:
                print(f"Impiegato {impiegato.nome} già presente nel team")
                print()
                break
        else:
            if (impiegato.stipendio + self.costo_team()) > self.budget_team:
                print("Impossibile proseguire con l'aggiunta, budget superato!")
                print()
                return
            self.team.append(impiegato)

    
    def stampa_team(self):
            print()
            print(f"--- TEAM DI {self.nome.upper()} ---")
            print()
            if not self.team:
                print("Il team è vuoto.")
                print()
            else:
                for impiegato in self.team:
                    print(f"- Nome: {impiegato.nome} | Reparto: {impiegato.reparto} | Stipendio: {impiegato.stipendio}€")
                    print()
    
# Fase di testing

imp1 = Impiegato("Luigi", "Ortofrutta", 1500)
imp2 = Impiegato("Andrea", "Controllo qualità", 2300)
imp3 = Impiegato("Sandro", "Controllo qualità", 1200)
imp4 = Impiegato("Elisa", "Ortofrutta", 1200)
imp5 = Impiegato("Paolo", "Controllo qualità", 1700)

man1 = Manager("Luca", "Ortofrutta", 3000, 5500)
man2 = Manager("Silvio", "Controllo qualità", 3300, 5000)

man1.aggiungi_al_team(imp1)
man1.aggiungi_al_team(imp1)
man1.aggiungi_al_team(imp4)

man2.aggiungi_al_team(imp2)
man2.aggiungi_al_team(imp3)
man2.aggiungi_al_team(imp5)


man1.stampa_team()
print()
man2.stampa_team()
print()
Impiegato.quanti_impiegati()
print()
