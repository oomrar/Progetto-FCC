#Gestore di configurazione utente

#Guida all'utente:
#1. Aggiungi una nuova impostazione: Per aggiungere una nuova impostazione.
# La funzione add_setting aggiunge una nuova impostazione al dizionario se la chiave non esiste già, altrimenti restituisce un messaggio di errore. 
# La funzione update_setting aggiorna il valore di un'impostazione esistente se la chiave esiste, altrimenti restituisce un messaggio di errore.
# La funzione delete_setting rimuove un'impostazione dal dizionario se la chiave esiste, altrimenti restituisce un messaggio di errore.
# Infine, view_settings restituisce una stringa che mostra tutte le impostazioni attuali se il dizionario non è vuoto, altrimenti restituisce che non ci sono impostazioni disponibili.

test_settings = {"Nome": "Omar", 

                }

def add_setting (setting_dict, setting_tuple):
    key = setting_tuple [0].lower()
    value = setting_tuple [1].lower()
    if key in setting_dict:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
         setting_dict [key] = value
         return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting (setting_dict, setting_tuple):
    key = setting_tuple [0].lower()
    value = setting_tuple [1].lower()
    if key in setting_dict:
        setting_dict [key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
         return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
    
def delete_setting (setting_dict, key):
    key = key.lower()
    if key in setting_dict:
        del setting_dict [key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"

def view_settings (setting_dict):
    if not setting_dict:
        return "No settings available."
    else:
        frase = "Current User Settings:"
        for key, value in setting_dict.items():
            frase += f"\n {key.capitalize()} : {value.capitalize()}" 
    return frase
   


add_setting (test_settings, ("Età", "24")) #Aggiunta di una nuova impostazione
add_setting (test_settings, ("Cognome", "Houssa")) #Tentativo di aggiungere un'impostazione già esistente
update_setting (test_settings, ("Età", "23")) #Aggiornamento di un'impostazione esistente
#delete_setting (test_settings, "Cognome") #Eliminazione di un'impostazione
print(view_settings(test_settings))

#Solo con il comando print visualizzo il risultato delle funzioni, altrimenti non vedrei nulla ma i valori sarebbero comunque aggiornati.