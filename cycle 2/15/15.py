import numpy as np
print("----------------------\n Reg.No: SJC22MCA-2022\n Name: Denzel Sunny\n Batch: S3 MCA\n ----------------------\n")

# Define matrix A and vector b
A = np.array([[2, 1],
              [1, 3]])

b = np.array([5, 7])

# Use np.linalg.solve() to find X
X = np.linalg.solve(A, b)

# Display the solution X
print("Matrix A:")
print(A)

print("\nVector b:")
print(b)

print("\nSolution X (from AX = b):")
print(X)
