#print("\nex2-2\n")

def lng_nb_voy(txt):
    voyelles = "aeiouyAEIOUY"
    mots = txt.split(" ")
    resultats = []
    for mot in mots:
        nb_voyelles = 0
        for char in mot:
            if char in voyelles:
                nb_voyelles += 1
        resultats.append((mot, len(mot), nb_voyelles))
    return resultats

txt = "laleli laleli"
print( "Texte:", txt )
print( "Longueur et voyelles:", lng_nb_voy(txt) )
