# Un'agenzia HR deve applicare adeguamenti salariali, formattare report e calcolare costi aziendali. 
# Tutte le trasformazioni che in precedenza avresti fatto con cicli for ora le farai con map() e lambda.

nomi      = ["Alice","Bruno","Carla","Diego","Elena","Fabio"]
stipendi  = [2800, 3200, 2500, 4100, 3600, 2900]   # euro/mese
ruoli     = ["Junior","Senior","Junior","Lead","Senior","Junior"]
aumento   = {"Junior": 0.08, "Senior": 0.05, "Lead": 0.10}  # percentuali

print('')


aggiungi_tasse = lambda s: round(s * 1.23, 2)
in_ore = lambda s: round(s / 160, 2)
print("--- STIPENDI TASSATI ---")
print('')
for stipendio in stipendi:
    
    print(f"- {stipendio} -> {aggiungi_tasse(stipendio)}")
    print(f"  Stipendio orario: {in_ore(stipendio)}")
    print('')

print('')








