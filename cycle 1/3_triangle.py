def checkTriangle(x, y, z):
    if x == y == z:
        print("Given Triangle is a Equilateral Triangle")

    elif x == y or y == z or z == x:
        print("Given Triangle is a Isosceles Triangle")

    else:
        print("Given Triangle is a Scalene Triangle")

print("----------------------\n Reg.No: SJC22MCA-2022\n Name: Denzel Sunny\n Batch: S3 MCA\n ----------------------\n")
print("enter sides of the Triangle")
side1=int(input("enter side1: "))
side2=int(input("enter side2: "))
side3=int(input("enter side3: "))

checkTriangle(side1, side2, side3)