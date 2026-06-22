# Una scheda personale ha alcuni campi obbligatori (nome, cognome) e molti opzionali (telefono, indirizzo, note, sito_web, data_nascita…). 
# Le funzioni hasattr() e getattr() permettono di interrogare la scheda senza sapere in anticipo quali campi opzionali sono stati compilati.

campi_obbligatori  = ["nome", "cognome", "email"]
campi_opzionali    = ["telefono", "indirizzo", "citta", "data_nascita",
                      "sito_web", "note"]
campi_da_stampare  = campi_obbligatori + campi_opzionali

class SchedaPersonale:

    def __init__(self, nome, cognome, email):
        self.nome = nome
        self.cognome = cognome
        self.email = email

    def aggiungi_campo(self, nome_campo, valore):
        setattr(self, nome_campo, valore)
    
    def to_stringa(self):
        righe = []
        for campo in campi_da_stampare:
            valore = getattr(self, campo, None)
            if valore is not None:
                righe.append(f"{campo.capitalize()}: {valore}")
        return "\n".join(righe)
    
    
# TEST FASE 1
print()    
profilo = SchedaPersonale("Omar", "Houssa", "omarhoussa.oh@gmail.com")
profilo.aggiungi_campo("telefono", "3713017958")
print(profilo.__dict__)
print()



# TEST FASE 2

scheda_completa = SchedaPersonale("Omar", "Houssa", "omarhoussa.oh@gmail.com")
scheda_parziale = SchedaPersonale("Omar", "Houssa", "omarhoussa.oh@gmail.com")
scheda_completa.aggiungi_campo("telefono", "371301758")


print()
print("TEST SCHEDA PARZIALE")
for campo in campi_da_stampare:
    if hasattr(scheda_parziale, campo):
        print(f"Campo {campo} presente nella scheda parziale")
    else:
        print(f"Campo {campo} assente.")

print()
print("TEST SCHEDA COMPLETA")
for campo in campi_da_stampare:
    if hasattr(scheda_completa, campo):
        print(f"Campo {campo} presente nella scheda parziale")
    else:
        print(f"Campo {campo} assente.")
print()

