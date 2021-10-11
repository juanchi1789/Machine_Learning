# Linear Regresion

import pandas as pd
import numpy as np
import sklearn
import seaborn
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn import metrics
from scipy import stats
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import statsmodels.api as sm
from statsmodels.sandbox.regression.predstd import wls_prediction_std


def linear_reg(variable_obj, variable_x):
    y = df[[variable_obj]]
    X = df[[variable_x]]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=123)
    lr = LinearRegression()
    lr.fit(X_train, y_train)
    y_pred = lr.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    plt.scatter(X, y, color='black')
    plt.plot(X_test, y_pred, color='blue', linewidth=3)
    plt.title(variable_obj + ' vs ' + variable_x)
    plt.xlabel(variable_obj)
    plt.ylabel(variable_x)
    ##plt.show()
    plt.clf()

    #y_test = np.where(y_test < 10, 'Baja', (np.where(y_test < 15, 'Media', 'Alta')))
    #y_predicted = np.where(y_pred < 10, 'Baja', (np.where(y_pred < 15, 'Media', 'Alta')))

    #matrix = confusion_matrix(y_test, y_predicted)
    #ax = seaborn.heatmap(matrix, annot=True, fmt="d")
    #plt.title("Matriz de confusion de " + variable_obj +" vs "+ variable_x)
    #plt.xlabel("Real")
    #plt.ylabel("Predicted")
    #plt.show()

    #print("Metricas")
    #print(classification_report(y_test, y_predicted))


    print("El termino indep es:", lr.intercept_)
    print("El coeficiente es:", lr.coef_[0][0])
    print("R2:", r2)
    #print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
    #print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
    print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

    print("\n")


# ---->Correlacion entre las variables<----

# Load data

df = pd.read_csv("Advertising.csv")
df = df[["TV", "Radio", "Newspaper", "Sales"]]
# print(df.head())
# print(df.corr())
# print("\n")

seaborn.heatmap(df.corr(), annot=True)
plt.title("Matriz de correlacion")
plt.show()

# seaborn.pairplot(df)
# plt.title("Pair plot")
# plt.show()


# ---->MODELOS DE REGRESION LINEAL SIMPLE<----

# DATA:
tv = df["TV"]
radio = df["Radio"]
news = df["Newspaper"]
sales = df["TV"]

# <------>

# (1) Tv vs Sales

linear_reg("Sales", "TV")

# <------>
# (2) Radio vs Sales
linear_reg("Sales", "Radio")
# <------>
# (3) Newspaper vs Sales
linear_reg("Sales", "Newspaper")
# <------>

# DIAGNOSTICO:

# ---->MODELOS DE REGRESION LINEAL MULTIPLE<----

y = df["Sales"]
X = df[["TV", "Radio", "Newspaper"]]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=123)

lr = LinearRegression()
lr.fit(X_train, y_train)
y_predicted = lr.predict(X_test)
r2 = r2_score(y_test, y_predicted)

# DIAGNOSTICO:
print("El termino indep es:", lr.intercept_)
print("El coeficiente es:", lr.coef_)
print("R2:", r2)

#print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_predicted))
#print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_predicted))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_predicted)))

# SIN CONSIDERAR EL DIARIO

print("\n")

y = df["Sales"]
X = df[["TV", "Radio"]]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=123)

lr2 = LinearRegression()
lr2.fit(X_train, y_train)
y_predicted = lr2.predict(X_test)
r22 = r2_score(y_test, y_predicted)

# DIAGNOSTICO:
print("El termino indep es:", lr2.intercept_)
print("El coeficiente es:", lr2.coef_)
print("R2:", r22)
#print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_predicted))
#print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_predicted))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_predicted)))

y_test = np.where(y_test < 10, 'Baja', (np.where(y_test < 15, 'Media', 'Alta')))
y_predicted = np.where(y_predicted < 10, 'Baja', (np.where(y_predicted < 15, 'Media', 'Alta')))

matrix = confusion_matrix(y_test, y_predicted)
ax = seaborn.heatmap(matrix, annot=True, fmt="d")

plt.title("Matriz de confusion de la Regresion multivariada")
plt.xlabel("Real")
plt.ylabel("Predicted")
plt.show()
print("Metricas")
print(classification_report(y_test, y_predicted))



