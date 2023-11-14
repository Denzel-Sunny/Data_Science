print("----------------------\n Reg.No: SJC22MCA-2022\n Name: Denzel Sunny\n Batch: S3 MCA\n ----------------------\n")

list1 = [2, 4, 6, 8, 10]
list2 = [1, 3, 5, 7, 9]
print("The First list is:", list1)
print("The Second list is:", list2)
if len(list1) != len(list2):
    print("Lists must have the same length for addition.")
else:
    result = []
    for i in range(len(list1)):
        sum_element = list1[i] + list2[i]
        result.append(sum_element)
    print("\nThe addition of 2 lists:", result)

