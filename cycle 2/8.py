import numpy as np
print("----------------------\n Reg.No: SJC22MCA-2022\n Name: Denzel Sunny\n Batch: S3 MCA\n ----------------------\n")

arr1 = np.array([1, 2, 3, 4, 5])
# Insert element at specific index (15 at index 2)
arr1_insert = np.insert(arr1, 2, 15)

print("Original array: ",arr1)
print("After insertion: ",arr1_insert)


arr2 = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])
# insert at  specific row index
arr2_inserted = np.insert(arr2, 1, [10, 11, 12], axis=0)

print("\noriginal 2d array: \n", arr2)
print("\n2D array after insertion: ", arr2_inserted)