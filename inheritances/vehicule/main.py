class Vehicule:
    def __init__(self, marque, vitesse):
        self.marque = marque
        self.vitesse = vitesse
    
    def rouler(self):
        return "Le véhicule {} roule à {} km/h".format(self.marque, self.vitesse)

class Voiture(Vehicule):
    def __init__(self, marque, vitesse, nombre_de_portes):
        super(Voiture, self).__init__(marque, vitesse)
        self.nombre_de_portes = nombre_de_portes

    def rouler(self): 
        #text = super(Voiture, self).rouler() 
        #text += " et {} portes".format(self.nombre_de_portes)
        return super(Voiture, self).rouler() + " et {} portes".format(self.nombre_de_portes)

vehicule = Vehicule("Mercedes", 100)
voiture  = Voiture("BMW", 80, 4)

print(vehicule.rouler())
print(voiture.rouler())