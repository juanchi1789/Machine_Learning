import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import statsmodels.api as sm


df =pd.read_csv(r'/Users/juanmedina1810/PycharmProjects/Machine_Learning/TP4/TP/acath.csv').interpolate()
print(df)

# Armamos X e Y
X = sm.add_constant(df[['age', 'cad.dur','choleste']])
y = df['sigdz']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.10,random_state=123)
print(len(y_train))
print(np.sum(y_train==1))
print(np.sum(y_train==0))

umbral = 0.5

# Regresion Logistica ------------------------------------------> sin el sexo

log_reg_1 = sm.Logit(y_train,X_train).fit()
print(log_reg_1.summary())
y_pred = log_reg_1.predict(X_test)
y_pred = np.where(y_pred > umbral,1,0)
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt="d")
plt.title("Matriz de confusion sin el Sexo")
plt.show()
print(classification_report(y_test, y_pred))


# Regresion Logistica ------------------------------------------> con el sexo

X = sm.add_constant(df[['sex','age', 'cad.dur','choleste']])
y = df['sigdz']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.10)

log_reg = sm.Logit(y_train,X_train).fit()
print(log_reg.summary())
y_pred = log_reg.predict(X_test)
y_pred = np.where(y_pred > umbral,1,0)
cm = confusion_matrix(y_test, y_pred)

sns.heatmap(cm, annot=True, fmt="d")
plt.title("Matriz de confusion con el Sexo")
plt.show()
print(classification_report(y_test, y_pred))
print("\n")

# Regresion Logistica ------------------------------------------> calculo con los coeficientes

# Colesterol: 199
# edad : 60
# duracion : 2

"""
Los parametros B1,B2,B3 los podemos obtener directamente con la libreria
"""

logit = np.sum(log_reg_1.params * [1,60,2,199])

p= np.exp(logit)/(1+np.exp(logit))
print("La probabilidad de que el paciente tenga una enfermedad cardiaca es:",round(p,4))
# La probabil