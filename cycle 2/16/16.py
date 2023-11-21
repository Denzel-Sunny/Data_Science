import numpy as np
print("----------------------\n Reg.No: SJC22MCA-2022\n Name: Denzel Sunny\n Batch: S3 MCA\n ----------------------\n")

# Define the matrix A
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# Perform SVD
U, S, Vt = np.linalg.svd(A)

# Reconstruct the matrix A from the three matrices obtained after SVD
reconstructed_A = U @ np.diag(S) @ Vt

# Display the original matrix A
print("Matrix A:")
print(A)

# Display the matrices U, S, and Vt
print("\nMatrix U:")
print(U)

print("\nMatrix S (Diagonal Matrix):")
print(S)

print("\nMatrix Vt (Transpose of V):")
print(Vt)

# Display the reconstructed matrix A
print("\nReconstructed Matrix A:")
print(reconstructed_A)
