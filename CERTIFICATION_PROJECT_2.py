# Applicazione di Gestione Budget e Grafico delle Spese
# Questo modulo definisce la classe 'Category' per gestire un registro di transazioni finanziarie (depositi, prelievi, trasferimenti) suddivise per categorie di spesa.
# Include inoltre la funzione esterna 'create_spend_chart' per generare una rappresentazione grafica testuale della percentuale di spesa di ogni categoria rispetto al totale complessivo.


class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    def deposit(self, importo, descrizione=""):
        self.ledger.append({"amount": importo, "description": descrizione})
        
    def withdraw(self, importo, descrizione=""):
        if self.check_funds(importo):
            self.ledger.append({"amount": -importo, "description": descrizione})
            return True
        return False
        
    def get_balance(self):
        saldo_corrente = 0
        for transaction in self.ledger:
            saldo_corrente += transaction["amount"]
        return saldo_corrente

    def transfer(self, importo, altra_categoria):
        if self.check_funds(importo):
            self.withdraw(importo, f"Transfer to {altra_categoria.name}")
            altra_categoria.deposit(importo, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, importo):
        if importo > self.get_balance():
            return False
        return True    
    
    def __str__(self):
        output = self.name.center(30, "*") + "\n"
        for trans in self.ledger:
            desc = trans["description"][:23]
            amount = f"{trans['amount']:.2f}"
            output += f"{desc:<23}{amount:>7}\n"
        output += f"Total: {self.get_balance():.2f}"
        return output

def create_spend_chart(categories):
    chart = "Percentage spent by category\n"

    spese_per_categoria = []
    totale_generale_speso = 0

    for cat in categories:
        spesa_cat = 0
        for trans in cat.ledger:
            if trans["amount"] < 0:
                spesa_cat += abs(trans["amount"])
        spese_per_categoria.append(spesa_cat)
        totale_generale_speso += spesa_cat

    percentuali = []
    for spesa in spese_per_categoria:
        if totale_generale_speso > 0:
            percentuale_reale = (spesa / totale_generale_speso) * 100
            percentuali.append(int(percentuale_reale // 10) * 10)
        else:
            percentuali.append(0)

    for valore in range(100, -1, -10):
        chart += f"{valore:>3}|"
        for perc in percentuali:
            if perc >= valore:
                chart += " o "
            else:
                chart += "   "
        chart += " \n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    nomi = [cat.name for cat in categories]
    max_lunghezza = max(len(nome) for nome in nomi)
    
    for i in range(max_lunghezza):
        chart += "    "
        for nome in nomi:
            if i < len(nome):
                chart += f" {nome[i]} "
            else:
                chart += "   "
        
        chart += " "
        if i < max_lunghezza - 1:
            chart += "\n"

    return chart

food = Category("Food")
clothing = Category("Clothing")
auto = Category("Auto")

# 2. Esegui dei movimenti (depositi e prelievi)
food.deposit(1000, "deposito iniziale")
food.withdraw(100.50, "spesa alimentare")
food.withdraw(50.00, "ristorante")

clothing.deposit(500, "deposito iniziale")
clothing.withdraw(50.00, "scarpe")

auto.deposit(300, "deposito iniziale")
auto.withdraw(200.00, "benzina e meccanico")

# 3. Metti le categorie dentro una lista
mie_categorie = [food, clothing, auto]

# 4. Genera e stampa il grafico a barre
grafico = create_spend_chart(mie_categorie)
print(grafico)