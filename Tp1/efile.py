

def frequence_mots(chaine):
    mots = chaine.split(" ")
    frequence = {}
    for mot in mots:
        frequence[mot] = frequence.get(mot, 0) + 1
    return frequence

chaine = input("Entrez une chaîne de caractères : ")
frequence = frequence_mots(chaine)
print(f"Fréquence des mots : {frequence}")


# def reverse(Phrase):
    # dictio = {}
    # mots = Phrase.split(" ")
    # for i in mots:
        # dictio[i] = dictio.get(i,0)+1
    
    # print (dictio)
    
# Phrase = input("Entrer une phrase : ")
# reverse(Phrase)