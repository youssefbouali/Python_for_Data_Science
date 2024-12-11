print("1-\n")

#def lire_liste(n):
#    l=[0]
#    for i in range(n):
#        v = float(input(f"entrer une list :{i}"))
#        l.append(v)
#    print (l)
#        
#
#lire_liste(5)


print("\n2-\n")

def minmax_liste(n):
    print(min(n))
    print(max(n))

minmax_liste([1,2,3,4,5])


print("\n3-\n")

def frequence_numbers(listnumbers):
    frequence = max(listnumbers, key=listnumbers.count)
    return frequence

listnumbers = [1,2,3,4,4,5,2,4]
frequence = frequence_numbers(listnumbers)
print (frequence)


#def frequence_numbers(listnumbers):
#    frequence = {}
#    for number in listnumbers:
#        frequence[number] = frequence.get(number, 0) + 1
#    return frequence
#
#listnumbers = [1,2,3,4,4,5,2,4]
#frequence = frequence_numbers(listnumbers)
#plusfr = sorted(frequence, key=lambda x:frequence.get(x, 0), reverse=True)
#print(f"plusfr : {plusfr[0]}")
#print(f"Fréquence des numbers : {frequence}")


print("\n4-\n")

def supp(l):
    p = list(filter(lambda x:x>0, l))

p2 = supp([1,2,3,4,4,5,2,4,0,-1,-2])
print(p2)



print("\n5-\n")

def s(listn):
    return sum(listn)

print( s([1,2,3]) )



print("\nex2-1\n")

def verifier_uniques(liste):
    #set(list) Get unique elements set([1,2,3,3]) => 1 2 3
    return len(liste) == len(set(liste))
    
print( verifier_uniques([1,2,3,3]) )


print("\nex2-2\n")

#def lng_nb_voy(txt):
#    voyelles = "aeiouyAEIOUY"
#    mots = txt.split(" ")
#    resultats = []
#    for mot in mots:
#        for char in mot:
#            if char in voyelles:
#                resultats[mot] += 1
#                resultats.append((len(mot), nb_voyelles))
#                nb_voyelles
#            
#        nb_voyelles = sum(1 for char in mot if char in voyelles)
#        resultats.append((len(mot), nb_voyelles))
#    return resultats
#
#print(lng_nb_voy("laleli laleli"))

def lng_nb_voy(txt):
    voyelles = "aeiouyAEIOUY"
    mots = txt.split(" ")
    resultats = []
    for mot in mots:
        nb_voyelles = sum(1 for char in mot if char in voyelles)
        resultats.append((len(mot), nb_voyelles))
    return resultats

print(lng_nb_voy("laleli laleli"))


print("\nex3\n")


print("\nex4\n")

import csv, json