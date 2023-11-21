import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import numpy as np


student = pd.read_csv('student_scores.csv')
print(student.head())
student.describe()
student.info()

Xax = student.iloc[:,0]
Yax = student.iloc[:,1]
plt.scatter(Xax,Yax)
plt.xlabel("No. of hours")
plt.ylabel("Score")
plt.title("Student scores")
plt.show()

x = student.iloc[:, :-1]
y = student.iloc[:, 1]
print('X values: ')
print(x)
print('Y values: ')
print(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
print(x_train)

regressor = LinearRegression()
regressor.fit(x_train, y_train)
print('INTERCEPT=', regressor.intercept_)
print('CO_EFFICENT=',regressor.coef_)
y_pred = regressor.predict(x_test)
for(i,j) in zip(y_test, y_pred):
    if(i!=j):
        print("Actual value :",i,"predicted value :", j)
print("Number of mislabeled points from test data set :", (y_test != y_pred).sum())

print("Mean Absolute error :", metrics.mean_absolute_error(y_test,y_pred))
print("Mean Squared error :", metrics.mean_squared_error(y_test,y_pred))
print("Root Mean Squared error :", np.sqrt(metrics.mean_squared_error(y_test,y_pred)))