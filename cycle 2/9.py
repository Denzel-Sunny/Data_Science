import numpy as np
print("----------------------\n Reg.No: SJC22MCA-2022\n Name: Denzel Sunny\n Batch: S3 MCA\n ----------------------\n")

arr1 = np.array([1,2,3,4,5])
diagonal_elements = np.diag(arr1)
print("Original Array: ", arr1)
print("Diagonal elements: ", diagonal_elements)

arr2 = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
diag_elments = np.diag(arr2)
print("Original 2d array: \n", arr2)
print("Diagonal elements: ", diag_elments)

arr_nonsqr = np.array([[1, 2, 3],
                      [4, 5, 6]])
diag_nonsqr = np.diag(arr_nonsqr)
print("Original: \n", arr_nonsqr)
print("diagonal elements: \n", diag_nonsqr)
