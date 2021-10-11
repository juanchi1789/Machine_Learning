# <-------------------------------------------------------------------------------------------------------------------->
# Ej 1: Desition Trees and Random Forest
import funciones
import random
import matplotlib.pyplot as plt
import pandas as pd  # solo para importar el archivo
import numpy as np
import math as mt

array = pd.read_csv("german_credit.csv", low_memory=False)
print(array.head())

data = array.values  # lista que contiene la información de cada individuo en forma de lista, REGISTROS TOTALES

variables = list(array.keys())
variable_obj = variables[0]
print("La variable objetivo es: " + variable_obj)

datos_totales = data
lista_duracion = []
lista_amount = []
lista_age = []
i = 0
while i < len(datos_totales):
    contador = 0
    while contador < len(datos_totales[i]):
        if contador == 2:
            lista_duracion.append(datos_totales[i][contador])
        if contador == 5:
            lista_amount.append(datos_totales[i][contador])
        if contador == 13:
            lista_age.append(datos_totales[i][contador])
        contador = contador + 1
    i = i + 1

# plt.subplot(1,3,1)
# plt.hist(lista_duracion)
# plt.title("Histograma de duracion del credito")
# plt.xlabel("Meses de duracion")
# plt.show()

# plt.subplot(1,3,2)
# plt.hist(lista_amount)
# plt.title("Histograma de Monto del credito")
# plt.xlabel("Monto del credito solicitado")
# plt.show()

# plt.subplot(1,3,3)
# plt.hist(lista_age)
# plt.title("Histograma de Edades")
# plt.xlabel("Edades")
# plt.show()


print("\n")
# <-------------------------------------------------------------------------------------------------------------------->

# Armamos los registros de entrenamiento y de testeo de forma aleatoria:

personas = list(range(0, 1000))  # indice de personas

i = 0
coef = 80
index = []
index.append(random.sample(personas, int(
    len(data) * coef / 100)))  # El indice de las personas seleccionadas para participar del entrenamiento
index[0].sort()
# print("Las personas que participan del entrenamiento son : " + str(index[0]))

entrenamiento = []
i = 0
while i < len(index):
    entrenamiento.append((data[index[i]]))
    i = i + 1

entrenamiento = entrenamiento[0]
testeo = []
personas = list(range(0, 1000))  # indice de personas
index_test = []
i = 0
while i < len(personas):
    if not (personas[i] in index[0]):
        index_test.append(personas[i])
    i = i + 1

while i < len(index_test):
    testeo.append((data[index_test[i]]))
    i = i + 1

# print("Las pesonas que participan del testeo son: " + str(index_test))
print("Los dataset fueron creados")

# <-------------------------------------------------------------------------------------------------------------------->
print("\n")
print("Empezamos a catergorizar los datos:")
print("Las variables a categorizar son: ")
print(variables[2])
print(variables[5])
print(variables[13])

# tiene que entrar una lista de listas y vos operar sobre el 2, 4 y 12 componente de cada lista interior

funciones.categorizador(entrenamiento, [2, 5, 13])

funciones.categorizador(testeo, [2, 5, 13])

print("La categorizacion termino")

# <-------------------------------------------------------------------------------------------------------------------->
# ALGORITMO ID3: con entropy de Shannon

from numpy import log2

# entropoia = -(cantidad_pos/total)*np.log2((cantidad_pos/total))-(cantidad_neg/total)*np.log2((cantidad_neg/total))

# gain = entropia(conjunto_mayor) - sum((count.valores/count.totales)*entropia(conjunto_menor))

# arbol = {}

# arbol = {"acount balance":{1:} ==> nodo raiz
# (ramas)
# {2:{"telephone":{1:{"length":....}},{2:{"svalue":...}}}
# {3:}
# {4:}
# }

# La funcion objetivo esta en la columna 0

objetivo = 0  # en nuestro caso siempre

dic = {"juan": [{"Leandro": [1, 2, 3]}, {"Lulu": [1, 2, 3]}, {"Anibal": [1, 2, 3]}]}
variables = list(array.keys())

# Me estoy dando cuenta que necesito varias cosas:

# 1) una funcion que me de la ganancia total
entropia_total = funciones.entropia_total(entrenamiento, objetivo)


# entrenamiento[0] ==> una persona

def metodos(data):
    i = 0
    metodos = []
    contador = 0
    while contador < 21:  # quiero todos los valores de cada metodo
        met = []
        i = 0
        while i < len(data):
            met.append(data[i][contador])
            i = i + 1
        contador = contador + 1
        metodos.append(met)

    return sorted(metodos)# nos da una lista, donde en cada columna tengo los valores del metodo

print("Mira")
print(metodos(data)[2])

def entropia(data,objetivo,variable,*instancia):# esto me va a dar la entropia de una instancia de una variable
    # la instancia puede ser un valor entre 1 y 10 ó 1 y 4 depende de la variable a considerar
    entropia = 0
    # Entropia general
    if variable == 0: # caso de la entropia general
        entropia = entropia_total(data,0)
        return entropia

    # Los otros casos
    else:
        met = metodos(data)  # va a tener una longitud de 21
        datos = met[variable]  # La columna que buscamos estudiar
        leng = met[variable].count(instancia)  # Cantidad de veces que aparece la instancia
        pos = 0
        neg = 0
        i = 0
        while i < len(met[variable]):
            if met[variable][i] == instancia and met[objetivo][i] == 1:
                pos = pos + 1
            if met[variable][i] == instancia and met[objetivo][i] == 0:
                neg = neg + 1
            i = i + 1
        # en este punto tengo los valores para calcular la entropia
        prob_pos = pos/leng
        prob_neg = neg/leng
        entropia = (-prob_pos*mt.log2(prob_pos))-(prob_neg*mt.log2(prob_neg)) # Los otros casos
        return entropia

def ganancia(data, objetivo, variable, general):
    met = metodos(data)  # Lista con cada metodo agregado
    datos = met[variable]  # los datos que vamos a estudiar
    if general == 1:  # se trata de calcular la ganancia del metodo completo
        valores = []
        valores = funciones.valores(data,variable)  # esto nos da un lista que tiene cada valor posible que puede tomar la variable
        ganancia = funciones.entropia_total(data, objetivo)
        resto = 0
        i = 0
        print("Estamos en general")
        while i < len(valores):  # Voy recorriendo instancia por instancia
            print("Los valores son:" +str(valores))
            print("valor: " + str(valores[i]))
            veces = met[variable].count(valores[i])  # cantidad de veces que aparece
            entro = entropia(data, objetivo, variable, valores[i])
            resto = resto - (veces / len(met[variable])) * entro
            i = i + 1
        ganancia = ganancia - resto
        return ganancia

var = 1
while var < 21:
    gan = 0
    ganancias = []
    variable = var
    gan = ganancia(data, 0, var, 1)
    print("La ganancia de la variable " + variables[variable] + " es: " + str(gan))
    ganancias.append(gan)
    var = var + 1

print(data)

def id3(data, objetivo, lista_atributos, profundidad):
    print("Comenzamos con el ID3")
    # data = matrix de personas
    # objetivo = 0 ==> devuelve o no el prestamo
    # variables = [variable1,variable2,....] son strings que marcan el nombre de cada variable
    # profundidad = 4 niveles del arbol
    arbol = {}
    prof = 0
    while prof < profundidad:
        # desde aca vamos a a armar el arbol
        print("Start")
        if prof == 0:  # nodo raiz
            entropia = funciones.entropia_total(data, objetivo)
            ganancia_var = []
            i = 0
            while i < 21:  # Cantidad de variables (21)
                print("Do stuff")

    return arbol
