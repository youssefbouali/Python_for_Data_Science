import numpy as np

# 1
matrix_3x3 = np.array(range(2, 11)).reshape(3, 3)
print(" Matrice 3x3:")
print(matrix_3x3)

# 2
matrix_5x5 = np.ones((5, 5), dtype=int)
#matrix_5x5 = np.array([[1] for i in range(5*5)]).reshape(5,5)

matrix_5x5[1:-1, 1:-1] = 0
#for i in range(1, len(matrix_5x5[0]) - 1):
#    for j in range(1, len(matrix_5x5[0]) - 1):
#        matrix_5x5[i][j] = 0

print("\n Matrice 5x5:")
print(matrix_5x5)

# 3
celsius = np.array([0, 20, 30, 100])
fahrenheit = celsius * 1.8 + 32.00
print("\n Conversion Celsius -> Fahrenheit:")
print("Celsius:", celsius)
print("Fahrenheit:", fahrenheit)