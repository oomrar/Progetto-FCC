# Gestisci il sistema informatico di una pompa di benzina. 
# Devi elaborare i rifornimenti della giornata, calcolare gli incassi per tipo di carburante e trovare il cliente che ha speso di più.

clienti      = ["Targa AX219", "Targa BK774", "Targa CZ501", "Targa DM883", "Targa EF120", "Targa GH456", "Targa IL789"]
litri        = [40, 25, 60, 15, 80, 35, 50]
carburante   = ["benzina", "diesel", "benzina", "diesel", "benzina", "diesel", "benzina"]
prezzo_benz  = 1.85
prezzo_dies  = 1.72

# Scontrini

def calcola_costo(clienti, litri, carburante, i):
        costo_cliente = 0
        if carburante[i]=="benzina":
            costo_cliente = prezzo_benz * litri[i]
            print(f"{clienti[i]} | {litri[i]}L benzina | €{round(costo_cliente, 2)}")
        elif carburante[i]=="diesel":
                costo_cliente = prezzo_dies * litri[i]
                print(f"{clienti[i]} | {litri[i]}L diesel | €{round(costo_cliente, 2)}")


for i in range(len(clienti)):
     calcola_costo(clienti, litri, carburante, i)

print("+" * 50)
   
    
litri_benz = 0
litri_dies = 0

# Fase 2: Totali per carburante
for i in range(len(clienti)):
     if carburante[i] == "benzina":
          litri_benz += litri[i]
     elif carburante [i] == "diesel":
          litri_dies += litri[i]

incasso_benz = litri_benz * 1.85
incasso_dies = litri_dies * 1.72

print(f"Benzina | tot litri: {litri_benz} | Incasso: {incasso_benz}")
print(f"Diesel | tot litri: {litri_dies} | Incasso: {incasso_dies}")

print("+" * 50)

# Fase 3: Cliente TOP

cliente_max = 0
indice_max = 0

for i in range(len(clienti)):
     costo_cliente = 0
     if carburante[i]=="benzina":
        costo_cliente = prezzo_benz * litri[i]
        if costo_cliente > cliente_max:
             cliente_max = costo_cliente    
             indice_max = i
             
     elif carburante[i]=="diesel":
            costo_cliente = prezzo_dies * litri[i]
            if costo_cliente > cliente_max:
                cliente_max = costo_cliente   
                indice_max = i
                     
print(f"Cliente TOP: {clienti[indice_max]} con {cliente_max}")

print("+" * 50)

# Fase 4: Fascia di spesa

bassa_spesa = []
media_spesa = []
alta_spesa = []

for i in range(len(clienti)):
    costo_cliente = 0
    if carburante[i]=="benzina":
        costo_cliente = prezzo_benz * litri[i]
    elif carburante[i]=="diesel":
            costo_cliente = prezzo_dies * litri[i]
    if costo_cliente < 40:
         bassa_spesa.append(clienti[i])
    elif costo_cliente <= 100:
          media_spesa.append(clienti[i])
    else:
         alta_spesa.append(clienti[i])
    
print(f"Alta spesa ({len(alta_spesa)}): {alta_spesa}")

print("+" * 50)

# Fase 5: Rifornimento simulato

clienti.append("Targa ZZ999")
litri.append(55)
carburante.append("benzina")

for i in range(len(clienti)):
     calcola_costo(clienti, litri, carburante, i)