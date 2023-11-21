import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

advertising = pd.read_csv('Company_data.csv')
advertising.head()
advertising.describe()
advertising.info()
print("Feature Values:")
x = advertising.iloc[:, :-1]
print(x)
print("Target Variables Values:")
y = advertising.iloc[:, -1]
print(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

regressor = LinearRegression()
regressor.fit(x_train, y_train)
print("intercept is:")
print(regressor.intercept_)
print("Co_efficients are:")
print(regressor.coef_)
y_pred = regressor.predict(x_test)
for(i,j) in zip(y_test,y_pred):
    if(i != j):
        print("Actual value: ",i, "Predicted value: ",j)
print("Number of mislabeled points from test data set:",(y_test != y_pred).sum())

print("Mean Absolute error: ",metrics.mean_absolute_error(y_test,y_pred))
print("Mean Squared error: ",metrics.mean_squared_error(y_test,y_pred))
print("Root Mean Squared error: ",np.sqrt(metrics.mean_squared_error(y_test,y_pred)))
