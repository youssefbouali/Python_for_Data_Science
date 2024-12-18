import numpy as np
import random

# 1
#array_1d = np.random.randint(1, 101, 20)
array_1d = np.array([ random.randint(1, 100) for i in range(20) ])


# 2
moyenne = np.mean(array_1d)
filtered_array1 = array_1d[array_1d > moyenne]


# 3
filtered_array2 = np.where(array_1d > moyenne, array_1d*2, array_1d)
modified_moyenne = np.mean(filtered_array2)


# 4
print("\n Tableau initial:")
print(array_1d)

print("\n Tableau filtré")
print(filtered_array1)

print("\n Tableau modifié")
print(filtered_array2)

print("\n Moyenne avant modification:")
print(moyenne)

print("\n Moyenne après modification:")
print(modified_moyenne)