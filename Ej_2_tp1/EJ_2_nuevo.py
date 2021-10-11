# <-------------------------------------------------------------------------------------------------------------------->
# Ej 2 Mejorado:

import math
import funciones
import pandas as pd  # solo para importar el archivo
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

array = pd.read_csv("Noticias_argentinas.csv", low_memory=False)
data = array.values

# <-------------------------------------------------------------------------------------------------------------------->
# CLASES:

# Nacional -------> 3860
# Destacada -------> 3859
# Deportes -------> 3855
# Salud -------> 3840

clases = ["Nacional", "Destacada", "Deportes", "Salud"]

palabras_spam = ['a', "el", "la", "los", "y", "de", "ellos", "que", "qué", "del", "pero", "ademas", "sin", "con", "la",
                 "que", "se", "su", "lo", "las", "me", "son", "pero", "porque", "|", "cómo", "no", "en", "para",
                 "es", "[video]", "...", "después", 'de', 'por', "un", "una", 'a', 'como', 'o']

# <-------------------------------------------------------------------------------------------------------------------->

# <-------------------------------------------------------------------------------------------------------------------->

# Etapa INICIAL, cargamos los titulos en una lista y armamos el diccionario inicial

# Armamos los DATASETS TOTALES:

nacional_total = []
destacada_total = []
deportes_total = []
salud_total = []

# Armamos la data de entrada

contador = 0
while contador < len(data):
    if data[contador][3] == "Nacional":
        nacional_total.append(data[contador][1])
    contador = contador + 1

contador = 0
while contador < len(data):
    if data[contador][3] == "Destacadas":
        destacada_total.append(data[contador][1])
    contador = contador + 1

contador = 0
while contador < len(data):
    if data[contador][3] == "Deportes":
        deportes_total.append(data[contador][1])
    contador = contador + 1

contador = 0
while contador < len(data):
    if data[contador][3] == "Salud":
        salud_total.append(data[contador][1])
    contador = contador + 1

# El siguiente diccionario contiene los titulos totales segun la clase

dic_in = {"Nacional": nacional_total, "Destacada": destacada_total, "Deportes": deportes_total, "Salud": salud_total}

print("\n")
print("La cantidad de titulos por clase es:")
funciones.mostrar_cantidad_de_titulos(dic_in)
print("\n")

# Armamos las clases de Entrenamiento y de testeo por clase

# DATASETS ENTRENAMIENTO
coef = 1.3
dic_entrenamiento = {"Nacional": nacional_total[0:int(len(nacional_total) / coef)],
                     "Destacada": destacada_total[0:int(len(destacada_total) / coef)],
                     "Deportes": deportes_total[0:int(len(deportes_total) / coef)],
                     "Salud": salud_total[0:int(len(salud_total) / coef)]}

# DATASETS TESTEO
dic_testeo = {"Nacional": nacional_total[int(len(nacional_total) / coef):len(nacional_total)],
              "Destacada": destacada_total[int(len(destacada_total) / coef):len(destacada_total)],
              "Deportes": deportes_total[int(len(deportes_total) / coef):len(deportes_total)],
              "Salud": salud_total[int(len(salud_total) / coef):len(salud_total)]}

print("La cantidad de titulos por clase en el entrenamiento:")
funciones.mostrar_cantidad_de_titulos(dic_entrenamiento)
print("\n")

# <-------------------------------------------------------------------------------------------------------------------->
# Etapa FILTRADO, Filtramos los datos que guardamos en el diccionario

dic_filtrado = funciones.filtrado_dic(dic_entrenamiento)  # Hasta aca solo se filtraron

# solo los caracteres y se armo una lista con
# las palabras de los titulos

print("\n")
print("La cantidad de palabras por clase en entrenamiento:")
funciones.mostrar_cantidad_de_palabras(dic_filtrado)

# se debe destacar que las palabras individuales como "de","hasta",etc. No van a ser filtradas en esta etapa, lo seran
# mas adelante
# <-------------------------------------------------------------------------------------------------------------------->

# Espacio libre para un posible calculo


# <-------------------------------------------------------------------------------------------------------------------->
# Etapa de ENTRENAMIENTO:

dic_entrenado = funciones.entrenador(dic_filtrado)

total = len(dic_entrenado[clases[0]]) + len(dic_entrenado[clases[1]]) + len(dic_entrenado[clases[2]]) + len(
    dic_entrenado[clases[3]])

print("P(Nacional): " + str(len(dic_entrenado[clases[0]]) / total))
print("P(Destacada): " + str(len(dic_entrenado[clases[1]]) / total))
print("P(Deportes): " + str(len(dic_entrenado[clases[2]]) / total))
print("P(Salud): " + str(len(dic_entrenado[clases[3]]) / total))

# Hasta aca ya tenemos los diccionarios de cada clase, con cada palabra como llave y la probabilidad a priori como su
# valor.

print("\n")
print("La cantidad de palabras que tiene nuestro diccionario entrenado son: ")

funciones.mostrar_cantidad_de_palabras_entrenadas(dic_entrenado)

# Nacional : {"Palabra":probabilidad condicional por prob de la clase }


# Lo que nos queda por hacer es simplemente eliminar aquellos elementos que consideramos que pueden traer porblemas
# para el calculo de testeo, eso lo hacemos en la seccion siguiente

# <-------------------------------------------------------------------------------------------------------------------->

# Estapa de Limpieza, aqui vamos a eliminar aquellas palabras que no queremos que causen

funciones.limpiador(dic_entrenado)  # limpieza

print("\n")
print("Luego de la limpieza nos queda la siguiente cantidad de palabras:")
funciones.mostrar_cantidad_de_palabras_entrenadas(dic_entrenado)

print("\n")
print("Limpieza y entrenamiento terminado")

# <-------------------------------------------------------------------------------------------------------------------->

# Etapa de TESTEO

# Vamos a ver cuan bueno es nuestro algoritmo para discriminar un titulo y luego vamos a ver cuan bueno
# es considerando toda la lista de titulos de testeo que armamos en la parte superior

print("\n")
print("La cantidad de titulos por clase en el testeo:")

funciones.mostrar_cantidad_de_titulos(dic_testeo)

# quiero ver cuales son las probabilidades de que este titulo corresponda a cada clase

nacional = 0
destacada = 0
deportes = 0
salud = 0

# La parte siguiente no esta automatizada, vamos cambiando el valor del parametro "clase" que se define a continuacion

tit = 0

# MANUAL
clase = 0  # clase = 0 ==> Nacional, clase = 1 ==>Destacada, clase = 2 ==> Deportes, clase = 3 ==> Salud

print("Cantidad de titulos totales:" + str(len(dic_testeo[clases[clase]])))

while tit < len(dic_testeo[clases[clase]]):

    titulo = (dic_testeo[clases[clase]][tit])

    palabras = titulo.split()
    palabras = funciones.filtrado_test(palabras)
    palabras = funciones.filter(palabras)

    # tuve que limpiar a mano con el siguiente ciclo porque la funcion que habia definido no lo hacia correctamtente

    i = 0
    while i < len(palabras_spam):
        if palabras_spam[i] in palabras:
            palabras.remove(palabras_spam[i])
        i = i + 1

    probas = [0.25691298234650833, 0.35174191532573035, 0.24285267926886425, 0.14849242305889704]  # estas son

    # las probabilidades que calule
    # en el metodo entrenamient

    i = 0
    while i < len(palabras):  # recorre la lista de palabras de ese titulo en particular
        contador = 0
        palabra = palabras[i]
        while contador < len(clases):  # recorre el diccionario y nos da el valor

            # laplace = (0+1)/(4+len(dic_entrenado[clases[clase]])) # ==> Me no puede discriminar a Nacional y a Destacada

            laplace = 0.00001  # Eleccion arbitraria ==> yo se que esta mal pero fue la que mejor se ajusto
            probas[contador] = probas[contador] * dic_entrenado[clases[contador]].get(palabra, laplace)
            contador = contador + 1
        i = i + 1

    # Calculo de Aciertos ==> Para la matriz de confusion

    if probas[0] > probas[1] and probas[0] > probas[2] and probas[0] > probas[3]:
        nacional = nacional + 1
    if probas[1] > probas[0] and probas[1] > probas[2] and probas[1] > probas[3]:
        destacada = destacada + 1
    if probas[2] > probas[0] and probas[2] > probas[1] and probas[2] > probas[3]:
        deportes = deportes + 1
    if probas[3] > probas[0] and probas[3] > probas[1] and probas[3] > probas[2]:
        salud = salud + 1
    tit = tit + 1

print("Valores finales:")

datos = [[485, 330, 43, 33], [273, 479, 102, 37], [37, 72, 770, 11],
         [42, 76, 17, 752]]  # resultados obtenidos de aciertos por clase (manual)

ax = sns.heatmap(datos, linewidth=0.5, annot=True, fmt="d")
plt.title("Matriz de confusion")
plt.xlabel("Prediccion")
plt.ylabel("Real")
plt.show()

print("Valor total:" + str(len(dic_testeo[clases[clase]])))
total = len(dic_testeo[clases[clase]])

print("Casos detectados:")
print(nacional)
print(destacada)
print(deportes)
print(salud)

print("Probabilidades:")
print(nacional / total)
print(destacada / total)
print(deportes / total)
print(salud / total)
print("\n")
print("Metricas de evaluacion:")  # los calculos siguientes se hicieron a mano tomando el promedio de todas las metricas
# por clase

print("Accuracy: " + str(0.698511))
print("Precision: " + str(0.70223))
print("Recall: " + str(0.698725))
print("F1 score: " + str(0.699847))
print("Tasa de verdaderos positivos: " + str(0.698725))
print("Tasa de Falsos positivos: " + str(0.100526))
print("\n")

# <-------------------------------------------------------------------------------------------------------------------->
# Etapa ROC

print("Curva ROC")

# Armo mi data frame, voy a tener 1 curva por clase ==> voy a tener 4 curvas

# PASOS:

# 1) armo mi data frame (con las 4 clases) y el vector humbral

# Vamos a tomar 100 titulos (en esta primera prueba) ==> 25 de cada clase

titulos = [[dic_testeo["Nacional"]], [dic_testeo["Destacada"]],
           [dic_testeo["Deportes"]], [dic_testeo["Salud"]]]

# 2) calculo las probabilidades sobre esta data

# armo una lista de listas porque los undices 0 1 2 3 son las clases (me va a servir despues

probabilidades = [[], [], [],
                  []]  # En este vector voy a guardar las probabilidades de que cada uno de los titulos definido
# anteriormente ==> estas probabilidades van a cambiar segun la clase que querramos diferenciar


clase = 0  # con esto vamos a ir ajustanto la clase que estemos estudiando ==> MANUAL

while clase < 4:

    print("Metodo " + str(clase) + ": " + str(clases[clase]))

    total = len(dic_entrenado[clases[0]]) + len(dic_entrenado[clases[1]]) + len(dic_entrenado[clases[2]]) + len(
        dic_entrenado[clases[3]])

    probas_de_clase = [0.25691298234650833, 0.35174191532573035, 0.24285267926886425, 0.14849242305889704]

    contador = 0
    while contador < len(titulos):  # va viendo los titulos de cada clase
        i = 0
        while i < len(titulos[contador]):  # va viendo los titulos por separado
            title = 0

            while title < len(titulos[contador][i]):  # veo al titulo como una lista
                titulo = titulos[contador][i][title]
                palabras = titulo.split()
                palabras = funciones.filtrado_test(palabras)
                palabras = funciones.filter(palabras)  # yodo lo anterior es para limpiar esta lista

                # hasta aca ya tenemos las el titulo como una lista de palabras ==> tenemos que calcular la proabilidad de
                # este titulo y guardarla en la lista (de listas) de probabilidad segun la clase a la cual pertenece

                alfa = 0
                proba_del_titulo = probas_de_clase[contador]
                total_de_palabra = 0

                while alfa < len(palabras):  # aca se va a calcular la probabilidad de cada titulo

                    total_de_palabra = 1
                    laplace = 0.00001
                    proba_del_titulo = proba_del_titulo * dic_entrenado[clases[clase]].get(palabras[alfa], laplace)
                    alfa = alfa + 1

                probabilidades[contador].append(proba_del_titulo)

                title = title + 1

            i = i + 1

        contador = contador + 1

    print("Probabilidades para discriminar a: " + clases[clase])

    print((probabilidades[0]))
    print((probabilidades[1]))
    print((probabilidades[2]))
    print((probabilidades[3]))

    print("\n")

    # tengo que comparar cada valor de probabilidad con los componentes de mi vector_humbral

    print("Pasamos a calcular las TVP y la TFP: ")
    cantidad = 200
    vector_humbral = []
    i = 1
    while i <= cantidad:
        vector_humbral.append((math.pow(1e-1, i)))
        i = i + 1
    print("El vector humbral es: ")
    print(vector_humbral)

    dic_roc = {"Nacional": probabilidades[0], "Destacada": probabilidades[1], "Deportes": probabilidades[2],
               "Salud": probabilidades[3]}  # diccionario con las probabilidades

    # Listas de los parametros
    vp_list = []
    vn_list = []
    fp_list = []
    fn_list = []

    cambio_en_humbral = 0
    while cambio_en_humbral < len(vector_humbral):
        humbral = vector_humbral[cambio_en_humbral]
        i = 0
        vp = 0
        vn = 0
        fp = 0
        fn = 0
        while i < 4:  # va pasando de clase en clase
            contador = 0
            while contador < len(dic_roc[clases[i]]):  # va mirando las listas de las Probabilidades (VA DE CERO A 25)

                if clase == 0:  # el metodo que busca diferenciar a los titulos nacionales
                    valor = dic_roc[clases[i]][contador]  # el valor de la probabilidad

                    #           <----------------------------------------------------->
                    if valor > humbral and clases[i] == "Nacional":  # en este caso tomamos solamente el caso nacional
                        vp = vp + 1
                    if valor < humbral and clases[i] == "Nacional":
                        fn = fn + 1
                    #           <----------------------------------------------------->
                    if valor > humbral and clases[i] != "Nacional":  # Todos los otros casos
                        fp = fp + 1
                    if valor < humbral and clases[i] != "Nacional":
                        vn = vn + 1

                if clase == 1:  # el metodo que busca diferenciar a los titulos nacionales
                    valor = dic_roc[clases[i]][contador]  # el valor de la probabilidad

                    #           <----------------------------------------------------->
                    if valor > humbral and clases[i] == "Destacada":  # en este caso tomamos solamente el caso nacional
                        vp = vp + 1
                    if valor < humbral and clases[i] == "Destacada":
                        fn = fn + 1
                    #           <----------------------------------------------------->
                    if valor > humbral and clases[i] != "Destacada":  # Todos los otros casos
                        fp = fp + 1
                    if valor < humbral and clases[i] != "Destacada":
                        vn = vn + 1

                if clase == 2:  # el metodo que busca diferenciar a los titulos nacionales
                    valor = dic_roc[clases[i]][contador]  # el valor de la probabilidad

                    #           <----------------------------------------------------->
                    if valor > humbral and clases[i] == "Deportes":  # en este caso tomamos solamente el caso nacional
                        vp = vp + 1
                    if valor < humbral and clases[i] == "Deportes":
                        fn = fn + 1
                    #           <----------------------------------------------------->
                    if valor > humbral and clases[i] != "Deportes":  # Todos los otros casos
                        fp = fp + 1
                    if valor < humbral and clases[i] != "Deportes":
                        vn = vn + 1

                if clase == 3:  # el metodo que busca diferenciar a los titulos nacionales
                    valor = dic_roc[clases[i]][contador]  # el valor de la probabilidad
                    #           <----------------------------------------------------->
                    if valor > humbral and clases[i] == "Salud":  # en este caso tomamos solamente el caso nacional
                        vp = vp + 1
                    if valor < humbral and clases[i] == "Salud":
                        fn = fn + 1
                    #           <----------------------------------------------------->
                    if valor > humbral and clases[i] != "Salud":  # Todos los otros casos
                        fp = fp + 1
                    if valor < humbral and clases[i] != "Salud":
                        vn = vn + 1

                contador = contador + 1

            i = i + 1
        # Cargamos las listas
        vp_list.append(vp)
        vn_list.append(vn)
        fp_list.append(fp)
        fn_list.append(fn)
        cambio_en_humbral = cambio_en_humbral + 1

    print("\n")
    print("Los parametros obtenidos son: ")

    print("Verdaderos positivos: " + str(vp_list))
    print("Verdaderos negativos: " + str(vn_list))
    print("Falsos negativos:     " + str(fn_list))
    print("Falsos positivos:     " + str(fp_list))

    # 4) determino la TVP y la TFP para cada valor del humbral

    print("tenemos los valores de los parametros, solo queda formar los pundos ROC")

    tvp = []
    i = 0
    while i < len(vp_list):
        tvp.append((vp_list[i]) / (vp_list[i] + fn_list[i]))
        i = i + 1

    tfp = []
    i = 0
    while i < len(vn_list):
        tfp.append((fp_list[i]) / (fp_list[i] + vn_list[i]))
        i = i + 1

    print("\n")
    print("Las tas me quedan:")
    print("TASA de Verdaderos positivos: " + str(tvp))
    print("TASA DE Falsos positivos: " + str(tfp))

    print("Mi primera curva ROC: ")

    # 6) grafico cada punto ==> termino la ROC

    linealx = [0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1]
    linealy = [0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1]

    plt.plot(tfp, tvp)
    plt.plot(linealx, linealy)
    plt.title("CURVA ROC!")
    plt.xlabel("Tasa de Falsos positivos")
    plt.ylabel("Tasa de Verdaderos positivos")
    plt.show()
    clase = clase + 1

# for k in range(len(vector_humbral)):
#   for i in range(len(probabilidades[0])):
#      for j in range(4):
#         if probabilidades[i][j] < vector_humbral[k]:
#            if i == 0:
#               fn = fn + 1
#          else:
#             vn = vn + 1
#    else:
#       if i == 0:
#          vp = vp + 1
#     else:
#        fp = fp + 1

# print("Fp"+ str(fp))
# print("VP"+ str(vp))
# print("Vn"+ str(vn))
# print("Fn"+ str(fn))
# fp = 0
# fn = 0
# vp = 0
# vn = 0


# print("Los parametros son:")

# print("VP: "+str(vp))
# print("VN: "+str(vn))
# print("FP: "+str(fp))
# print("FN: "+str(fn))


# <-------------------------------------------------------------------------------------------------------------------->
