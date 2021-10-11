
# Funcionde del EJ 1

import numpy as np
import math as mt

def categorizador(list_of_list,list_var_cat):# en nuestro caso la seg lista es [2,4,12]
    indice_1 = 0
    while indice_1 < len(list_of_list):# recorre la lista de listas
        indice_2 = 0
        while indice_2 < len(list_of_list[indice_1]):# recorre los datos de la persona

            if indice_2 == list_var_cat[0]:# Duracion del credito ==> [2,5,13]

                if 0 <= list_of_list[indice_1][indice_2] <= 20:# BAJO
                    list_of_list[indice_1][indice_2] = 1
                if 20 < list_of_list[indice_1][indice_2] <= 35:# MEDIO
                    list_of_list[indice_1][indice_2] = 2
                if 35 < list_of_list[indice_1][indice_2]:# ALTO
                    list_of_list[indice_1][indice_2] = 3

            if indice_2 == list_var_cat[1]:  # Duracion del credito ==> [2,5,13]

                if 0 <= list_of_list[indice_1][indice_2] <= 2550:  # BAJO
                    list_of_list[indice_1][indice_2] = 1
                if 2550 < list_of_list[indice_1][indice_2] <= 7000:  # MEDIO
                    list_of_list[indice_1][indice_2] = 2
                if 7000 < list_of_list[indice_1][indice_2]:  # ALTO
                    list_of_list[indice_1][indice_2] = 3

            if indice_2 == list_var_cat[2]:  # EDAD  ==> [2,5,13]

                if 0 <= list_of_list[indice_1][indice_2] <= 35:  # BAJO
                    list_of_list[indice_1][indice_2] = 1
                if 35 < list_of_list[indice_1][indice_2] <= 50:  # MEDIO
                    list_of_list[indice_1][indice_2] = 2
                if 50 < list_of_list[indice_1][indice_2]:  # ALTO
                    list_of_list[indice_1][indice_2] = 3

            indice_2 = indice_2 + 1

        indice_1 = indice_1 + 1

def entropia_total(list, objetivo):
    total_pers = len(list)
    i = 0
    pos = 0
    neg = 0
    while i < total_pers:
        if list[i][objetivo] == 1:
            pos = pos + 1
        if list[i][objetivo] == 0:
            neg = neg + 1
        i = i + 1

    entropia = round(-(pos / total_pers) * np.log2((pos / total_pers)) - (pos / total_pers) * np.log2((pos / total_pers)),4)

    return entropia

def valores(list,columna):# Detector de valores
    i = 0
    valores = []  # tengo que poder reconocer los valores que va a tomar la variable, porque cada variable
                  # los toma distintos
    while i < len(list):  # voy recorriendo las columnas para ver los valores distintos
        if not (list[i][columna] in valores):
            valores.append(list[i][columna])
        i = i + 1
    valores.sort()

    return valores

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

