#print("\n2-\n")

def min_max(liste):
    return min(liste), max(liste) #tuple

liste = [1,2,3,4,5]
resultat = min_max(liste)

minimum, maximum = resultat
print("Liste:", liste)
print("Min:", minimum)
print("Max:", maximum)