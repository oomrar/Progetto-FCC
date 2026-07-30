# In questo progetto, userai la programmazione orientata agli oggetti per creare una classe Rectangle e una classe Square. La classe Square dovrebbe essere una sottoclasse di Rectangle e ereditare i suoi metodi e attributi.




class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, larghezza):
        self.width = larghezza
        
    def set_height(self, altezza):
        self.height = altezza

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)
    
    def get_diagonal(self):
        return (self.width**2 + self.height**2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        else:
            riga = '*'* self.width + '\n'
            return riga * self.height
    def get_amount_inside(self,forma):
        fit_orizzontale = self.width // forma.width
        fit_verticale = self.height // forma.height
        return fit_orizzontale * fit_verticale

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"  


class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)

    def set_width(self, new_side):
        self.width = new_side
        self.height = new_side
    def set_height(self, new_side):
        self.height = new_side
        self.width = new_side
    def set_side(self, side):
        self.set_width(side)
    def __str__(self):
        return f"Square(side={self.width})"

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))