import numpy as np

# 1
matrix_5x5 = np.array([ 1 for i in range(5*5) ]).reshape(5,5)

for i in range( matrix_5x5.shape[1] ): #(lines, colonne)
    matrix_5x5[i][i] = 0  #1,1  2,2  3,3  4,4  5,5

print(" Matrice avec diagonale remplacée:")
print(matrix_5x5)


# 2
def is_square(matrix_5x5):
    return matrix_5x5.shape[0] == matrix_5x5.shape[1] #(5, 5)

print("\n La matrice est-elle carrée ?")
print(is_square(matrix_5x5))


# 3
matrix1 = np.array([1, 2, 3, 4, 5])

#matrix2 = np.array([ matrix1[len(matrix1)-1-i] for i in range(len(matrix1)) ]) #5-1-0=4 #5-1-1=3 #5-1-2=2 #5-1-3=1 #5-1-4=0
matrix2 = matrix1[ : : -1]

print("\n Matrice renversée:")
print(matrix2)