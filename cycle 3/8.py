import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

iris = pd.read_csv("iris.csv")

pairplot = sns.pairplot(iris, kind="scatter", markers=["o"])

#pairplot = sns.pairplot(iris, kind="kde", markers=["s"])

#pairplot = sns.pairplot(iris, kind="reg", markers=["D"])

#pairplot = sns.pairplot(iris, kind="hist")

plt.show()

