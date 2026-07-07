# Una scheda anagrafica ha nome, cognome ed età. 
# Il nome deve essere una stringa non vuota; l'età deve essere un intero tra 0 e 130. 
# Il codice fiscale, una volta assegnato, non deve poter essere modificato dall'esterno: è un attributo in sola lettura dopo la creazione.

print()

class Persona:

    def __init__(self, nome, cognome, eta, codice_fiscale):
        self.nome = nome
        self._cognome = cognome
        self.eta = eta
        self._codice_fiscale = codice_fiscale

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, new_name):
        if not new_name or not isinstance(new_name, str):
            raise ValueError("Nome non valido")
        self._nome = new_name

    @property
    def eta(self):
        return self._eta 
    
    @eta.setter
    def eta(self, new_eta):
        if not isinstance(new_eta, int):
            raise TypeError("L'età deve essere un numero intero")
        if not (0 <= new_eta <= 130):
            raise ValueError("Età non valida")
        self._eta = new_eta

    @property
    def codice_fiscale(self):
        return self._codice_fiscale
    
    @property
    def nome_completo(self):
        return self._nome + " " + self._cognome
    
    @property
    def is_maggiorenne(self):
        return self._eta >= 18
            
        

persona1 = Persona("Omar", "Houssa", 13, "HSSMRO03D24E463Z")
# persona2 = Persona("", "Houssa", "13", "HSSMRO03D24E463Z") Istanza sbagliata per verifica test

print()

# Test fase 1
print(persona1.nome)
print(persona1.eta)
persona1.eta = 23
print(f"Età modificata: {persona1.eta}")

# Test fase 2 
print(persona1.codice_fiscale)
# persona1.codice_fiscale = "HSSMRTIEOFGNIE23" Test per l'attribute error

# Test fase 3
print(persona1.nome_completo)
print(persona1.is_maggiorenne)
persona1.nome = "Dario"
print(f"Test se il nome completo cambia: {persona1.nome_completo}")

print()
