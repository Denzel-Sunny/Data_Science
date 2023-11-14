import numpy as np
print("----------------------\n Reg.No: SJC22MCA-2022\n Name: Denzel Sunny\n Batch: S3 MCA\n ----------------------\n")

complex_array = np.array([[1+2j, 2+3j, 3+4j], [4+5j, 5+6j, 6+7j]], dtype=complex)

print("2D complex array: ")
print(complex_array)

rows, cols = complex_array.shape
print(f"\nNumber of rows: {rows}")
print(f"Number of columns: {cols}")

dimensions = complex_array.ndim
print(f"\nDimension of array : {dimensions}")

reshaped_array = complex_array.reshape(3,2)
print("\nReshaped Array: ")
print(reshaped_array)


