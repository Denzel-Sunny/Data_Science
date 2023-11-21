import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")

#sns.displot(data=iris, x="sepal_length", kde=True)
#sns.relplot(data=iris, x="sepal_length", y="petal_length", hue="species")
sns.histplot(data=iris, x="petal_length", bins=10, kde=True)

plt.show()