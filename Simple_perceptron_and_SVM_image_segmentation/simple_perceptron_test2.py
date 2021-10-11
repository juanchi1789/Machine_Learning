
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets._samples_generator import make_blobs
from sklearn.model_selection import train_test_split
from simple_perceptron import Perceptron
from mlxtend.plotting import plot_decision_regions
from sklearn import svm
from simple_perceptron_test import accuracy


X, y = make_blobs(n_samples=100,n_features=2 ,centers=2, random_state=2, cluster_std=1.1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=123)

percept = Perceptron()
error = percept.fit(X_train, y_train)
predicciones = percept.predict(X_test)

print("Los pesos son: ",percept.weights, "Y el bias es: ",percept.bias)

# La recta queda como x1*w1 + x2*w2 + bias = 0

plt.scatter(X[:,0],X[:,1])
plt.show()
