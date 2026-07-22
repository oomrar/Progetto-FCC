# Una classe gestisce le credenziali di un utente. 
# La password ha regole di complessità che vengono verificate nel setter; internamente viene salvata in chiaro (semplificazione), ma il getter la restituisce mascherata. Viene anche tracciato quante volte la password è stata cambiata.

print()

class Utente:

    def __init__(self, username, password):
        self.username = username
        self._n_cambi = 0
        self.password = password
        

    @property
    def password(self):
        return self._password[:2] + "*" * (len(self._password) -4) + self._password[-2:]

    @property
    def cambi(self):
        return self._n_cambi
    
    @password.setter
    def password(self, new_password):
        if not len(new_password)>= 8:
            raise ValueError("La password deve contenere almeno 8 caratteri")
        if not any(c.isupper() for c in new_password):
            raise ValueError("Almeno una lettera deve essere maiuscola")
        if not any(c.islower() for c in new_password):
            raise ValueError("Almeno una lettera deve essere minuscola")
        if not any(c.isdigit() for c in new_password):
            raise ValueError("La password deve contenere almeno un numero")
        self._password = new_password
        self._n_cambi += 1

    def verifica(self, tentativo):
        return tentativo == self._password
    
    @property
    def is_forte(self):
        return len(self._password) >= 12
            


