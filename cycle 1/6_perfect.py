
print("----------------------\n Reg.No: SJC22MCA-2022\n Name: Denzel Sunny\n Batch: S3 MCA\n ----------------------\n")

n = int(input("enter the number: "))

sum = 0

for i in range(1, n):
    if n % i == 0:
        sum = sum + i

if sum == n:
    print(f"The number {n} is a perfect number")
else:
    print(f"The number {n} is not a perfect number")