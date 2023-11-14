import pandas as pd
print("----------------------\n Reg.No: SJC22MCA-2022\n Name: Denzel Sunny\n Batch: S3 MCA\n ----------------------\n")

df = pd.read_csv('iris.csv')

#shape of data
print("Shape of data: ", df.shape)

#first 5 rows of the data
print("\nfirst 5: \n", df.head())
#last 5 rows of the data
print("\nlast 5: \n", df.tail())

#description
print("\nDescription of dataset: \n", df.describe())

#count no of sample for each variety
print("\nNo. fo samples: \n", df['variety'].value_counts())