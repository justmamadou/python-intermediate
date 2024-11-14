class Livre:
    def __init__(self, titre, auteur, annee):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee

class Bibliotheque:
    def __init__(self, livres=0):
        self.livres = livres

    livres = []
    
    def ajouter_livrer(self, titre, auteur, annee):
        livre = Livre(titre, auteur, annee)
        livres.append(livre)
        return livres


b = Bibliotheque