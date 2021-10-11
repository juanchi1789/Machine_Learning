
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets._samples_generator import make_blobs
from sklearn.model_selection import train_test_split
import math
from mlxtend.plotting import plot_decision_regions
from sklearn import svm


class Perceptron:

    def __init__(self, learning_rate=0.1, n_iters=100):
        self.lr = learning_rate
        self.n_iters = n_iters
        self.activation_func = self._unit_step_func
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samples, n_features = X.shape
        errores = []

        # init parameters
        self.weights = np.zeros(n_features)
        self.bias = 0
        error = 1
        i = 0

        while i < self.n_iters and error > 0:
            # print("iter ", i)
            error = 0
            for idx, x_i in enumerate(X):
                linear_output = np.dot(x_i, self.weights) + self.bias
                y_predicted = self.activation_func(linear_output)
                update = self.lr * (y[idx] - y_predicted)
                self.weights += update * x_i
                self.bias += update
                if y[idx] - y_predicted != 0:
                    error = error + 1
            # print("El error en la tanda: ", i, " es: ", error)
            errores.append(error)
            i = i + 1

        return errores

    def predict(self, X):
        linear_output = np.dot(X, self.weights) + self.bias
        y_predicted = self.activation_func(linear_output)
        return y_predicted

    def _unit_step_func(self, x):
        return np.where(x >= 0, 1, 0)


def shortest_distance(x1, y1, a, b, c):
    d = abs((a * x1 + b * y1 + c)) / (math.sqrt(a * a + b * b))
    return d


def accuracy(y_true, y_predicted):
    accuracy = np.sum(y_true == y_predicted) / len(y_true)
    return accuracy


def tandas(puntos_min_1, puntos_min_2):
    tanda_1 = []
    tanda_1.append([puntos_min_1[0], puntos_min_1[1]])
    tanda_1.append([puntos_min_1[0], puntos_min_1[2]])
    tanda_1.append([puntos_min_1[1], puntos_min_1[2]])
    tanda_1 = np.array(tanda_1)

    tanda_2 = []
    tanda_2.append([puntos_min_2[0], puntos_min_2[1]])
    tanda_2.append([puntos_min_2[0], puntos_min_2[2]])
    tanda_2.append([puntos_min_2[1], puntos_min_2[2]])
    tanda_2 = np.array(tanda_2)

    return tanda_1, tanda_2


def activation_func(x):
    return np.where(x >= 0, 1, 0)


def predict(X, weights, bias):
    linear_output = np.dot(X, weights) + bias
    y_predicted = activation_func(linear_output)
    return y_predicted




X, y = make_blobs(n_samples=50, n_features=2, centers=2, random_state=2, cluster_std=1.1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25,random_state=123)

print("Muestras para Testeo",len(X_test))
print("Muestras para Entrenamiento",len(X_train))

percept = Perceptron()
error = percept.fit(X_train, y_train)
predicciones = percept.predict(X_test)

print("La accuracy del perceptron es: ", accuracy(y_test, predicciones))
print("Los pesos son: ", percept.weights, " y el BIAS es: ", percept.bias)
print("Por lo tanto la recta nos queda como: ", percept.weights[0], "*x1 +", percept.weights[1], "*x2+", percept.bias,"=0")

# Grafico
x = np.linspace(-4, 4, 1000)
plt.plot(x, (-percept.weights[0] / percept.weights[1]) * x + (-percept.bias / percept.weights[1]), linestyle='dashed')
plt.scatter(X_test[:, 0], X_test[:, 1])
plt.title("Puntos y recta del Perceptron")
plt.xlabel("x1")
plt.ylabel("x2")
plt.show()

# tengo que dividir mi conjunto de datos en las 2 clases y operar ahi
print("Dividimos el conjunto en las clases: ")

clase_1 = []
clase_2 = []
for i in range(len(X_test)):
    if percept.predict(X_test[i]) == 1:
        clase_1.append(X_test[i])
    else:
        clase_2.append(X_test[i])

clase_1 = np.array(clase_1)
clase_2 = np.array(clase_2)

print("Clase 1","\n",clase_1)
print("Clase 2","\n",clase_2)
print("\n")

print("A partir de aca buscamos los puntos que esten mas cerca del la recta formada por los pesos y el bias del perceptron: ")
vectores_soporte = 3 # Voy a tomar 3 puntos de cada clase

print("-----> Para la clase 1") # Calculo las distancias a todos los puntos
distancias = []
for i in range(len(clase_1)):
    d = shortest_distance(clase_1[i, 0], clase_1[i, 1], percept.weights[0], percept.weights[1], percept.bias)
    distancias.append(d)
    print("El indice: ", i, "La distancia para el punto: ", clase_1[i], "es", d)
distancias = np.array(distancias)
print("Las distancias de todos los puntos ordenadas", np.sort(distancias))
print("las ", vectores_soporte, " distancias minimas son: ", np.sort(distancias)[0:vectores_soporte])# Me quedo con las minimas
maximos = np.sort(distancias)[0:vectores_soporte]
puntos_dist_min_1 = []
for i in range(len(maximos)):
    indice = np.where(distancias == maximos[i])[0][0]
    puntos_dist_min_1.append(clase_1[indice])
    print("Que corresponden con el indice: ", indice, "El punto en este indice es: ", puntos_dist_min_1[i])
puntos_dist_min_1 = np.array(puntos_dist_min_1)

print("-----> Para la clase 2")# Calculo las distancias a todos los puntos
distancias = []
for i in range(len(clase_2)):
    d = shortest_distance(clase_2[i, 0], clase_2[i, 1], percept.weights[0], percept.weights[1], percept.bias)
    distancias.append(d)
    print("El indice: ", i, "La distancia para el punto: ", clase_2[i], "es", d)
distancias = np.array(distancias)
print("Las distancias de todos los puntos ordenadas", np.sort(distancias))
print("las", vectores_soporte, "distancias minimas son: ", np.sort(distancias)[0:vectores_soporte])# Me quedo con las minimas
maximos = np.sort(distancias)[0:vectores_soporte]

puntos_dist_min_2 = []
for i in range(len(maximos)):
    indice = np.where(distancias == maximos[i])[0][0]
    puntos_dist_min_2.append(clase_2[indice])
    print("Que corresponden con el indice: ", indice, "El punto en este indice es: ", puntos_dist_min_2[i])
puntos_dist_min_2 = np.array(puntos_dist_min_2)

x = np.linspace(-4, 4, 1000)
plt.plot(x, (-percept.weights[0] / percept.weights[1]) * x + (-percept.bias / percept.weights[1]), linestyle='dashed')
plt.scatter(X_test[:, 0], X_test[:, 1])
plt.scatter(puntos_dist_min_1[:, 0], puntos_dist_min_1[:, 1], marker='d')
plt.scatter(puntos_dist_min_2[:, 0], puntos_dist_min_2[:, 1], marker='v')
plt.title("Puntos mas cercanos a la recta del perceptron")
plt.xlabel("x1")
plt.ylabel("x2")
plt.show()

# Con estas cosas puedo calcular la recta que pasa por 2 puntos

x2 = puntos_dist_min_1[0][0]
y2 = puntos_dist_min_1[0][1]

x1 = puntos_dist_min_1[1][0]
y1 = puntos_dist_min_1[1][1]

m = (y1 - y2) / (x1 - x2)
b = (x1 * y2 - x2 * y1) / (x1 - x2)

# plt.plot(x, m * x + b, linestyle='dashed')
# plt.show()

tanda1, tanda2 = tandas(puntos_dist_min_1, puntos_dist_min_2)# Divido los puntos de la clase 1 y 2 en 3 grupos de 2

# <------------------------------------------------------------------------------------------------------------------->
# CLASE 1

i = 0
candidatos1 = [] # aca quiero guardar las posibles rectas
while i < 3:  # tanda 1 y tanda 2
    m = 0
    b = 0

    x2 = tanda1[i][0][0]
    y2 = tanda1[i][0][1]

    x1 = tanda1[i][1][0]
    y1 = tanda1[i][1][1]

    m = (y1 - y2) / (x1 - x2)
    b = (x1 * y2 - x2 * y1) / (x1 - x2)

    distancia = []
    for value in range(3):
        distancia.append(shortest_distance(puntos_dist_min_2[value][0], puntos_dist_min_2[value][1], m, -1, b))
    for dist in range(len(distancia)):
        pesos = [-m, 1]
        bias = b - distancia[dist]/2
        y_result = predict(X_test, pesos, -bias)
        pesos = [m, 1]
        print("\n")
        print("El accuracy es: ", accuracy(y_test, y_result))
        if accuracy(y_test, y_result) == 1:
            candidatos1.append([pesos,-bias])
            print(pesos, bias)
            print(y_result)
            print(y_test)
    i = i + 1


print("Los candidatos de la clase 1:","\n",candidatos1)

for i in range(len(candidatos1)):
    m = candidatos1[i][0][0]
    b = candidatos1[i][1]
    x = np.linspace(-4, 4, 1000)
    plt.plot(x, (-percept.weights[0] / percept.weights[1]) * x + (-percept.bias / percept.weights[1]),
                 linestyle='dashed')  # recta del perceptron
    plt.scatter(X_test[:, 0], X_test[:, 1])
    plt.scatter(puntos_dist_min_1[:, 0], puntos_dist_min_1[:, 1], marker='d')
    plt.scatter(puntos_dist_min_2[:, 0], puntos_dist_min_2[:, 1], marker='v')
    plt.plot(x, m * x - b)
    plt.title("Rectas candidatas de la clase 1*")
    plt.xlabel("x1")
    plt.ylabel("x2")
plt.show()

minimo_total = []
for value in range(len(candidatos1)):
    m = candidatos1[value][0][0]
    b = candidatos1[value][1]
    print("-----> Para la clase 1")  # Calculo las distancias a todos los puntos
    distancias1 = []
    for i in range(len(clase_1)):
        d = shortest_distance(clase_1[i, 0], clase_1[i, 1], m, 1, -b)
        distancias1.append(d)
        print("El indice: ", i, "La distancia para el punto: ", clase_1[i], "es", d)
    min1 = min(distancias1)

    print("-----> Para la clase 2")  # Calculo las distancias a todos los puntos
    distancias2 = []
    for i in range(len(clase_2)):
        d = shortest_distance(clase_2[i, 0], clase_2[i, 1], m, 1, -b)
        distancias2.append(d)
        print("El indice: ", i, "La distancia para el punto: ", clase_2[i], "es", d)
    min2 = min(distancias2)

    minimo_total.append(min(min1,min2))

min_1 = max(minimo_total)
print("La mejor recta de la clase 1 es:",candidatos1[(minimo_total).index(max(minimo_total))], "con una margen minima de: ",min_1)
m = candidatos1[(minimo_total).index(max(minimo_total))][0][0]
b = candidatos1[(minimo_total).index(max(minimo_total))][1]

x = np.linspace(-4, 4, 1000)
plt.plot(x, (-percept.weights[0] / percept.weights[1]) * x + (-percept.bias / percept.weights[1]),
             linestyle='dashed')  # recta del perceptron
plt.scatter(X_test[:, 0], X_test[:, 1])
plt.scatter(puntos_dist_min_1[:, 0], puntos_dist_min_1[:, 1], marker='d')
plt.scatter(puntos_dist_min_2[:, 0], puntos_dist_min_2[:, 1], marker='v')
plt.plot(x, m * x - b)
plt.title("Recta seleccionada de la clase 1")
plt.xlabel("x1")
plt.ylabel("x2")
plt.show()

# <------------------------------------------------------------------------------------------------------------------->
# CLASE 2

i = 0
candidatos2 = [] # aca quiero guardar las posibles rectas
while i < 3:  # tanda 1 y tanda 2
    m = 0
    b = 0

    x2 = tanda2[i][0][0]
    y2 = tanda2[i][0][1]

    x1 = tanda2[i][1][0]
    y1 = tanda2[i][1][1]

    m = (y1 - y2) / (x1 - x2)
    b = (x1 * y2 - x2 * y1) / (x1 - x2)

    # aca la recta por si las quiero ver
    distancia = []
    for value in range(3):
        distancia.append(shortest_distance(puntos_dist_min_1[value][0], puntos_dist_min_1[value][1], m, -1, b))
    for dist in range(len(distancia)):
        pesos = [-m, 1]
        bias = b + distancia[dist]/2
        print("Para esta recta tenemos un b de", b, "y un bias de:",bias)
        y_result = predict(X_test, pesos, -bias)
        pesos = [m, 1]
        print("\n")
        print("El accuracy es: ", accuracy(y_test, y_result))
        plt.plot(x, m * x + bias)  # GRAFICO

        if accuracy(y_test, y_result) == 1:
            candidatos2.append([pesos,-bias])
            print(pesos, bias)
            print(y_result)
            print(y_test)
    i = i + 1


print("Los candidatos de la clase 2:","\n",candidatos2)

for i in range(len(candidatos2)):
    m = candidatos2[i][0][0]
    b = candidatos2[i][1]
    x = np.linspace(-4, 4, 1000)
    plt.plot(x, (-percept.weights[0] / percept.weights[1]) * x + (-percept.bias / percept.weights[1]),
                 linestyle='dashed')  # recta del perceptron
    plt.scatter(X_test[:, 0], X_test[:, 1])
    plt.scatter(puntos_dist_min_1[:, 0], puntos_dist_min_1[:, 1], marker='d')
    plt.scatter(puntos_dist_min_2[:, 0], puntos_dist_min_2[:, 1], marker='v')
    plt.plot(x, m * x - b)
    plt.title("Rectas candidatas de la clase 2*")
    plt.xlabel("x1")
    plt.ylabel("x2")
plt.show()

minimo_total = []
for value in range(len(candidatos2)):
    m = candidatos2[value][0][0]
    b = candidatos2[value][1]

    print("-----> Para la clase 1")  # Calculo las distancias a todos los puntos
    distancias1 = []
    for i in range(len(clase_1)):
        d = shortest_distance(clase_1[i, 0], clase_1[i, 1], m, 1, -b)
        distancias1.append(d)
        print("El indice: ", i, "La distancia para el punto: ", clase_1[i], "es", d)
    min1 = min(distancias1)

    print("-----> Para la clase 2")  # Calculo las distancias a todos los puntos
    distancias2 = []
    for i in range(len(clase_2)):
        d = shortest_distance(clase_2[i, 0], clase_2[i, 1], m, 1, -b)
        distancias2.append(d)
        print("El indice: ", i, "La distancia para el punto: ", clase_2[i], "es", d)
    min2 = min(distancias2)

    minimo_total.append(min(min1,min2))


minimo_2=max(minimo_total)

print("La mejor recta de la clase 2 es:",candidatos2[(minimo_total).index(max(minimo_total))], "con una margen minima de: ",minimo_2)
m = candidatos2[(minimo_total).index(max(minimo_total))][0][0]
b = candidatos2[(minimo_total).index(max(minimo_total))][1]
x = np.linspace(-4, 4, 1000)
plt.plot(x, (-percept.weights[0] / percept.weights[1]) * x + (-percept.bias / percept.weights[1]),
             linestyle='dashed')  # recta del perceptron
plt.scatter(X_test[:, 0], X_test[:, 1])
plt.scatter(puntos_dist_min_1[:, 0], puntos_dist_min_1[:, 1], marker='d')
plt.scatter(puntos_dist_min_2[:, 0], puntos_dist_min_2[:, 1], marker='v')
plt.plot(x, m * x - b)
plt.title("Recta seleccionada de la clase 2")
plt.xlabel("x1")
plt.ylabel("x2")
plt.show()


print("\n")
print("La mejor recta de la clase 1 es:",candidatos1[(minimo_total).index(max(minimo_total))], "con una margen minima de: ",min_1)
print("La mejor recta de la clase 2 es:",candidatos2[(minimo_total).index(max(minimo_total))], "con una margen minima de: ",minimo_2)


x = np.linspace(-4, 4, 1000)
plt.plot(x, (-percept.weights[0] / percept.weights[1]) * x + (-percept.bias / percept.weights[1]),
             linestyle='dashed')  # recta del perceptron
plt.scatter(X_test[:, 0], X_test[:, 1])
plt.scatter(puntos_dist_min_1[:, 0], puntos_dist_min_1[:, 1], marker='d')
plt.scatter(puntos_dist_min_2[:, 0], puntos_dist_min_2[:, 1], marker='v')

m = candidatos1[(minimo_total).index(max(minimo_total))][0][0]
b = candidatos1[(minimo_total).index(max(minimo_total))][1]
plt.plot(x, m * x - b)
plt.title("Hiperplano Optimo")
plt.xlabel("x1")
plt.ylabel("x2")
plt.show()

SVM = svm.SVC(kernel='linear',degree=3,C=1000)
SVM.fit(X_test, y_test)
plot_decision_regions(X_test, y_test, clf=SVM)
plt.title("Sobre el conjunto de Testeo")
plt.xlabel("x1")
plt.ylabel("x2")
plt.show()
