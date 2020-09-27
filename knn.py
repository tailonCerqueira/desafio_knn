# Obtendo o dataset iris

from sklearn import datasets
import numpy as np

iris = datasets.load_iris()
x = np.array(iris.data) # matriz de instâncias
y = np.array(iris.target) # vetor de rótulos

print(x)
print(y)