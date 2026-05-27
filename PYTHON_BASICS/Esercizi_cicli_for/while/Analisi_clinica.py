# Vogliamo classificare queste misurazioni e contare quante sono preoccupanti.

pressioni = [120, 145, 118, 150, 160, 115]

casi_alti = 0
da_ricontrollare = []

for dato in pressioni:
    if dato > 140:
        casi_alti += 1
        da_ricontrollare.append(dato)
        print (f"Valore {dato}: ALTO")
    else:
        print(f"Valore {dato}: REGOLARE")

print(f" \nRIEPILOGO:\nCasi alti:{casi_alti}\nDa ricontrollare: {da_ricontrollare}")