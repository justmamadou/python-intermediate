class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur  = largeur

    def aire(self):
        return self.largeur * self.longueur

    def perimetre(self):
        return (self.largeur + self.longueur) * 2

    def __str__(self):
        return "Perimetre: {} \nAire: {}".format(self.perimetre(), self.aire())


rec1 = Rectangle(10,30)
print(rec1.perimetre())
print(rec1.aire())

print(rec1)