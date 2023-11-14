print("----------------------\n Reg.No: SJC22MCA-2022\n Name: Denzel Sunny\n Batch: S3 MCA\n ----------------------\n")
rows = int(input("enter number of rows: "))
columns = int(input("enter number of columns: "))

matrix1 = []
matrix2 = []

print("enter elements of matrix1: ")
for i in range(rows):
    row = []
    for j in range(columns):
        element = int(input(f"enter elements at row {i + 1}, column {j + 1}: "))
        row.append(element)
    matrix1.append(row)

print("enter elements of matrix2: ")
for i in range(rows):
    row = []
    for j in range(columns):
        element = int(input(f"enter elements at row {i + 1}, column {j + 1}: "))
        row.append(element)
    matrix2.append(row)

result_matrix = []

for i in range(rows):
    row = []
    for j in range(columns):
        element = matrix1[i][j] + matrix2[i][j]
        row.append(element)
    result_matrix.append(row)

print("sum of the two matrices: ")
for row in result_matrix:
    print(row)
