class Produit:
    def __init__(self, nom, prix, quantite):
        self.nom = nom
        self.prix = prix
        self.quantite = quantite

class Stock():
    def __init__(self, produits=[]):
        self.produits = produits
    
    def ajouter_produit(self, produit):
        self.produits.append(produit)
        return self.produits

    def supprimer_produit(self, produit):
        self.produits.remove(produit)

    def afficher_produits(self):
      return "Produits: {}".format(self.produits)
    

