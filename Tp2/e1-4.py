#print("\n4-\n")

def supprimer_negatifs(liste):
    return list(filter(lambda x:x>=0, liste))

liste = [1,2,3,4,0,-1,-2]
print("Liste:", liste)
print("Liste sans les nombres négatifs:", supprimer_negatifs(liste) )
