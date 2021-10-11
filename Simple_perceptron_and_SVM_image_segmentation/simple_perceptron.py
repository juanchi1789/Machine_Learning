

import numpy as np


class Perceptron:

    def __init__(self, learning_rate=0.1, n_iters=50):
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
            print("iter ", i)
            error = 0
            for idx, x_i in enumerate(X):
                linear_output = np.dot(x_i, self.weights) + self.bias
                y_predicted = self.activation_func(linear_output)
                update = self.lr * (y[idx] - y_predicted)
                self.weights += update * x_i
                self.bias += update * 1
                if y[idx] - y_predicted != 0:
                    error = error + 1
            print("El error en la tanda: ", i, " es: ", error)
            errores.append(error)
            i = i + 1
        return errores

    def predict(self, X):
        linear_output = np.dot(X, self.weights) + self.bias
        y_predicted = self.activation_func(linear_output)
        return y_predicted

    def _unit_step_func(self, x):
        return np.where(x >= 0, 1, 0)
