import numpy as np
print("----------------------\n Reg.No: SJC22MCA-2022\n Name: Denzel Sunny\n Batch: S3 MCA\n ----------------------\n")

X = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# i) Display the cube of each element of the matrix using different methods
# Using np.power() to calculate the cube
cubed_matrix1 = np.power(X, 3)
# Using the ** operator to calculate the cube
cubed_matrix2 = X ** 3
# Using np.multiply() to calculate the cube
cubed_matrix3 = np.multiply(X, np.multiply(X, X))
# Using the * operator to calculate the cube
cubed_matrix4 = X * X * X

print("Matrix X:")
print(X)

print("\nCube of each element (using np.power()):")
print(cubed_matrix1)

print("\nCube of each element (using ** operator):")
print(cubed_matrix2)

print("\nCube of each element (using np.multiply()):")
print(cubed_matrix3)

print("\nCube of each element (using * operator):")
print(cubed_matrix4)

# ii) Display the identity matrix of the given square matrix
identity_matrix = np.identity(X.shape[0])
print("\nIdentity Matrix of X:")
print(identity_matrix)

# iii) Display each element of the matrix to different powers
exponentials = [2, 3, 4]

powered_matrices = [np.power(X, exp) for exp in exponentials]

for i, exp in enumerate(exponentials):
    print(f"\nMatrix X to the power of {exp}:")
    print(powered_matrices[i])