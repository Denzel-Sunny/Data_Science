import numpy as np
print("----------------------\n Reg.No: SJC22MCA-2022\n Name: Denzel Sunny\n Batch: S3 MCA\n ----------------------")

n = 4
matrix = np.random.randint(1, 10, (n, n))

try:
    inverse_matrix = np.linalg.inv(matrix)
except np.linalg.LinAlgError:
    inverse_matrix = None
    print("The Matrix is not invertible.")

rank = np.linalg.matrix_rank(matrix)
determinant = np.linalg.det(matrix)
matrix_id = matrix.flatten()
eigenvalues, eigenvectors = np.linalg.eig(matrix)
print("Original matrix: ", matrix)

if inverse_matrix is not None:
    print("Inverse matrix: \n", inverse_matrix)

print("Rank of Matrix: ", rank)
print("Determinant of Matrix: ", determinant)
print("Matrix as 1D array: ", matrix_id)
print("Eigenvalues: \n", eigenvalues)
print("Eigenvectors: \n", eigenvectors)

