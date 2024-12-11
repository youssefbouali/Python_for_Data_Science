#print("1-\n")

def lire_liste(n):
    liste=[]
    for i in range(n):
        element = float(input(f"Entrez l'élément {i+1} : "))
        liste.append(element)
    return liste
    
    
print( lire_liste(5) )