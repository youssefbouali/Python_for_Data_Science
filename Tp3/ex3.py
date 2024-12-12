class CompteBancaire:
    compteur = 0
    def __init__(self, solde=0):
        CompteBancaire.compteur += 1
        self.code = CompteBancaire.compteur
        self.solde = solde
    def deposer(self, montant):
        self.solde += montant
    def retirer(self, montant):
        self.solde -= montant
    def __str__(self):
        return f"Compte {self.code}, Solde : {self.solde} MAD"

class CompteEpargne(CompteBancaire):
    TauxInteret = 6
    def calculInteret(self):
        self.solde += self.solde * (CompteEpargne.TauxInteret / 100)

class ComptePayant(CompteBancaire):
    def deposer(self, montant):
        super().deposer(montant - 5)

    def retirer(self, montant):
        super().retirer(montant + 5)

if __name__ == "__main__":
    c1 = CompteBancaire()
    c2 = CompteEpargne(1000)
    c3 = ComptePayant()

    c1.deposer(500)
    c2.deposer(500)
    c3.deposer(500)

    c1.retirer(100)
    c2.retirer(100)
    c3.retirer(100)

    c2.calculInteret()
    print(c1)
    print(c2)
    print(c3)

    comptes = []
    for i in range(5):
        compte = CompteBancaire()
        compte.deposer(2000 + 100 * i)
        comptes.append(compte)

    for compte in comptes:
        print(compte)
        