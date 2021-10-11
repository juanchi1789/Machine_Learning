import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import plotly.express as px



df = pd.read_csv(r'/Users/juanmedina1810/PycharmProjects/Machine_Learning/TP4/TP/acath.csv').interpolate()
print(df)
# <--------------------------------------------------------------------> Implementamos el metodo de K_medias


def var_x_class(clase):  # variación de una clase
    var = 0
    copia = clase.copy()
    size = len(clase)
    for i, j in copia.iterrows():  # Voy iterando sobre las filas de dataset

        var = var + ((clase - j) ** 2).sum().sum()  # La primera suma corresponde a la diferencia al
                                                    # cuadrado de los vectores "clase" y "j", hasta
                                                    # ahi tenemos un vector

        #var = var.sum()  # Aca se suman los componentes del vector "var"
        clase.drop(i, inplace=True)  # Elimino la fila que ya calcule para evitar calcular varias veces

    return var / size  # devuelvo la

def var_total(data, k):  # Entrega la suma de las variabilidade de las clases
    suma = 0
    for i in range(0, k):
        data_class = data.loc[data["clase"] == i].drop("clase", axis=1)
        suma = suma + var_x_class(data_class)
    return suma

def distancia_euc(x, y):
    return np.linalg.norm(x - y)

def k_means(data, k, umbral, max_iters=25):

    dat = data

    xx = 0 # esta variable la vamos a usar para cortar con el maximo de iteraciones

    clase = np.random.randint(0, k, size=len(data))  # Inicialmente las clases se asignan aleatoriamente
    data["clase"] = clase
    print("La data:","\n",data)

    centroides = [0 for _ in range(k)] # Voy a tener tantos centroides como "K" yo especifique

    print("Los centroides:",centroides)

    variabilidad1 = var_total(data, k)# Comenzamos con una variabilidad incial que es la que le corresponde a los datos cuando
                                      # se les asigna una clase aleatoria

    print("La primera variabilidad es:",variabilidad1)

    variabilidad0 = 2 * variabilidad1# Esto nos va a servir para entrar al while que esta abajo

    variabilidades = []  # Donde voy a guardar las variabilidades para poder graficar despues

    while variabilidad0 - variabilidad1 >= umbral * variabilidad1 and xx < max_iters:
        # Este while nos va a permitir romper la ejecucion del programa cuando la tasa de cambio de la variabilidad sea
        # muy cercana a cero o cuando se supere el numero de iteraciones maximas

        variabilidades.append(variabilidad1)

        variabilidad0 = variabilidad1# fijo la variabilidad anterior

        print("Iteracion numero:", xx)

        for i in range(0, k):
            centro = data.loc[data["clase"] == i].mean()  # Calculo del centroide a partir de la media
                                                          # el centroide correponde con la media de las componentes
                                                          # de los vectores de la clase

            centroides[i] = centro.drop("clase")# tengo que eliminar la clase del centroide

        print("EL centroide es:","\n",centroides)

        # Ya con los centroides nuevos ajusto las clases a los nuevos centroides:

        for i, x in dat.iterrows():

            cl = 0
            x = x.drop('clase')
            d = np.dot(x - centroides[0], x - centroides[0])# Fijo la distancia al primer centroide

            for h in range(1,k):
                d1 = np.dot(x - centroides[h], x - centroides[h])  # norma cuadrada entre el ejemplo x y el cetroide de la clase c
                if d1 < d:
                    cl = h
                    d = d1

            data.loc[i, "clase"] = cl  # nos quedamos con la clase que minimiza la distancia al centroide

        variabilidad1 = var_total(data, k) # Se calcula la nueva variabilidad total

        xx = xx + 1

    return data, variabilidades # Nos devuelve los datos con las clases calculadas y el vector de las variabilidades




data = df.drop(['sex', 'sigdz', 'tvdlm'], axis=1).dropna()  # Elimino las columnas que no quiero en el sistema
y_fin = df['sigdz']
k = 2
print(data)

data_clasificada,variabilidades = k_means(data,k,0.0001,max_iters=50)
plt.plot(variabilidades)
plt.grid(True)
plt.show()
y_pred = data_clasificada['clase']

data_clasificada['clase_true'] = y_fin
print(data_clasificada)
data_array = np.array(data_clasificada)
print(data_array)


cm = confusion_matrix(y_fin, y_pred)
sns.heatmap(cm, annot=True, fmt="d")
plt.show()
print(classification_report(y_fin, y_pred))


df_graph = pd.DataFrame(data=data_clasificada,index= np.linspace(0,len(data_clasificada)-1,num= len(data_clasificada)).astype(int),
                        columns=['age', 'cad.dur', 'choleste','clase'])
df_graph['species'] = 0
df_graph.loc[df_graph['clase'] == 0, 'species'] = '0'
df_graph.loc[df_graph['clase'] == 1, 'species'] = '1'

fig = px.scatter_3d(df_graph, x='age', y='cad.dur', z='choleste',
              color='species', opacity=1)
fig.show()
