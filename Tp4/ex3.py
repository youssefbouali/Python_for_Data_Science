import numpy as np

# 1
matrix_4x4 = np.array(range(1, 17)).reshape(4, 4)
print(" Matrice 4x4:")
print(matrix_4x4)


# 2
#matrix_4x4[ [0,2] ] = matrix_4x4[ [2,0] ]
temp_row = np.copy(matrix_4x4[0])
matrix_4x4[0] = matrix_4x4[2]
matrix_4x4[2] = temp_row

print("\n Matrice après échange des lignes 1 et 3:")
print(matrix_4x4)


# 3
column_sums = np.sum(matrix_4x4, axis=0) #axis=0 -> colonne
print("\n Somme de chaque colonne:")
print(column_sums)


# 4
matrix_4x4 = matrix_4x4.T
print("\n Matrice transposée:")
print(matrix_4x4)
