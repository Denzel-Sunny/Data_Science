import numpy as np

print("----------------------\n Reg.No: SJC22MCA-2022\n Name: Denzel Sunny\n Batch: S3 MCA\n ----------------------\n")
matrix1 = np.array([[1,2,3],
                    [4,5,6],
                    [7,8,9]])
matrix2 = np.array([[9,8,7],
                    [6,5,4],
                    [3,2,1]])

print("matrix 1: \n",matrix1,"\nmatrix 2: \n", matrix2)

add = matrix1 + matrix2
print("\naddition result: ")
print(add)
sub = matrix1 - matrix2
print("\nSubtraction result: ")
print(sub)
element_multiplicaiton = matrix1 * matrix2
print("\nElementwise multiplicaiton: ")
print(element_multiplicaiton)
mask = (matrix2 != 0)
div = np.divide(matrix1, matrix2, where=mask)
print("\nDivision result: ")
print(div)
transpose = matrix1.T
print("\nTranspose of Matrix: ")
print(transpose)
diagonal = np.trace(matrix1)
print("\nSum of diagonal elements: ")
print(diagonal)