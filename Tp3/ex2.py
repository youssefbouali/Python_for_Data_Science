class Article:
    def __init__(self, nom, reference, prixUnitaire):
        self.__nom = nom
        self.__reference = reference
        self.__prixUnitaire = prixUnitaire

    def get_nom(self):
        return self.__nom
    def set_nom(self, nom):
        self.__nom = nom
    def get_reference(self):
        return self.__reference
    def set_reference(self, reference):
        self.__reference = reference
    def get_prixUnitaire(self):
        return self.__prixUnitaire
    def set_prixUnitaire(self, prix):
        self.__prixUnitaire = prix
    def getType(self):
        return "Ceci est un article."

class Stylo(Article):
    def __init__(self, nom, reference, prixUnitaire, couleur):
        super().__init__(nom, reference, prixUnitaire)
        self.__couleur = couleur

    def get_couleur(self):
        return self.__couleur
    def set_couleur(self, couleur):
        self.__couleur = couleur
    def getType(self):
        return "Ceci est un stylo."

class Ramette(Article):
    def __init__(self, nom, reference, prixUnitaire, formatb):
        super().__init__(nom, reference, prixUnitaire)
        self.__formatb = formatb

    def get_format(self):
        return self.__formatb
    def set_format(self, formatb):
        self.__formatb = formatb
    def getType(self):
        return "Ceci est une ramette."

if __name__ == "__main__":
    article = Article("Article1", "77", 10.0)
    stylo = Stylo("Bic", "123", 2.5, "Bleu")
    ramette = Ramette("A4 Papier", "400", 15.0, "A4")
    print(stylo.getType())
    print(ramette.getType())
    print(article.getType())
