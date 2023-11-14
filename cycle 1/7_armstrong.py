
print("----------------------\n Reg.No: SJC22MCA-2022\n Name: Denzel Sunny\n Batch: S3 MCA\n ----------------------\n")
t1=1
t2=1000

for num in range(t1, t2+1):
    order = len(str(num))
    sum = 0
    temp = num
    while temp>0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if num == sum:
        print(num)
