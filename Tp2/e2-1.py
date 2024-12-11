#print("\nex2-1\n")

def verifier_uniques(liste):
    #set(list) Get unique elements set([1,2,3,3]) => 1 2 3
    return len(liste) == len(set(liste)) # convertir la liste en un ensemble


liste = [1,2,3,3]
print( "Liste:", liste )
print( "La liste est unique:", verifier_uniques(liste) )
