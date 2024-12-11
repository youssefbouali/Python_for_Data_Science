
def frequence_caracteres(chaine):
    frequence = {}
    for caractere in chaine:
        frequence[caractere] = frequence.get(caractere, 0) + 1
    return frequence

chaine = input("Entrez une chaîne de caractères : ")
frequence = frequence_caracteres(chaine)
print(f"Fréquence des caractères : {frequence}")



# def reverse(Phrase):
    # dictio = {}
    # for i in Phrase:
        # dictio[i] = dictio.get(i,0)+1
    
    # print (dictio)
    
# Phrase = input("Entrer une phrase : ")
# reverse(Phrase)