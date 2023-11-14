import numpy as np

print("----------------------\n Reg.No: SJC22MCA-2022\n Name: Denzel Sunny\n Batch: S3 MCA\n ----------------------\n")

print("Array with first 15 even numbers: ")
even_numbers = np.arange(2, 32, 2)
print(even_numbers)

subset_a = even_numbers[2:9:2]
print("\na. Elements from index 2 to 8 with step 2: ", subset_a)

subset_b = even_numbers[-3:]
print("\nb. Last 3 elements of the array using negative index: ", subset_b)

subset_c = even_numbers[::2]
print("\nc. Alternative elements of the array: ", subset_c)

subset_d = even_numbers[-3::2]
print("\nd. Last 3 alternate elements: ", subset_d)
