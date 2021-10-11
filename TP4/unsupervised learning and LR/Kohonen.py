import pandas as pd
import numpy as np
import matplotlib.pyplot as plt# Para visualizar
import seaborn as sns# Para visualizar
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report


# Implementacion de redes de Kohonen


df = pd.read_csv(r'/Users/juanmedina1810/PycharmProjects/Machine_Learning/TP4/TP/acath.csv').interpolate()
datos_maximos = len(df)
datos = df.drop(['sex','tvdlm'], axis=1).dropna()
datos.reset_index(inplace=True,drop = True)

y_true = datos['sigdz']# Para despues evaluar la comparacion
datos = datos.drop(['sigdz'], axis=1)

data = np.array(datos)# Voy a trabajar con los datos en forma de Array de numpy
y_true = np.array(y_true)


class kohonen:

    def __init__(self, data, net_dim, n_iter, init_learning_rate):

        self.data = data
        self.init_learning_rate = init_learning_rate
        self.n_iter = n_iter# Limite de iteraciones
        self.init_radius = 2*np.sqrt(2)# El radio inicial, comienza compitiendo con los nodos que estan cercanos

        self.net = np.random.random((net_dim[0], net_dim[1], data.shape[1]))# Los nodos se inicializan con valores random

    def _cal_euc(self, x, y):# Distancia Euclidea
        return np.sqrt(np.sum((x - y) ** 2))

    def normalizar(self):
        max = self.data.max()
        print("El max es:")
        self.data = self.data / self.data.max()
        return max

    def Neurona_ganadora(self, t):
        dist_minima = 1000 # Una distancia minima arbitraria que nos va a permitir entrar al If de abajo

        for i in range(self.net.shape[0]):# Recorro fila
            for j in range(self.net.shape[1]):# Recorro columna

                dist = self._cal_euc(self.net[i, j], t)# La distancia entre un punto de la matrix de pesos y el vector e

                if dist < dist_minima:# En esta iteracion nos quedamos con la menor (En la primera iteracion entra seguro)
                    bmu = self.net[i, j]
                    bmu_id = np.array([i, j])

        return bmu, bmu_id # Devuelvo el vector mas cercano y su indice (Posicion en la matrix de pesos)

    def Eta_decaimiento(self, i):# El Eta decae linealmente (Clase)
        return self.init_learning_rate * (1-i/self.n_iter)

    def R_decaimiento(self, i):# El radio decae exponencialmente (Yo lo prefiero asi)
        return self.init_radius * np.exp(-i)

    def V_param(self, radius, dist):# Parametro V visto en clase, tambien exponencial
        return np.exp(-2*dist / radius)

    def train(self):

        for k in range(self.n_iter):# El numero de iteraciones afecta el entrenamiento

            t = self.data[np.random.randint(0, self.data.shape[0]), :]# Agarro un vector al azar

            bmu, bmu_id = self.Neurona_ganadora(t)# Encuento la neurona que esta a menor distancia (La neurona y su indice)

            l = self.Eta_decaimiento(k)# el eta decae
            r = self.R_decaimiento(k)# El radio decae (Notar que esto es despues de encontrar la neurona ganadora)

            for i in range(self.net.shape[0]):# Recorro las filas
                for j in range(self.net.shape[1]):# Recorro las columnas

                    grid_node = np.array([i, j])# genero un ID de nodo

                    dis = self._cal_euc(grid_node, bmu_id)# distancia desde la grilla a la ganadora

                    if dis < r:# Solo se van a actualizar los pesos mas cercanos

                        V = self.V_param(r, dis)# Calculo el parametro V
                        w = self.net[i, j]# Agarro un nodo de la matriz (Peso viejo)

                        new_w = w + (l * V * (t - w))# Ecuacion de apredizaje (Actualizo el peso)

                        self.net[i, j] = new_w# Modifico el valor de la matriz con el nuevo peso

        matrix_de_pesos = self.net# Esta matrix nos va a guardar los pesos que resultan despues de todas las iteraciones

        return matrix_de_pesos

    def matrix_u(self):# Matrix que nos va dar la visualizacion

        self.u_matrix = np.zeros((self.net.shape[0], self.net.shape[1]))# Matrix en blanco

        for i in range(0, self.net.shape[0]):# Recorro las filas
            for j in range(0, self.net.shape[1]):# recorro las columnas

                sum_dist = 0 # Cuantas veces se activo cada neurona
                ct = 0 # parametro que voy a usar para promediar

                # Voy a tomar la distancia de la neurona con sus vecinos y luego lo promedio
                if i - 1 >= 0:
                    sum_dist = sum_dist + self._cal_euc(self.net[i, j], self.net[i - 1, j])# La fila de arriba en la misma columna
                    ct = ct + 1

                if i + 1 <= self.net.shape[0] - 1:
                    sum_dist = sum_dist + self._cal_euc(self.net[i, j], self.net[i + 1, j])# La fila de abajo en la misma columna
                    ct = ct + 1


                if i - 1 >= 0 and j + 1 <= self.net.shape[1] - 1:
                    sum_dist = sum_dist + self._cal_euc(self.net[i, j], self.net[i - 1, j + 1])# la fila de arriba y la columna de la derecha
                    ct = ct + 1


                if i - 1 >= 0 and j - 1 >= 0:
                    sum_dist = sum_dist + self._cal_euc(self.net[i, j], self.net[i - 1, j - 1])# a fila de arriba y la columna de la izquierda
                    ct = ct + 1

                if j - 1 >= 0:
                    sum_dist = sum_dist + self._cal_euc(self.net[i, j], self.net[i, j - 1])# La columna de la izquierda en la mima fila
                    ct = ct + 1

                if j + 1 <= self.net.shape[1] - 1:
                    sum_dist = sum_dist + self._cal_euc(self.net[i, j], self.net[i, j + 1])# La columna de la derecha en la misma fila
                    ct = ct + 1


                if i + 1 <= self.net.shape[0] - 1 and j - 1 >= 0:
                    sum_dist = sum_dist + self._cal_euc(self.net[i, j], self.net[i + 1, j - 1])# la fila de abajo y la columna de la izquierda
                    ct = ct + 1


                if i + 1 <= self.net.shape[0] - 1 and j + 1 <= self.net.shape[1] - 1:
                    sum_dist = sum_dist + self._cal_euc(self.net[i, j], self.net[i + 1, j + 1])# la fila de abajo y la columna de la derecha
                    ct = ct + 1

                self.u_matrix[i, j] = sum_dist / ct

        return self.u_matrix


kohonen_net = kohonen(data,net_dim=(4,4),n_iter=2000,init_learning_rate=0.1)
maximo = kohonen_net.normalizar()
pesos = kohonen_net.train()# Matrix de pesos

print("La matriz de pesos nos queda:","\n",pesos)
matrix_u = kohonen_net.matrix_u()


# Quiero poder clasificar el resultado que me da el metodo, lo voy a hacer a partir del

print(matrix_u)

max1 = 0
for i in range(matrix_u.shape[0]):# filas
    for j in range(matrix_u.shape[1]):# Column
        value = matrix_u[i][j]
        if value > max1:
            max1 = value
            index_max = [i,j]

print("El indice del maximo es:",index_max)
print("El maximo es:",maximo)
print("El peso que mas se mostro:",pesos[index_max[0]][index_max[1]])
sns.heatmap(matrix_u)
plt.show()
maximo_vector = pesos[index_max[0]][index_max[1]]
"""Acordate que esta tode normalizado"""


umbral = 0.56 # La idea es poder elegir el umbral que meximize el Accuracy
data = data/maximo

def clasificador(data,maximo_vector):
    umbral = 0.598
    y_pred = []
    for i in range(len(data)):
        if np.abs(np.linalg.norm(data[i]-maximo_vector))**2<umbral:
            y_pred.append(1)
        else:
            y_pred.append(0)
    y_pred = np.array(y_pred)
    return y_pred


y_pred = clasificador(data,maximo_vector)
cm = confusion_matrix(y_true, y_pred)
sns.heatmap(cm, annot=True, fmt="d")
plt.show()
print(classification_report(y_true, y_pred))