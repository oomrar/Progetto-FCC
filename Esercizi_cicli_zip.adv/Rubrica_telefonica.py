# Gestisci una rubrica telefonica personale. 
# Le operazioni fondamentali — leggere un valore per chiave, aggiungere nuovi contatti, aggiornarne uno esistente e rimuoverlo — modelleranno la quasi totalità delle interazioni reali con questa struttura dati.

rubrica = {
    "Alice":   "333-1122334",
    "Bruno":   "347-5566778",
    "Carla":   "320-9988776",
    "Diego":   "366-4433221",
    "Elena":   "391-7766554"
}

# Fase 1. Lettura e accesso

print(f"Numero di Carla: {rubrica["Carla"]}")
numero_luca = rubrica.get("Luca", "CONTATTO NON TROVATO")
print(numero_luca)

# Fase 2. Aggiungere, modificare, rimuovere

rubrica.update({"Fabio": "333-832-6857"})
print("RUBRICA CON AGGIUNTA")
print(rubrica)

rubrica.update({"Bruno": "345-3829374"})
print("RUBRICA CON MODIFICA")
print(rubrica)

del rubrica["Diego"]
print("RUBRICA CON RIMOZIONE")
print(rubrica)


# Fase 3. Verifica preventiva con in

def verifica_contatto(nome_cercato, rubrica):
    if nome_cercato in rubrica:
        print(f"Contatto trovato! Il numero di {nome_cercato} è {rubrica[nome_cercato]}")
    else:
        rubrica[nome_cercato] = "---"
        print(f"Il contatto '{nome_cercato}' non è presente in rubrica. È stato aggiunto con il numero '---'.")



nome_cercato = "Bruno"
verifica_contatto(nome_cercato, rubrica)

           