import numpy as np
print("----------------------\n Reg.No: SJC22MCA-2022\n Name: Denzel Sunny\n Batch: S3 MCA\n ----------------------\n")

X = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
# Create matrix Y with the same dimensions as X
Y = np.random.randint(1, 10, X.shape)

# Perform the operation X^2 + 2Y
result = X**2 + 2 * Y

# Display the original matrices and the result
print("Matrix X:")
print(X)

print("\nMatrix Y:")
print(Y)

print("\nResult of X^2 + 2Y:")
print(result)