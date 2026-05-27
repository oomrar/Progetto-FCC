#Immagina di ricevere questa stringa fissa che rappresenta una transazione bancaria grezza:"USER_MARIO_ROSSI_CARD_1234567887654321_AMOUNT_00150.50".
# Il tuo compito è ripulire i dati per motivi di privacy e calcolare le tasse.

code = "USER_MARIO_ROSSI_CARD_1234567887654321_AMOUNT_00150.50"

nome = code[5:10]
cognome = code[11:16]

nome_cogn = nome + " " + cognome
card_number = code [22:38]
importo = float(code [47:])

asterisc = "*"
card_un = asterisc * 12 + card_number[-4:]

vat = importo * 0.22
id_transaction = cognome [-1:-4:-1] + str(int(importo))

print (f"Cliente: {nome_cogn}\nCarta: {card_un}\nTassa Iva: {vat}\nID Scontrino: {id_transaction}")