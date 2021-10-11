# <-------------------------------------------------------------------------------------------------------------------->
# Ej 2:

import math
import random
import funciones
import pandas as pd  # solo para importar el archivo
import matplotlib.pyplot as plt
import seaborn as sns

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

# <-------------------------------------------------------------------------------------------------------------------->
# Armamos las clases de Entrenamiento y de testeo por clase aleatoriamente

# ENTRENAMIENTO

coef = 80  # Armo un dataset con el 80% de datos para entrenar y un 20% de datos para testear (sobre los totales ingresados)

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

# <-------------------------------------------------------------------------------------------------------------------->

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

nacional_test = nacional_total
entretetenimiento_test = entretenimiento_total
deportes_test = deportes_total
salud_test = salud_total

# TESTEO

dic_testeo = {"Nacional": nacional_test,
              "Entretenimiento": entretetenimiento_test,
              "Deportes": deportes_test,
              "Salud": salud_test}

# <-------------------------------------------------------------------------------------------------------------------->
# Filtrado de palabras spam

dic_filtrado = funciones.filtrado_dic(dic_entrenamiento)# me entrega un diccionario de esta forma==> DIC={"CLASE":[lista de palabras en esta clase]}

# <-------------------------------------------------------------------------------------------------------------------->
# Entrenamiento

dic_entrenado = funciones.entrenador(dic_filtrado)# ENTRENAMIENTO

# <-------------------------------------------------------------------------------------------------------------------->
# Algunos parametros

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

# <-------------------------------------------------------------------------------------------------------------------->

print(dic_entrenado["Nacional"])

# <-------------------------------------------------------------------------------------------------------------------->


