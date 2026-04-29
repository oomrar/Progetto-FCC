#Vogliamo creare una funzione che controlli se una password è "valida" secondo alcuni criteri di base basati sui tipi di dati.

def valida_password (password):
    if len (password) >= 8:
        return True
    else:
        return False

password = input("Inserisci la password: ")

if valida_password (password):
    print ("Accesso consentito")
else:
    print("Password troppo corta")

