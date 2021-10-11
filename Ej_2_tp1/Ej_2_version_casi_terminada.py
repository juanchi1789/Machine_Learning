# <-------------------------------------------------------------------------------------------------------------------->
# Ej 2:

import math
import random
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

# Etapa INICIAL, cargamos los titulos en una lista

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
    if data[contador][3] == "Entretenimiento":  # Entrenamiento
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

dic_in = {"Nacional": nacional_total, "Entretenimiento": entretenimiento_total, "Deportes": deportes_total,
          "Salud": salud_total}
print("\n")

# Armamos las clases de Entrenamiento y de testeo por clase aleatoriamente

# ENTRENAMIENTO
# Armo un dataset con el 80% de datos para entrenar y un 20% de datos para testear (sobre los totales ingresados)



coef = 80
nacional_entre = random.sample(nacional_total, int(len(nacional_total) * coef / 100))
entretenimiento_entre = random.sample(entretenimiento_total, int(len(entretenimiento_total) * coef / 100))
deportes_entre = random.sample(deportes_total, int(len(deportes_total) * coef / 100))
salud_entre = random.sample(salud_total, int(len(salud_total) * coef / 100))

print("longitud nacional: " + str(len(nacional_entre)))
print("longitud Entretenimiento: " + str(len(entretenimiento_entre)))
print("longitud Deportes: " + str(len(deportes_entre)))
print("longitud Salud: " + str(len(salud_entre)))

dic_entrenamiento = {"Nacional": nacional_entre,
                     "Entretenimiento": entretenimiento_entre,
                     "Deportes": deportes_entre,
                     "Salud": salud_entre}

# Tambien armo el dataset de testeo con los que no estan en el data set de entrenamiento

nacional_test = []
entrenamiento_test = []
deportes_test = []
salud_test = []

i = 0
while i < (len(nacional_entre)):
    nacional_total.remove(nacional_entre[i])
    i = i + 1

i = 0
while i < (len(entretenimiento_entre)):
    entretenimiento_total.remove(entretenimiento_entre[i])
    i = i + 1

i = 0
while i < (len(deportes_entre)):
    deportes_total.remove(deportes_entre[i])
    i = i + 1

i = 0
while i < (len(salud_entre)):
    salud_total.remove(salud_entre[i])
    i = i + 1

salud_test = salud_total



nacional_test = nacional_total
entretetenimiento_test = entretenimiento_total
deportes_test = deportes_total
# TESTEO

dic_testeo = {"Nacional": nacional_test,
              "Entretenimiento": entretetenimiento_test,
              "Deportes": deportes_test,
              "Salud": salud_test}

print("La cantidad de titulos por clase en el Entretenimiento:")
funciones.mostrar_cantidad_de_titulos(dic_entrenamiento)
print("\n")

# <-------------------------------------------------------------------------------------------------------------------->

dic_filtrado = funciones.filtrado_dic(dic_entrenamiento)# me entrega un diccionario de esta forma==> DIC={"CLASE":[lista de palabras en esta clase]}

# <-------------------------------------------------------------------------------------------------------------------->

dic_entrenado = funciones.entrenador(dic_filtrado)# ENTRENAMIENTO


total_palabras = dic_entrenado["Nacional"].keys().__len__() + dic_entrenado["Entretenimiento"].keys().__len__() + \
                 dic_entrenado["Deportes"].keys().__len__() + dic_entrenado["Salud"].keys().__len__()

print("La cantidad de palabras totales es: " + str(total_palabras))

probas_de_clase = [dic_entrenado["Nacional"].keys().__len__() / total_palabras,
                   dic_entrenado["Entretenimiento"].keys().__len__() / total_palabras,
                   dic_entrenado["Deportes"].keys().__len__() / total_palabras,
                   dic_entrenado["Salud"].keys().__len__() / total_palabras]

palabras_unicas = []
i = 0
while i < len(clases):# recorre clase por clase
    contador = 0
    while contador < len(list(dic_entrenado[clases[i]].keys())):# recorre llave por llave

        if not(list(dic_entrenado[clases[i]].keys())[contador] in palabras_unicas):
            palabras_unicas.append(list(dic_entrenado[clases[i]])[contador])

        contador = contador + 1
    i = i + 1

print("La cantidad de palabras unicas en todas las clases es: "+str(len(palabras_unicas)))

print("\n")
print("Las probabilidades 'A priori' son: ")

print("La P(Nacional): " + str(probas_de_clase[0]))
print("La P(Entretenimiento): " + str(probas_de_clase[1]))
print("La P(Deportes): " + str(probas_de_clase[2]))
print("La P(Salud): " + str(probas_de_clase[3]))

# <----------------------------------------> testear correctamente

print("\n")

print("Tenemos: " + str(len(dic_testeo["Nacional"])) + " titulos para testear de Nacional")
print("Tenemos: " + str(len(dic_testeo["Entretenimiento"])) + " titulos para testear de Entretenimiento")
print("Tenemos: " + str(len(dic_testeo["Deportes"])) + " titulos para testear de Deportes")
print("Tenemos: " + str(len(dic_testeo["Salud"])) + " titulos para testear de Salud")

total = dic_entrenado["Nacional"].keys().__len__() + dic_entrenado["Entretenimiento"].keys().__len__() \
        + dic_entrenado["Deportes"].keys().__len__() + dic_entrenado["Salud"].keys().__len__() # cantidad de palabras totales

print("Comenzamos con el testeo")

aciertos = 0
desaciertos = 0
clases = 0

proba_nacional =            [[], [], [], []] # Matriz de probabilidades
proba_entretenimiento =     [[], [], [], []]
proba_deportes =            [[], [], [], []]
proba_salud =               [[], [], [], []]

while clases < 4:

    if clases == 0:  # clase Nacional
        contador = 0
        while contador < (len(dic_testeo["Nacional"])):  # (*)

            titulo = dic_testeo["Nacional"][contador]  # (*)
            palabras = titulo.split()
            palabras = funciones.filtrado(palabras)
            funciones.limpiador_test(palabras)

            # calculo de la probabilidad titulo por titulo:

            tit = 0
            proba = probas_de_clase[0]
            while tit < len(palabras): # recorremos la lista de palabras ==> son las palabras de cada titulo

                proba = proba * dic_entrenado["Nacional"].get(palabras[tit], 1*(1 + 0) / (
                            total + 4)) # LAPLACE INCORPORADO
                tit = tit + 1
            proba_nacional[clases].append(proba)

            tit = 0
            proba = probas_de_clase[1]
            while tit < len(palabras):
                proba = proba * dic_entrenado["Entretenimiento"].get(palabras[tit], 1*(1 + 0) / (
                            total + 4))  # LAPLACE INCORPORADO
                tit = tit + 1
            proba_entretenimiento[clases].append(proba)

            tit = 0
            proba = probas_de_clase[2]
            while tit < len(palabras):
                proba = proba * dic_entrenado["Deportes"].get(palabras[tit], 1*(1 + 0) / (
                            total + 4))  # LAPLACE INCORPORADO
                tit = tit + 1
            proba_deportes[clases].append(proba)

            tit = 0
            proba = probas_de_clase[3]
            while tit < len(palabras):
                proba = proba * dic_entrenado["Salud"].get(palabras[tit], 1*(1 + 0) / (
                            total + 4))  # LAPLACE INCORPORADO
                tit = tit + 1
            proba_salud[clases].append(proba)

            contador = contador + 1

    if clases == 1:  # clase Entretenimiento
        contador = 0
        while contador < (len(dic_testeo["Entretenimiento"])):  # (*)

            titulo = dic_testeo["Entretenimiento"][contador]  # (*)
            palabras = titulo.split()
            palabras = funciones.filtrado(palabras)
            funciones.limpiador_test(palabras)

            # calculo de la probabilidad titulo por titulo:

            tit = 0
            proba = probas_de_clase[0]
            while tit < len(palabras):
                proba = proba * dic_entrenado["Nacional"].get(palabras[tit], 1*(1 + 0) / (
                        total + 4))  # LAPLACE INCORPORADO
                tit = tit + 1
            proba_nacional[clases].append(proba)

            tit = 0
            proba = probas_de_clase[1]
            while tit < len(palabras):
                proba = proba * dic_entrenado["Entretenimiento"].get(palabras[tit], 1*(1 + 0) / (
                        total + 4))  # LAPLACE INCORPORADO
                tit = tit + 1
            proba_entretenimiento[clases].append(proba)

            tit = 0
            proba = probas_de_clase[2]
            while tit < len(palabras):
                proba = proba * dic_entrenado["Deportes"].get(palabras[tit], 1*(1 + 0) / (
                        total + 4))  # LAPLACE INCORPORADO
                tit = tit + 1
            proba_deportes[clases].append(proba)

            tit = 0
            proba = probas_de_clase[3]
            while tit < len(palabras):
                proba = proba * dic_entrenado["Salud"].get(palabras[tit], 1*(1 + 0) / (
                        total + 4))  # LAPLACE INCORPORADO
                tit = tit + 1
            proba_salud[clases].append(proba)

            contador = contador + 1

    if clases == 2:  # clase Deportes
        contador = 0
        while contador < (len(dic_testeo["Deportes"])):  # (*)

            titulo = dic_testeo["Deportes"][contador]  # (*)
            palabras = titulo.split()
            palabras = funciones.filtrado(palabras)
            funciones.limpiador_test(palabras)

            # calculo de la probabilidad titulo por titulo:

            tit = 0
            proba = probas_de_clase[0]
            while tit < len(palabras):
                proba = proba * dic_entrenado["Nacional"].get(palabras[tit], 1*(1 + 0) / (
                        total + 4))  # LAPLACE INCORPORADO
                tit = tit + 1
            proba_nacional[clases].append(proba)

            tit = 0
            proba = probas_de_clase[1]
            while tit < len(palabras):
                proba = proba * dic_entrenado["Entretenimiento"].get(palabras[tit], 1*(1 + 0) / (
                        total + 4))  # LAPLACE INCORPORADO
                tit = tit + 1
            proba_entretenimiento[clases].append(proba)

            tit = 0
            proba = probas_de_clase[2]
            while tit < len(palabras):
                proba = proba * dic_entrenado["Deportes"].get(palabras[tit], 1*(1 + 0) / (
                        total + 4))  # LAPLACE INCORPORADO
                tit = tit + 1
            proba_deportes[clases].append(proba)

            tit = 0
            proba = probas_de_clase[3]
            while tit < len(palabras):
                proba = proba * dic_entrenado["Salud"].get(palabras[tit], 1*(1 + 0) / (
                        total + 4))  # LAPLACE INCORPORADO
                tit = tit + 1
            proba_salud[clases].append(proba)

            contador = contador + 1

    if clases == 3:  # clase Salud
        contador = 0
        while contador < (len(dic_testeo["Salud"])):

            titulo = dic_testeo["Salud"][contador]
            palabras = titulo.split()
            palabras = funciones.filtrado(palabras)
            funciones.limpiador_test(palabras)

            # calculo de la probabilidad titulo por titulo:
            tit = 0
            proba = probas_de_clase[0]
            while tit < len(palabras):
                proba = proba * dic_entrenado["Nacional"].get(palabras[tit], (1 + 0) / (
                        total + 4))  # LAPLACE INCORPORADO
                tit = tit + 1
            proba_nacional[clases].append(proba)

            tit = 0
            proba = probas_de_clase[1]
            while tit < len(palabras):
                proba = proba * dic_entrenado["Entretenimiento"].get(palabras[tit], (1 + 0) / (
                        total + 4))  # LAPLACE INCORPORADO
                tit = tit + 1
            proba_entretenimiento[clases].append(proba)

            tit = 0
            proba = probas_de_clase[2]
            while tit < len(palabras):
                proba = proba * dic_entrenado["Deportes"].get(palabras[tit], (1 + 0) / (
                        total + 4))  # LAPLACE INCORPORADO
                tit = tit + 1
            proba_deportes[clases].append(proba)

            tit = 0
            proba = probas_de_clase[3]
            while tit < len(palabras):
                proba = proba * dic_entrenado["Salud"].get(palabras[tit],  (1 + 0) / (
                        total + 4))  # LAPLACE INCORPORADO
                tit = tit + 1
            proba_salud[clases].append(proba)

            contador = contador + 1

    clases = clases + 1

print("\n")
print("El testeo termino, ahora vamos a ver los aciertos")
print("Las matrices de probabilidad de Nacional: ")


print("\n")
aciertos = 0
on = 0
nacionales = 0
entretenimineto = 0
deportes = 0
salud = 0
vect1 = []
vect2 = []
vect3 = []
vect4 = []
datos = [[], [], [], []]

while on < 4: # este ciclo me va a dar la cantidad de aciertos por dataset de testeo

    nacionales = 0
    entretenimineto = 0
    deportes = 0
    salud = 0

    if on == 0:
        i = 0
        while i < len(proba_nacional[0]):

            if proba_nacional[0][i] > proba_deportes[0][i] and proba_nacional[0][i] > proba_salud[0][i] and \
                    proba_nacional[0][i] > proba_entretenimiento[0][i]:
                nacionales = nacionales + 1

            if proba_entretenimiento[0][i] > proba_deportes[0][i] and proba_entretenimiento[0][i] > proba_salud[0][
                i] and proba_entretenimiento[0][i] > proba_nacional[0][i]:
                entretenimineto = entretenimineto + 1

            if proba_deportes[0][i] > proba_nacional[0][i] and proba_deportes[0][i] > proba_salud[0][i] and \
                    proba_deportes[0][i] > proba_entretenimiento[0][i]:
                deportes = deportes + 1

            if proba_salud[0][i] > proba_deportes[0][i] and proba_salud[0][i] > proba_nacional[0][i] and proba_salud[0][
                i] > proba_entretenimiento[0][i]:
                salud = salud + 1

            i = i + 1
        vect1 = [nacionales, entretenimineto, deportes, salud] # vector donde guardo las probabilidades


    nacionales = 0
    entretenimineto = 0
    deportes = 0
    salud = 0

    if on == 1:
        i = 0
        while i < len(proba_entretenimiento[1]):

            if proba_nacional[1][i] > proba_deportes[1][i] and proba_nacional[1][i] > proba_salud[1][i] and \
                    proba_nacional[1][i] > \
                    proba_entretenimiento[1][i]:
                nacionales = nacionales + 1

            if proba_entretenimiento[1][i] > proba_deportes[1][i] and proba_entretenimiento[1][i] > proba_salud[1][
                i] and \
                    proba_entretenimiento[1][i] > proba_nacional[1][i]:
                entretenimineto = entretenimineto + 1

            if proba_deportes[1][i] > proba_nacional[1][i] and proba_deportes[1][i] > proba_salud[1][i] and \
                    proba_deportes[1][i] > \
                    proba_entretenimiento[1][i]:
                deportes = deportes + 1

            if proba_salud[1][i] > proba_deportes[1][i] and proba_salud[1][i] > proba_nacional[1][i] and proba_salud[1][
                i] > \
                    proba_entretenimiento[1][i]:
                salud = salud + 1

            i = i + 1
        vect2 = [nacionales, entretenimineto, deportes, salud]

    nacionales = 0
    entretenimineto = 0
    deportes = 0
    salud = 0

    if on == 2:
        i = 0
        while i < len(proba_deportes[2]):

            if proba_nacional[2][i] > proba_deportes[2][i] and proba_nacional[2][i] > proba_salud[2][i] and \
                    proba_nacional[2][i] > \
                    proba_entretenimiento[2][i]:
                nacionales = nacionales + 1

            if proba_entretenimiento[2][i] > proba_deportes[2][i] and proba_entretenimiento[2][i] > proba_salud[2][
                i] and \
                    proba_entretenimiento[2][i] > proba_nacional[2][i]:
                entretenimineto = entretenimineto + 1

            if proba_deportes[2][i] > proba_nacional[2][i] and proba_deportes[2][i] > proba_salud[2][i] and \
                    proba_deportes[2][i] > \
                    proba_entretenimiento[2][i]:
                deportes = deportes + 1

            if proba_salud[2][i] > proba_deportes[2][i] and proba_salud[2][i] > proba_nacional[2][i] and proba_salud[2][
                i] > \
                    proba_entretenimiento[2][i]:
                salud = salud + 1

            i = i + 1
        vect3 = [nacionales, entretenimineto, deportes, salud]

    nacionales = 0
    entretenimineto = 0
    deportes = 0
    salud = 0

    if on == 3:
        i = 0
        while i < len(proba_salud[3]):

            if proba_nacional[3][i] > proba_deportes[3][i] and proba_nacional[3][i] > proba_salud[3][i] and \
                    proba_nacional[3][i] > \
                    proba_entretenimiento[3][i]:
                nacionales = nacionales + 1

            if proba_entretenimiento[3][i] > proba_deportes[3][i] and proba_entretenimiento[3][i] > proba_salud[3][
                i] and \
                    proba_entretenimiento[3][i] > proba_nacional[3][i]:
                entretenimineto = entretenimineto + 1

            if proba_deportes[3][i] > proba_nacional[3][i] and proba_deportes[3][i] > proba_salud[3][i] and \
                    proba_deportes[3][i] > \
                    proba_entretenimiento[3][i]:
                deportes = deportes + 1

            if proba_salud[3][i] > proba_deportes[3][i] and proba_salud[3][i] > proba_nacional[3][i] and proba_salud[3][
                i] > \
                    proba_entretenimiento[3][i]:
                salud = salud + 1

            i = i + 1
        vect4 = [nacionales, entretenimineto, deportes, salud]

    on = on + 1

print("\n")

# <-------------------------------------------------------------------------------------------------------------------->
print("Matrix de confusion")

# ACIERTOS
datos = [vect1, vect2, vect3, vect4]
plt.subplot(1, 2, 1)
ax = sns.heatmap(datos, linewidth=0.5, annot=True, fmt="d")
plt.title("Matriz de confusion aciertos")
plt.xlabel("Prediccion")
plt.ylabel("Real")

# PROBABILIDADES
pvect1 = funciones.divisor_de_listas(vect1, vect1[0] + vect1[1] + vect1[2] + vect1[3])
pvect2 = funciones.divisor_de_listas(vect2, vect2[0] + vect2[1] + vect2[2] + vect2[3])
pvect3 = funciones.divisor_de_listas(vect3, vect3[0] + vect3[1] + vect3[2] + vect3[3])
pvect4 = funciones.divisor_de_listas(vect4, vect4[0] + vect4[1] + vect4[2] + vect4[3])

datos_prob = [pvect1, pvect2, pvect3, pvect4]

plt.subplot(1, 2, 2)
ax_1 = sns.heatmap(datos_prob, linewidth=0.5, annot=True)
plt.title("Matriz de confusion probabilidades")
plt.xlabel("Prediccion")
plt.ylabel("Real")

plt.show()

# <-------------------------------------------------------------------------------------------------------------------->

# Curva ROC

# Utilizamos las mismas listas de probabilidad que usamos antes:

print(len(sorted(proba_nacional[0])))
print(len(sorted(proba_entretenimiento[0])))
print((sorted(proba_deportes[2])))
print(len(sorted(proba_salud[0])))

# Grafico cada punto ==> termino la ROC

cantidad = 1000
umbral = []
i = 1

while i <= cantidad:
    umbral.append((math.pow(1e-1, i)))
    i = i + 1
umbral.append(4)



#umbral =[0,1e-100,1e-90,1e-80,1e-70,1e-60,1e-50,1e-40,1e-30,1e-20,1e-10,1e-1,1,10]

#umbral = list(np.linspace(math.pow(1e-1,40),4,1000))

vp_list = []
vn_list = []
fp_list = []
fn_list = []

cambio_en_humbral = 0
while cambio_en_humbral < len(umbral):
    humbral = umbral[cambio_en_humbral]
    i = 0
    vp = 0
    vn = 0
    fp = 0
    fn = 0
    contador = 0
    while contador < len(proba_salud[3]):  # va mirando las listas de las Probabilidades
        valor = proba_salud[3][contador]  # el valor de la probabilidad

                    #<----------------------------------------------------->
        if valor > humbral and proba_salud[3][contador]>proba_nacional[3][contador] and proba_salud[3][contador]>proba_entretenimiento[3][contador] and proba_salud[3][contador]>proba_deportes[3][contador]:  # en este caso tomamos solamente el caso nacional
            vp = vp + 1
        if valor < humbral and proba_salud[3][contador]>proba_nacional[3][contador] and proba_salud[3][contador]>proba_entretenimiento[3][contador] and proba_salud[3][contador]>proba_deportes[3][contador]:
            fn = fn + 1

                    #<----------------------------------------------------->
        if valor > humbral and (proba_salud[3][contador]<proba_nacional[3][contador] or proba_salud[3][contador]<proba_entretenimiento[3][contador] or proba_salud[3][contador]<proba_deportes[3][contador]):  # Todos los otros casos
            fp = fp + 1
        if valor < humbral and (proba_salud[3][contador]<proba_nacional[3][contador] or proba_salud[3][contador]<proba_entretenimiento[3][contador] or proba_salud[3][contador]<proba_deportes[3][contador]):
            vn = vn + 1

        contador = contador + 1

        # Cargamos las listas
    vp_list.append(vp)
    vn_list.append(vn)
    fp_list.append(fp)
    fn_list.append(fn)

    cambio_en_humbral = cambio_en_humbral + 1

print(vp_list)
print(vn_list)
print(fp_list)
print(fn_list)

tvp = []
tvp.append(0)
i = 0
while i < len(vp_list):
    tvp.append((vp_list[i]) / (vp_list[i] + fn_list[i]))
    i = i + 1

tfp = []
tfp.append(0)
i = 0
while i < len(vn_list):
    tfp.append((fp_list[i]) / (fp_list[i] + vn_list[i]))
    i = i + 1

print("\n")
print("Las tas me quedan:")
print("TASA de Verdaderos positivos: " + str(tvp))
print("TASA DE Falsos positivos: " + str(tfp))

print("Mi primera curva ROC: ")

#grafico cada punto ==> termino la ROC

linealx = [0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1]
linealy = [0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1]

plt.plot(tfp, tvp)
plt.plot(linealx, linealy)
plt.title("CURVA ROC Salud")
plt.xlabel("Tasa de Falsos positivos")
plt.ylabel("Tasa de Verdaderos positivos")
plt.show()

