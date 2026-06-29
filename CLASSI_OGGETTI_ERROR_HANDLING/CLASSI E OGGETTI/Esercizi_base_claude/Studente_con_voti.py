# Modella uno studente universitario che accumula voti nel tempo. 
# La lista dei voti cresce ad ogni esame superato. 
# I metodi devono calcolare statistiche sulla lista e determinare lo stato accademico dello studente.

print()

class Studente:

    def __init__(self, nome, matricola):
        self.nome = nome
        self.matricola = matricola
        self.voti = []

    def aggiungi_voto(self, materia, voto):
        if voto >= 18 and voto <= 30:
            self.voti.append([materia, voto])
        else:
            print(f"Errore! Voto non valido per {materia}.")
    
    def media(self):
        media_aritmetica = 0
        totale_voti = 0
        if self.voti:
            for v in self.voti:
                totale_voti += v[1]
            media_aritmetica = totale_voti / len(self.voti)
            return media_aritmetica
        return 0
                

    def voto_massimo(self):
        if self.voti:
            voto_max = 0
            materia = ""
            for m, v in self.voti:
                if v > voto_max:
                    voto_max = v
                    materia = m
            return voto_max, materia
        return "Nessun voto presente"

    def voto_minimo(self):
        if self.voti:
            voto_min = self.voti[0][1]
            materia = self.voti[0][0]
            for m,v in self.voti:
                if v < voto_min:
                    voto_min = v
                    materia = m
            return voto_min, materia
        return "Nessun voto presente"

    def lode(self):
        for v in self.voti:
            if v[1] == 30:
                return True
        return False   
    
    def libretto(self):
        print("RIEPILOGO LIBRETTO")
        print()
        print(self.nome)
        print(self.matricola)
        print(len(self.voti))
        print()
        print("Lista voti:")
        for m, v in self.voti:
            print(f"Materia: {m} | Votazione: {v}")
        print()
        print(self.media())
        print(f"Lo studente ha lodi? {self.lode()}")

    def is_in_corso(self):
        condizione = len(self.voti) < 12
        return condizione
    
    def materia_migliore(self):
        if self.voti:
            voto, materia = self.voto_massimo()
            return materia
        return "Nessun esame sostenuto"
            
            

    

stud1 = Studente("Marco", "11/22")
stud2 = Studente("Sara", "45/32")

stud1.aggiungi_voto("Matematica", 27)
stud1.aggiungi_voto("Economia", 18)
stud1.aggiungi_voto("Statistica", 16)

stud2.aggiungi_voto("Matematica", 17)
stud2.aggiungi_voto("Economia", 21)
stud2.aggiungi_voto("Statistica", 30)
print()

print(f"Media studente 1: {stud1.media()}")
print(f"Media studente 2: {stud2.media()}")
print()

print(f"Voto max studente 1: {stud1.voto_massimo()}")
print(f"Voto max studente 2: {stud2.voto_massimo()}")
print()

print(f"Voto min studente 1: {stud1.voto_minimo()}")
print(f"Voto min studente 2: {stud2.voto_minimo()}")
print()

print(f"Sono presenti delle lodi per stud1? {stud1.lode()}")
print(f"Sono presenti delle lodi per stud2? {stud2.lode()}")
print()

stud1.libretto()
print(f"Lo studente è in corso? {stud1.is_in_corso()}")
print(f"Materia migliore studente 1: {stud1.materia_migliore()}")
print()
stud2.libretto()
print(f"Lo studente è in corso? {stud2.is_in_corso()}")
print(f"Materia migliore studente 2: {stud2.materia_migliore()}")



print()