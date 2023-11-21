print("----------------------\n Reg.No: SJC22MCA-2022\n Name: Denzel Sunny\n Batch: S3 MCA\n ----------------------\n")

n1, n2 =0, 1
limit =  int(input("Enter the range: "))
print("Fibonacci series: ")
print(n1, n2, end=" ")
for i in range(2, limit):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")


