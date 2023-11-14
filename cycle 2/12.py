import numpy as np
print("----------------------\n Reg.No: SJC22MCA-2022\n Name: Denzel Sunny\n Batch: S3 MCA\n ----------------------\n")
A = np.array([[1, 2, 3, 4, 5, 6],
              [7, 8, 9, 10, 11, 12],
              [13, 14, 15, 16, 17, 18],
              [19, 20, 21, 22, 23, 24],
              [25, 26, 27, 28, 29, 30]])
B = np.array([[2, 4, 6],
              [1, 3, 5],
              [7, 8, 9]])
print("Matrix A:")
print(A)
print("\nMatrix B:")
print(B)
# Extract a sub-matrix of dimension 3x3 from A
sub_matrix_A = A[:3, :3]
# Multiply the sub-matrix with matrix B
result_matrix = np.dot(sub_matrix_A, B)
# Replace the extracted sub-matrix in A with the result matrix
A[:3, :3] = result_matrix

print("\nResult Matrix (Sub-matrix * B):")
print(result_matrix)
print("\nUpdated Matrix A after Replacement:")
print(A)