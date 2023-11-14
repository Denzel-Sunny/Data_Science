import math

print("----------------------\n Reg.No: SJC22MCA-2022\n Name: Denzel Sunny\n Batch: S3 MCA\n ----------------------\n")


a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

discriminant = b**2 - 4*a*c

if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Root 1: {round(root1, 2)}")
    print(f"Root 2: {round(root2, 2)}")
elif discriminant == 0:
    root = -b / (2*a)
    print(f"Root: {round(root, 2)}")
else:
    real = -b / (2*a)
    imag = math.sqrt(-discriminant) / (2*a)
    print(f"Root 1: {round(real, 2)} + {round(imag, 2)}i")
    print(f"Root 2: {round(real, 2)} - {round(imag, 2)}i")
