import numpy as np

print("----------------------\n Reg.No: SJC22MCA-2022\n Name: Denzel Sunny\n Batch: S3 MCA\n ----------------------\n")

array_2d = np.array([[1, 2, 3, 4],
                     [5, 6, 7, 8],
                     [9, 10, 11, 12],
                     [13, 14, 15, 16]])
print(array_2d)
a_result = array_2d[1:, :]
print("\nAll elements excluding the first row: ")
print(a_result)

b_result = array_2d[:, :-1]
print("\nAll elements excluding the last column: ")
print(b_result)

c_result = array_2d[1:3, 0:2]
print("\nElements of the 1st and 2nd column in the 2nd and 3rd row: ")
print(c_result)

d_result = array_2d[:, 1:3]
print("\nElements of the 2nd and 3rd column: ")
print(d_result)

e_result = array_2d[0, 1:3]
print("\n2nd and 3rd element of the 1st row: ")
print(e_result)

f_result = array_2d[1:3, 0:3].flatten()[::-1]
print("\nElements from indices 4 to 10 in descending order: ")
print(f_result)