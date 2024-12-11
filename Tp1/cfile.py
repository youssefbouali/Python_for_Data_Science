
def inverser_ordre_mots(chaine):
    mots = chaine.split(" ")
    chaine_inversee = " ".join(reversed(mots))
    print(f"Chaîne inversée : {chaine_inversee}")

chaine = input("Entrez une chaîne de caractères : ")
inverser_ordre_mots(chaine)


# def reverse(Phrase):
    # mots = Phrase.split(" ")
    # motsInverse = " ".join(reversed(mots))
    # print (motsInverse)
    
# Phrase = input("Entrer une phrase : ")
# reverse(Phrase)