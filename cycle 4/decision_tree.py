import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv('car.csv')
print(data.head())
col_names = ['buying', 'paint', 'doors', 'persons', 'lug_boot', 'safety', 'class']
data.columns = col_names
print(col_names)

# scikit-learn uses only numerical features and they are interpreted as continuous numeric variables
# pandas.factorize() method to get numeric representation of an array by IDing distinct values
data['class'],class_names = pd.factorize(data['class'])
data['buying'],_ = pd.factorize(data['buying'])
data['paint'],_ = pd.factorize(data['paint'])
data['doors'],_ = pd.factorize(data['doors'])
data['persons'],_ = pd.factorize(data['persons'])
data['lug_boot'],_ = pd.factorize(data['lug_boot'])
data['safety'],_ = pd.factorize(data['safety'])

print(data.head())
x = data.iloc[:, :-1]
y = data.iloc[:, -1]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

tree1 = DecisionTreeClassifier()
tree1.fit(x_train, y_train)
y_pred = tree1.predict(x_test)

count_misclassified = (y_test != y_pred).sum()
print("misclassified samples count: ", count_misclassified)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy: ", accuracy)



