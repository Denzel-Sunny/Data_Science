from math import gcd
def co_prime(a, b):
    if gcd(a, b) == 1:
        print(f"the numbers {a} and {b} are coprime")
    else:
        print("not co-prime")

print("----------------------\n Reg.No: SJC22MCA-2022\n Name: Denzel Sunny\n Batch: S3 MCA\n ----------------------\n")

a=int(input("enter a: "))
b=int(input("enter b: "))

co_prime(a,b)