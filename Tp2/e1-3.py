#print("\n3-\n")

def element_plus_frequent(liste):
    plus_frequent = max(liste, key=liste.count)
    return plus_frequent

liste = [1,2,2,3,4,4,4,5]
print("Liste:", liste)
print("élément le plus fréquent:", element_plus_frequent(liste))