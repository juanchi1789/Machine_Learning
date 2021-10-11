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


clases = ["Nacional", "Entretenimiento", "Deportes", "Salud"]

# <-------------------------------------------------------------------------------------------------------------------->

# <-------------------------------------------------------------------------------------------------------------------->

# Etapa INICIAL, cargamos los titulos en una lista y armamos el diccionario inicial

# Armamos los DATASETS TOTALES:

nacional_total = []
entretenimiento_total = []
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
    if data[contador][3] == "Entretenimiento":# Entrenamiento
        entretenimiento_total.append(data[contador][1])
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

dic_in = {"Nacional": nacional_total, "Entretenimiento": entretenimiento_total, "Deportes": deportes_total, "Salud": salud_total}
# Entrenamiento
print("\n")
print("La cantidad de titulos por clase es:")
#funciones.mostrar_cantidad_de_titulos(dic_in)
print("\n")

# Armamos las clases de Entrenamiento y de testeo por clase

# ENTRENAMIENTO
coef = 1.3
dic_entrenamiento = {"Nacional": nacional_total[0:int(len(nacional_total) / coef)],
                     "Entretenimiento": entretenimiento_total[0:int(len(entretenimiento_total) / coef)],
                     "Deportes": deportes_total[0:int(len(deportes_total) / coef)],
                     "Salud": salud_total[0:int(len(salud_total) / coef)]}

# TESTEO
dic_testeo = {"Nacional": nacional_total[int(len(nacional_total) / coef):len(nacional_total)],
              "Entretenimiento": entretenimiento_total[int(len(entretenimiento_total) / coef):len(entretenimiento_total)],
              "Deportes": deportes_total[int(len(deportes_total) / coef):len(deportes_total)],
              "Salud": salud_total[int(len(salud_total) / coef):len(salud_total)]}

print("La cantidad de titulos por clase en el Entretenimiento:")
funciones.mostrar_cantidad_de_titulos(dic_entrenamiento)
print("\n")

# <-------------------------------------------------------------------------------------------------------------------->
#  VAMOS A PROBAR LODO A MENOR ESCALA Y DESPUES LO EXPANDIMOS


dic_filtrado = funciones.filtrado_dic(dic_entrenamiento)


# <----------------------------------------> Borrar palabras de una lista correctamente

#print("Antes:")
#print("longitud: " + str(len(dic_filtrado["Nacional"]))+ " palabras")

#contador = 0
#while contador < len(palabras_spam):
#    i = 0
#    while i < len(dic_filtrado["Nacional"]):
#        if palabras_spam[contador] in dic_filtrado["Nacional"]:
#            dic_filtrado["Nacional"].remove(palabras_spam[contador])
#        i = i + 1

#    print("Estamos en: "+ str(contador))
#    contador = contador + 1

# <----------------------------------------> Borrar keys de un diccionario correctamente

dic_entrenado = funciones.entrenador(dic_filtrado)

print("Antes: " +str(dic_entrenado["Nacional"].keys().__len__())+ " Palabras")

funciones.limpiador(dic_entrenado)

print("Ahora: " +str(dic_entrenado["Nacional"].keys().__len__())+ " Palabras")

# <----------------------------------------> testear correctamente

print("\n")

dic_testeo = {"Nacional": nacional_total[int(len(nacional_total) / coef):len(nacional_total)],
              "Entretenimiento": entretenimiento_total[int(len(entretenimiento_total) / coef):len(entretenimiento_total)],
              "Deportes": deportes_total[int(len(deportes_total) / coef):len(deportes_total)],
              "Salud": salud_total[int(len(salud_total) / coef):len(salud_total)]}

print("Tenemos: "+str(len(dic_testeo["Nacional"]))+" titulos para testear de Nacional")
print("Tenemos: "+str(len(dic_testeo["Entretenimiento"]))+" titulos para testear de Entretenimiento")
print("Tenemos: "+str(len(dic_testeo["Deportes"]))+" titulos para testear de Deportes")
print("Tenemos: "+str(len(dic_testeo["Salud"]))+" titulos para testear de Salud")

total = dic_entrenado["Nacional"].keys().__len__()+dic_entrenado["Entretenimiento"].keys().__len__()\
        +dic_entrenado["Deportes"].keys().__len__()+dic_entrenado["Salud"].keys().__len__()

print("Comenzamos con el testeo")

probas_de_clase = [0.25691298234650833, 0.35174191532573035, 0.24285267926886425, 0.14849242305889704]
aciertos = 0
desaciertos = 0
clases = 0
while clases < 4:

    if clases == 0:# clase Nacional
        proba_nacional = []
        proba_entretenimiento = []
        proba_deportes = []
        proba_salud = []

        contador = 0
        while contador < (len(dic_testeo["Salud"])): # (*)

            titulo = dic_testeo["Salud"][contador]# (*)
            palabras = titulo.split()
            palabras = funciones.filtrado(palabras)
            funciones.limpiador_test(palabras)

            # calculo de la probabilidad titulo por titulo:

            tit = 0
            proba = probas_de_clase[0]
            while tit < len(palabras):
                proba = proba * dic_entrenado["Nacional"].get(palabras[tit], (1+0)/(dic_entrenado["Nacional"].keys().__len__()+total))# LAPLACE INCORPORADO
                tit = tit + 1
            proba_nacional.append(proba)

            tit = 0
            proba = probas_de_clase[1]
            while tit < len(palabras):
                proba = proba * dic_entrenado["Entretenimiento"].get(palabras[tit], (1+0)/(dic_entrenado["Entretenimiento"].keys().__len__()+total))# LAPLACE INCORPORADO
                tit = tit + 1
            proba_entretenimiento.append(proba)

            tit = 0
            proba = probas_de_clase[2]
            while tit < len(palabras):
                proba = proba * dic_entrenado["Deportes"].get(palabras[tit], (1+0)/(dic_entrenado["Deportes"].keys().__len__()+total))# LAPLACE INCORPORADO
                tit = tit + 1
            proba_deportes.append(proba)

            tit = 0
            proba = probas_de_clase[3]
            while tit < len(palabras):
                proba = proba * dic_entrenado["Salud"].get(palabras[tit], (1+0)/(dic_entrenado["Salud"].keys().__len__()+total))# LAPLACE INCORPORADO
                tit = tit + 1
            proba_salud.append(proba)

            contador = contador + 1


    clases = clases + 1

print(len(proba_nacional))
print(len(proba_entretenimiento))
print(len(proba_deportes))
print(len(proba_salud))

i = 0
aciertos = 0
on = 0
nacionales = 0
entretenimineto = 0
deportes = 0
salud = 0

if on == 0:
    while i < 877:
        if proba_nacional[i]>proba_deportes[i] and proba_nacional[i]>proba_salud[i] and proba_nacional[i]>proba_entretenimiento[i]:
            nacionales = nacionales + 1

        if proba_entretenimiento[i]>proba_deportes[i] and proba_entretenimiento[i]>proba_salud[i] and proba_entretenimiento[i]>proba_nacional[i]:
            entretenimineto = entretenimineto + 1

        if proba_deportes[i]>proba_nacional[i] and proba_deportes[i]>proba_salud[i] and proba_deportes[i]>proba_entretenimiento[i]:
            deportes = deportes + 1

        if proba_salud[i]>proba_deportes[i] and proba_salud[i]>proba_nacional[i] and proba_salud[i]>proba_entretenimiento[i]:
            salud = salud + 1

        i = i + 1

print("Tuvimos de nacional: "+ str(nacionales) +" sobre 891 titulos totales, osea una proba de: " +str(nacionales/891))
print("Tuvimos de Entretenimiento: "+ str(entretenimineto) +" sobre 891 titulos totales, osea una proba de: " +str(entretenimineto/891))
print("Tuvimos de Deportes: "+ str(deportes) +" sobre 891 titulos totales, osea una proba de: " +str(deportes/891))
print("Tuvimos de Salud: "+ str(salud) +" sobre 891 titulos totales, osea una proba de: " +str(salud/891))

print("\n")
print("Matrix de confusion")

# los valores almacenados en el arreglo siguiente se obtuvieron de forma manual cambiando la variable que esta señalada
# arriba con (*) de la linea 157 y 159. Lo fui cambiando por "Nacional","Entretenimiento","Deportes" y "Salud" y fui
# anotando los resultados en el arreglo de abajo

datos = [[673, 68, 72, 78], [54, 722, 100, 13], [39, 74, 753, 24],
         [46, 46, 7, 788]]  # resultados obtenidos de aciertos por clase (manual)

ax = sns.heatmap(datos, linewidth=0.5, annot=True, fmt="d")
plt.title("Matriz de confusion")
plt.xlabel("Prediccion")
plt.ylabel("Real")
plt.show()

print("Metricas==> son valores viejos, tengo que cambiarlos")

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

titulos = [[dic_testeo["Nacional"]], [dic_testeo["Entretenimiento"]], [dic_testeo["Deportes"]], [dic_testeo["Salud"]]]

# 2) calculo las probabilidades sobre esta data

# armo una lista de listas porque los undices 0 1 2 3 son las clases (me va a servir despues

probabilidades = [[], [], [],
                  []]  # En este vector voy a guardar las probabilidades de que cada uno de los titulos definido
# anteriormente ==> estas probabilidades van a cambiar segun la clase que querramos diferenciar
clase = 0
while clase < 4:

    #print("Metodo " + str(clase) + ": " + str(clases[clase]))

    total = dic_entrenado["Nacional"].keys().__len__() + dic_entrenado["Entretenimiento"].keys().__len__() \
            + dic_entrenado["Deportes"].keys().__len__() + dic_entrenado["Salud"].keys().__len__()

    probas_de_clase = [0.25691298234650833, 0.35174191532573035, 0.24285267926886425, 0.14849242305889704]
    clases = ["Nacional", "Entretenimiento", "Deportes", "Salud"]
    contador = 0
    while contador < len(titulos):  # va viendo los titulos de cada clase
        i = 0
        while i < len(titulos[contador]):  # va viendo los titulos por separado
            title = 0

            while title < len(titulos[contador][i]):  # veo al titulo como una lista
                titulo = titulos[contador][i][title]
                palabras = titulo.split()
                palabras = funciones.filtrado_test(palabras) # yodo lo anterior es para limpiar esta lista
                palabras = funciones.filtrado(palabras)
                funciones.limpiador_test(palabras)

                # hasta aca ya tenemos las el titulo como una lista de palabras ==> tenemos que calcular la proabilidad de
                # este titulo y guardarla en la lista (de listas) de probabilidad segun la clase a la cual pertenece

                alfa = 0
                proba_del_titulo = probas_de_clase[contador]
                total_de_palabra = 0

                while alfa < len(palabras):  # aca se va a calcular la probabilidad de cada titulo

                    total_de_palabra = 1
                    proba_del_titulo = proba_del_titulo * dic_entrenado[clases[clase]].get(palabras[alfa], (1+0)/(dic_entrenado[clases[clase]].keys().__len__()+total))# LAPLACE INCORPORADO
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
    cantidad = 50
    vector_humbral = []
    i = 1
    while i <= cantidad:
        vector_humbral.append((math.pow(1e-1, i)))
        i = i + 1
    print("El vector humbral es: ")
    print(vector_humbral)

    dic_roc = {"Nacional": probabilidades[0], "Entretenimiento": probabilidades[1], "Deportes": probabilidades[2],
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
                    if valor > humbral and clases[i] == "Entretenimiento":  # en este caso tomamos solamente el caso nacional
                        vp = vp + 1
                    if valor < humbral and clases[i] == "Entretenimiento":
                        fn = fn + 1
                    #           <----------------------------------------------------->
                    if valor > humbral and clases[i] != "Entretenimiento":  # Todos los otros casos
                        fp = fp + 1
                    if valor < humbral and clases[i] != "Entretenimiento":
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