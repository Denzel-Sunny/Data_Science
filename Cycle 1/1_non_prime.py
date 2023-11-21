def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
        return True

print("----------------------\n Reg.No: SJC22MCA-2022\n Name: Denzel Sunny\n Batch: S3 MCA\n ----------------------\n")

start = int(input("Enter the starting number: "))
end = int(input("Enter the end number: "))
print(f"non-prime numbers between {start} and {end} is: ")
for num in range(start, end+1):
    if not is_prime(num):
        print(num, end=" ")