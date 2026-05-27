# Immagina di lavorare nel centro logistico di un e-commerce. Hai una lista di pacchi da spedire. 
# Ogni pacco è registrato come una stringa con questo formato:"ID_PACCO:DESTINAZIONE:PESO"

carico_giornaliero = ["P01:ROMA:2.5", "P02:LONDRA:9.0", "P03:PARIGI:4.8", "P04:BERLINO:15.5"]

# Definita la funzione per calcolare il prezzo di ogni carico.
def calcola_costo (città, peso):
    if città == "ROMA":
        return 5
    elif peso < 5:
        return 15
    else:
        return 25

# Accumulatori.
costo_totale = 0
pacchi_pesanti = 0

# Ciclo, che analizza i dati uno per uno.
for carico in carico_giornaliero:
    sezioni = carico.split (":")
    città = sezioni [1]
    peso = float(sezioni [2])
    costo_totale += calcola_costo(città, peso)

    if peso > 10:
        pacchi_pesanti += 1
   
# Output finale.
print (f"-- REPORT SPEDIZIONI -- \nCosto totale spedizioni: €{costo_totale}\nNumero pacchi pesanti (>10kg): {pacchi_pesanti}")
    


    
    
        