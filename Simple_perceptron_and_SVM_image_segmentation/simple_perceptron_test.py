import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets._samples_generator import make_blobs
from sklearn.model_selection import train_test_split
from simple_perceptron import Perceptron
from mlxtend.plotting import plot_decision_regions
from sklearn import svm
from sklearn.metrics import classification_report


def accuracy(y_true, y_predicted):
    accuracy = np.sum(y_true == y_predicted) / len(y_true)
    return accuracy


#X, y = make_blobs(n_samples=1000, n_features=2, centers=2, random_state=2, cluster_std=1.1) # Conjunto LS

X, y = make_blobs(n_samples=1000, n_features=2, centers=2, random_state=2, cluster_std=1.9)  # Conjunto no LS

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=123)

percept = Perceptron()
error = percept.fit(X_train, y_train)
predicciones = percept.predict(X_test)

print("La accuracy del perceptron es: ", accuracy(y_test, predicciones))
print("Los pesos son: ", percept.weights, "Y el bias es: ", percept.bias)

print(classification_report(y_test, predicciones))

plot_decision_regions(X_test, y_test, clf=percept)
plt.title("Sobre el conjunto de Testeo")
plt.xlabel("x1")
plt.ylabel("x2")
plt.show()

plt.plot(error, marker='o')
plt.xlabel('Iteraciones')
plt.ylabel('Errores')
plt.show()


clf = svm.SVC(kernel='linear', C=1000)

clf.fit(X_train, y_train)
plot_decision_regions(X_test, y_test, clf=clf)
plt.title("Sobre el conjunto de Testeo")
plt.xlabel("x1")
plt.ylabel("x2")
plt.show()

plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, s=30, cmap=plt.cm.Paired)

# plot the decision function
ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()

# create grid to evaluate model
xx = np.linspace(xlim[0], xlim[1], 30)
yy = np.linspace(ylim[0], ylim[1], 30)
YY, XX = np.meshgrid(yy, xx)
xy = np.vstack([XX.ravel(), YY.ravel()]).T
Z = clf.decision_function(xy).reshape(XX.shape)

# plot decision boundary and margins
ax.contour(XX, YY, Z, colors='k', levels=[-1, 0, 1], alpha=0.5,
           linestyles=['--', '-', '--'])
# plot support vectors
# ax.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], s=100,
#           linewidth=1, facecolors='none', edgecolors='k')
plt.title("SMV sobre el conjunto de testeo")
plt.xlabel("x1")
plt.ylabel("x2")
plt.show()
