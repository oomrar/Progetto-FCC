# Un attributo privato _celsius viene protetto da una property. 
# Il getter restituisce il valore; il setter lo valida prima di assegnarlo. 
# Le conversioni in Fahrenheit e Kelvin sono property calcolate in sola lettura: non hanno setter e non hanno un attributo privato dedicato — vengono calcolate ogni volta che vengono lette.

print()

class Temperatura:

    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, new_celsius):
        if new_celsius < -273.15:
            print("Temperatura non valida")
            return
        self._celsius = new_celsius

    @property
    def fahrenheit(self):
        return self._celsius * 9/5 +32
    
    @property
    def kelvin(self):
        return self._celsius + 273.15
    
temp1 = Temperatura(20)
print(temp1.celsius)
print(temp1.fahrenheit)
print(temp1.kelvin)
print()
temp1.celsius = 100
print(temp1.celsius)
print(temp1.fahrenheit)
print(temp1.kelvin)
print()
temp1.celsius = -300

print()