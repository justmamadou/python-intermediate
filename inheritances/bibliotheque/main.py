class Livre:
    def __init__(self, titre, auteur, annee):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee

    def __str__(self):
        return "Livre: Titre: {}, Auteur: {}, Année: {}".format(self.titre, self.auteur, self.annee)
 
class Bibliotheque:
    def __init__(self, livres=[]):
        self.livres = livres
    
    def ajouter_livrer(self, livre):
        self.livres.append(livre)
        return self.livres

    def recherche_par_auteur(self, auteur):
        livres_par_auteur = []
        for i in self.livres:
            if i.auteur == auteur:
                livres_par_auteur.append(i.titre)
        return livres_par_auteur


    def __str__(self):
        titres = []
        for i in self.livres:
          titres.append(i.titre)
        return "Livres: {} ".format(str(titres))


b = Bibliotheque()
l= Livre("The Alchimist", "Paulo Coehlo", 2016)
l2= Livre("Think and Grow Rich", "Napeleon Hill", 2016)
l3= Livre("Les quatres accords toltheques", "Napeleon Hill", 2016)
print(l)
print(l2)

b.ajouter_livrer(l)
b.ajouter_livrer(l2)
b.ajouter_livrer(l3)
print(b)

print(b.recherche_par_auteur("Napeleon Hill"))