class Etudiant: 
    def __init__(self, nom, prenom, notes):
        self.nom = nom
        self.prenom = prenom
        self.notes = notes

    def ajouter_note(self, note):
        return self.notes.append(note)
    
    def moyenne(self):
        sum = 0
        for i in range(len(self.notes)):
            sum += self.notes[i]
        moyenne = sum / len(self.notes)
        return moyenne

    def est_admis(self):
        if self.moyenne() > 10:
            return "L\'etudiant est admis en classe supérieure"
        else:
            return "L\'etudiant n'a pas eu la moyenne nécessaire pour passer en classe supérieure"

    def __str__(self):
        return "Etudiant : {} {} \nNotes: {} \nMoyenne : {}".format(self.prenom, self.nom, self.notes, self.moyenne())

et =  Etudiant("Mamadou", "Ba", [10,12,14,15])
print(et)

et.ajouter_note(18)
print(et)

print(et.est_admis())