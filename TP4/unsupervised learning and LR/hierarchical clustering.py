from turtle import distance

import pandas as pd
import numpy as np

df = pd.read_csv(r'/Users/juanmedina1810/PycharmProjects/Machine_Learning/TP4/TP/acath.csv').interpolate()

datos_maximos = 5

datosx = df.drop(['sex','tvdlm'], axis=1).dropna().sample(n=datos_maximos, random_state = 12)# Tomo menos datos para mejor visualizacion
datosx.reset_index(inplace=True,drop = True)

y_true = datosx['sigdz']# Para despues evaluar la comparacion
#datosx['clase'] = datosx.index
datosx = datosx.drop(['sigdz'], axis=1)
datos = np.array(datosx)
print(datos,"\n")# En modo de arreglo
vvv = []
for i in range(len(datos)):
    vvv.append(list(datos[i]))
    vvv[i] = (vvv[i],)


def is_leaf(cluster):

    return len(cluster) == 1

def get_children(cluster):
    if is_leaf(cluster):
        raise TypeError("No tiene hijos esto")
    else:
        return cluster[1]

def get_values(cluster):

    """
    Nos da el valor del cluster, si es una hoja
    o todos los valores en la hoja de clusters
    """

    if is_leaf(cluster):
        return cluster # Solo es 1 cluster conteniendo 1 valor
    else:
        return [value for child in get_children(cluster) for value in get_values(child)]


def cluster_distance(cluster1, cluster2, distance_agg=min):

    return distance_agg([distance(input1, input2)for input1 in get_values(cluster1)for input2 in get_values(cluster2)])

def get_merge_order(cluster):
    if is_leaf(cluster):
        return 1000000
    else:
        return cluster[0]

def bottom_up_cluster(inputs, distance_agg=min):
    clusters = [(input,) for input in inputs]
    while len(clusters) > 1:
        c1, c2 = min([(cluster1, cluster2) for i, cluster1 in enumerate(clusters) for cluster2 in clusters[:i]], key=lambda x, y: cluster_distance(x, y, distance_agg))

        clusters = [c for c in clusters if c != c1 and c != c2]
        merged_cluster = (len(clusters), [c1, c2])
        clusters.append(merged_cluster)
    return clusters[0]


c1 = vvv[0]
c2 = vvv[1]

merged_cluster = (len(vvv), [c1, c2])
print(merged_cluster)
print(get_values(c1))
print(get_values(c2))
print(get_values(c1)+get_values(c2))
#base_cluster = bottom_up_cluster(vvv)
#print(base_cluster)



def agr_jer(data):
    dic = {}
    maxi = max(data.index)
    i = 0
    original = data.copy()
    while len(data) > 1:

        i = i + 1
        ind, min = distancia(data.copy())

        if ind[0] <= maxi and ind[1] <= maxi:
            a = ind

        elif ind[0] > maxi and ind[1] <= maxi:
            a = dic[ind[0]][4] + [ind[1]]

        elif ind[0] <= maxi and ind[1] > maxi:
            a = dic[ind[1]][4] + [ind[0]]

        else:
            a = dic[ind[0]][4] + dic[ind[1]][4]

        dic[maxi + i] = [ind[0], ind[1], min, len(a), a]

        centroide = original.loc[a, :].mean()
        centroide.name = maxi + i
        data = data.append(centroide).copy()
        data.drop(ind, inplace=True)

    matrix = np.zeros([len(original) - 1, 4])
    c = 0
    for j in dic.keys():
        matrix[c, :] = dic[j][0:4]
        c += 1

    return matrix, dic

def distancia(data):
    ind = data.index[0]
    min = None
    for i, j in data.iterrows():
        distance = ((((data - j) ** 2).sum(axis=1)) ** (0.5))
        distance = distance.copy().to_numpy()
        if len(distance) > 1:
            min1 = np.min(distance[1:])
        data.drop(i, inplace=True)
        if min == None or min > min1:
            min = min1
            arg = np.argmin(distance[1:])
            ind = [i, data.index[arg]]

    return ind, min

def dist(pointA, pointB):
    res = (pointA - pointB) ** 2
    return np.sqrt(np.sum(res))

def matrix_dist(datos):
    #datos = datos.drop(['clase'], axis=1)
    #datos = np.array(datos)
    matrix = np.zeros((len(datos), len(datos)))
    try:
        for index1, cords1 in enumerate(datos):
            for index2, cords2 in enumerate(datos):
                if index1<=index2:
                    matrix[index1][index2] = 1000
                else:
                    matrix[index1][index2] = dist(cords1, cords2)
    except:
        print("El Krusty el payaso")
    return matrix

datos = np.array(datosx.copy().drop(['clase'],axis=1))

matrix = matrix_dist(datos)
print(matrix)
clusters = list(range(0, len(datos)))
print("clusters",clusters)
minimos = np.where(matrix == matrix.min())
clusters.remove(minimos[0])
clusters.remove(minimos[1])
min0 = list(minimos[0])[0]
min1 = list(minimos[1])[0]
clusters.append([min0,min1])
print("nuevos clusters",clusters)
print("Los datos quedan:", "\n", datos)

