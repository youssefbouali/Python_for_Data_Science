
def afficher_triangle(chaine):
    if len(chaine) < 4:
        print("La chaîne doit avoir une longueur minimale de 4.")
        return
    for i in range(1, len(chaine) + 1):
        print(chaine[:i])

chaine = input("Entrez une chaîne de caractères (min 4 caractères) : ")
afficher_triangle(chaine)



# def forme(Ch):

    # if len(Ch) < 4 :
        # print ("Les caracteres est inferiere à 4")
        # return
    
    # oldchars = ""
    # for i in Ch:
        # oldchars = oldchars+i
        # print (oldchars)
        
    
# Ch = input("Entrez les caracteres : ")
# forme(Ch)