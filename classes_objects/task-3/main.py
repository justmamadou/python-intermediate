class CompteBancaire:
    def __init__(self):
        self.solde = 0

    def deposer(self, montant):
        self.solde += montant

    def retirer(self, montant):
        if self.solde == 0:
            print(" Votre solde est de 0, vous ne pouvez pas retirer")
        else:
          self.solde -= montant
    def __str__(self):
        return "Le solde actuel est de {}".format(self.solde)


comp1 = CompteBancaire()
print(comp1)

comp1.deposer(100)
print(comp1)

comp1.retirer(60)
print(comp1)
