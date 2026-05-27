# Sei all'ingresso di una palestra. Hai una lista di soci autorizzati: soci_iscritti = ["mario", "luca", "anna", "paola"].
# Vuoi registrare chi entra oggi finché non decidi di chiudere il turno.

soci_iscritti = ["mario", "luca", "anna", "paola"]
entrati_oggi = []

while True:
    nome_utente = input ("Inserire nome utente: ")
    if nome_utente == "stop":
        break
    else:
        if nome_utente.lower() in soci_iscritti:
            entrati_oggi.append(nome_utente.lower())
        else:
            print("Spiacente non risulti fra i soci iscritti")

print(f"Persone entrate oggi: {entrati_oggi}")