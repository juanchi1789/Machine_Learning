# Ejercicio 2
import pandas as pd
import numpy as np

array = pd.read_csv("Noticias_argentinas.csv")
data = array.values

print("Consideraciones iniciales: \n")
print("El dataset de Noticias detacadas no se tomara en cuenta")
print("vamos a usar 8 clases \n")

# <--------------------------------------->
# CLASES:

# Nacional -------> 3860
# Destacada -------> 3859
# Deportes -------> 3855
# Salud -------> 3840
# Ciecia y tec -------> 3856
# Entretenimiento -------> 3850
# Economia ------->3850
# Internacional -------> 3850

# <--------------------------------------->

# Tenemos que crear nuestra dateset de ENTRENAMIENTO y la de TESTEO

print("Se considero que la mitad de los datos de cada clase son de Entrenamiento y la otra mitad de Testeo")

# Armamos los DATASETS TOTALES:

nacional_total = list()
destacada_total = list()
deportes_total = list()
salud_total = list()
cyt_total = list()
entretenimiento_total = list()
economia_total = list()
internacional_total = list()

arreglo_total = [nacional_total, destacada_total, deportes_total, salud_total, cyt_total, entretenimiento_total,
                 economia_total, internacional_total]

nacional_entr = list()
destacada_entr = list()
deportes_entr = list()
salud_entr = list()
cyt_entr = list()
entretenimiento_entr = list()
economia_entr = list()
internacional_entr = list()

nacional_test = list()
destacada_test = list()
deportes_test = list()
salud_test = list()
cyt_test = list()
entretenimiento_test = list()
economia_test = list()
internacional_test = list()

print("\n")

# Me gustaria poder hacer una funcion como la siguiente:
# noticias_clasificador(data,numero_de_clases_a_estudiar,porcent_entrenamiento_vs_testeo)


# CARGAMOS LOS TITULARES A LAS LISTA TOTAL

# lista nacional

print("Se crean las listas totales \n")

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

contador = 0
while contador < len(data):
    if data[contador][3] == "Ciencia y Tecnologia":
        cyt_total.append(data[contador][1])
    contador = contador + 1

contador = 0
while contador < len(data):
    if data[contador][3] == "Entretenimiento":
        entretenimiento_total.append(data[contador][1])
    contador = contador + 1

contador = 0
while contador < len(data):
    if data[contador][3] == "Economia":
        economia_total.append(data[contador][1])
    contador = contador + 1

contador = 0
while contador < len(data):
    if data[contador][3] == "Internacional":
        internacional_total.append(data[contador][1])
    contador = contador + 1

print("Las listas totales fueron creadas \n")

print("Se cargan las listas de testeo y entrenamiento")

contador = 0

i = 0

coef = 3  # el coeficiente que determina que porcentaje de la lista original va para el dataset de entenamiento o de testeo

nacional_entr = nacional_total[0:int(len(nacional_total) / coef)]
nacional_test = nacional_total[int(len(nacional_total) / coef):len(nacional_total)]

internacional_entr = internacional_total[0:int(len(internacional_total) / coef)]
internacional_test = internacional_total[int(len(internacional_total) / coef):len(internacional_total)]

destacada_entr = destacada_total[0:int(len(destacada_total) / coef)]
destacada_test = destacada_total[int(len(destacada_total) / coef):len(destacada_total)]

deportes_entr = deportes_total[0:int(len(deportes_total) / coef)]
deportes_test = deportes_total[int(len(deportes_total) / coef):len(deportes_total)]

salud_entr = salud_total[0:int(len(salud_total) / coef)]
salud_test = salud_total[int(len(salud_total) / coef):len(salud_total)]

cyt_entr = cyt_total[0:int(len(cyt_total) / coef)]
cyt_test = cyt_total[int(len(cyt_total) / coef):len(cyt_total)]

entretenimiento_entr = entretenimiento_total[0:int(len(entretenimiento_total) / coef)]
entretenimiento_test = entretenimiento_total[int(len(entretenimiento_total) / coef):len(entretenimiento_total)]

economia_entr = economia_total[0:int(len(economia_total) / coef)]
economia_test = economia_total[int(len(economia_total) / coef):len(economia_total)]

print("Las listas de entrenamiento y testeo fueron creadas \n")

print("Diccionario \n")

print("Vamos a armar la lista de las palabras por cada clase \n")


# El metodo split() ==> separa un string en una lista de las palabras que la forman

def palabras(lista):
    i = 0
    lista_de_palabras = []
    while i < len(lista):  # el primer cicli recorre la lista de titulos
        frase = lista[i].split()  # por cada titulo armamos una lista de sus palabras
        contador = 0
        while contador < len(frase):  # este ciclo opera sobre cada titulo (sobre la lista de palabras de cada titulo)

            frase[contador] = frase[contador].replace(",", "")  # Limpio los datos, ya que pueden generar conflictos
            frase[contador] = frase[contador].replace(":", "")
            frase[contador] = frase[contador].replace("+", "")
            frase[contador] = frase[contador].replace("?", "")
            frase[contador] = frase[contador].replace("¿", "")
            frase[contador] = frase[contador].replace("'", "")
            frase[contador] = frase[contador].replace('"', "")
            frase[contador] = frase[contador].replace('!', "")
            frase[contador] = frase[contador].replace('¡', "")
            frase[contador] = frase[contador].replace('\x9d', "")

            # if frase[contador].lower() in lista_de_palabras:  # veo si la palabra esta en la lista que voy armando
            #   contador = contador + 1
            # else:
            lista_de_palabras.append(frase[contador].lower())  # si la palabra no esta la elimino
            contador = contador + 1
        i = i + 1
    return lista_de_palabras


palabras_nacional = palabras(nacional_entr)
palabras_destacada = palabras(destacada_entr)
palabras_deportes = palabras(deportes_entr)
palabras_salud = palabras(salud_entr)
palabras_cyt = palabras(cyt_entr)
palabras_entretenimiento = palabras(entretenimiento_entr)
palabras_economia = palabras(economia_entr)
palabras_internacional = palabras(internacional_entr)

print("La lista de palabras para cada clase de entrenamiento fueron creadas \n")

print("Se procede a armar el diccionario")

# el diccionario que se va a diseñar es de tipo anidado

# La clase va a estar vinculada con las palabras y a su vez estas palabras lo estaran con la cantidad de veces que aparen
# en el arreglo

dic_nacional = {}
dic_destacada = {}
dic_deportes = {}
dic_salud = {}
dic_cyt = {}
dic_entretenimiento = {}
dic_economia = {}
dic_international = {}

print("Se procede a calcular las probabilidades 'a priori' \n")

print("Se calculan las probabilidades de cada clase \n")

prob_nacional = 1 / 8
prob_destacada = 1 / 8
prob_deportes = 1 / 8
prob_salud = 1 / 8
prob_cyt = 1 / 8
prob_entretenimiento = 1 / 8
prob_economia = 1 / 8
prob_internacional = 1 / 8

print("Las probabilidades de cada clase fueron calculadas\n")

print("Se proceden a calcular las probablidades condicionales de cada palbra en cada clase y a armar el diccionario")

i = 0
veces = 0

while i < len(palabras_nacional):
    veces = palabras_nacional.count(palabras_nacional[i])
    dic_nacional.update({palabras_nacional[i]: float((veces / len(palabras_nacional)) * prob_nacional)})
    i = i + 1
print(len(dic_nacional))

print("Diccionario nacional terminado\n")

veces = 0
i = 0
while i < len(palabras_destacada):
    veces = palabras_destacada.count(palabras_destacada[i])
    dic_destacada.update({palabras_destacada[i]: (veces / len(palabras_destacada)) * prob_destacada})
    i = i + 1
print(len(dic_destacada))
print("Diccionario destacada terminado\n")

veces = 0
i = 0
while i < len(palabras_deportes):
    veces = palabras_deportes.count(palabras_deportes[i])
    dic_deportes.update({palabras_deportes[i]: (veces / len(palabras_deportes)) * prob_deportes})
    i = i + 1
print(len(dic_deportes))
print("Diccionario deportes terminado\n")

veces = 0
i = 0
while i < len(palabras_salud):
    veces = palabras_salud.count(palabras_salud[i])
    dic_salud.update({palabras_salud[i]: (veces / len(palabras_salud)) * prob_deportes})
    i = i + 1
print(len(dic_salud))
print("Diccionario salud terminado\n")

veces = 0
i = 0
while i < len(palabras_cyt):
    veces = palabras_cyt.count(palabras_cyt[i])
    dic_cyt.update({palabras_cyt[i]: (veces / len(palabras_cyt)) * prob_cyt})
    i = i + 1
print(len(dic_cyt))
print("Diccionario cyt terminado\n")

veces = 0
i = 0
while i < len(palabras_entretenimiento):
    veces = palabras_entretenimiento.count(palabras_entretenimiento[i])
    dic_entretenimiento.update(
        {palabras_entretenimiento[i]: (veces / len(palabras_entretenimiento)) * prob_entretenimiento})
    i = i + 1
print(len(dic_entretenimiento))
print("Diccionario entretenimiento terminado\n")

veces = 0
i = 0
while i < len(palabras_economia):
    veces = palabras_economia.count(palabras_economia[i])
    dic_economia.update({palabras_economia[i]: (veces / len(palabras_economia)) * prob_economia})
    i = i + 1
print(len(dic_economia))
print("Diccionario economia terminado\n")

veces = 0
i = 0
while i < len(palabras_internacional):
    veces = palabras_internacional.count(palabras_internacional[i])
    dic_international.update({palabras_internacional[i]: (veces / len(palabras_internacional)) * prob_internacional})
    i = i + 1
print(len(dic_international))

print("Diccionario internacional terminado\n")

print("Diccionarios de probabilidad condicional terminados")

print("El entretenimiento termino, desde aqui comenzamos con la evaluacion de los datesets de Testeo")

# los datasets de testeo son los siguientes:

# nacional_test
# destacada_test
# deportes_test
# salud_test
# cyt_test
# entretenimiento_test
# economia_test
# internacional_test

# voy a ir seccion por seccion calculando las probabilidades de que cada titulo sea de la seccion correspondiente
# y luego tengo que calcular cuan "Eficiente" es mi modelo, para esto tengo que


# testeo a menor escala


titulo = "El pais vive un estado de desesperacion desde"
frase = titulo.split()
print("La porbabilidad de que sea nacional: ")

prob_nacional =1/8
i = 0
while i < len(frase):
    frase[i] = frase[i].replace(",", "")  # Limpio los datos, ya que pueden generar conflictos
    frase[i] = frase[i].replace(":", "")
    frase[i] = frase[i].replace("+", "")
    frase[i] = frase[i].replace("?", "")
    frase[i] = frase[i].replace("¿", "")
    frase[i] = frase[i].replace("'", "")
    frase[i] = frase[i].replace('"', "")
    frase[i] = frase[i].replace('!', "")
    frase[i] = frase[i].replace('¡', "")
    frase[i] = frase[i].replace('\x9d', "")

    if dic_nacional.get(frase[i].lower()) is None:
        prob_nacional = 1/(8 + 14) * prob_nacional # cooreccion de laplace
    else:
        prob_nacional = float(dic_nacional.get(frase[i].lower())) * prob_nacional
    i = i + 1

print("la prob de que sea nacional es: "+str(prob_nacional))



def clase_maxima(lista_test,dic_nacional,dic_destacada,dic_deportes,dic_salud,dic_cyt,dic_entretenimiento,dic_economia,dic_international):

    dic_probabilidades = {}# donde voy a tener las clases y las probabilidades de que el titulo sea de una clase
    i = 0 # se va a mover sobre los titulos hasta el ultimo de ellos
    contador = 0 # se va a mover sobre las palabras del titulo

    while i < len(lista_test):

        frase = lista_test[i].split # Agarramos al titulo

        prob = 1/8

        while contador < len(frase):
            frase[contador] = frase[contador].replace(",", "")  # Limpio los datos, ya que pueden generar conflictos
            frase[contador] = frase[contador].replace(":", "")
            frase[contador] = frase[contador].replace("+", "")
            frase[contador] = frase[contador].replace("?", "")
            frase[contador] = frase[contador].replace("¿", "")
            frase[contador] = frase[contador].replace("'", "")
            frase[contador] = frase[contador].replace('"', "")
            frase[contador] = frase[contador].replace('!', "")
            frase[contador] = frase[contador].replace('¡', "")
            frase[contador] = frase[contador].replace('\x9d', "")

            if dic_nacional.get(frase[contador].lower()) is None:
                prob = 1 / (8 + 14) * prob  # cooreccion de laplace
            else:
                prob = float(dic_nacional.get(frase[contador].lower())) * prob
            contador = contador + 1

        dic_probabilidades.update({"Nacional":prob}) # Nacional !!

        contador = 0
        prob = 1/8
        while contador < len(frase):
            frase[contador] = frase[contador].replace(",", "")  # Limpio los datos, ya que pueden generar conflictos
            frase[contador] = frase[contador].replace(":", "")
            frase[contador] = frase[contador].replace("+", "")
            frase[contador] = frase[contador].replace("?", "")
            frase[contador] = frase[contador].replace("¿", "")
            frase[contador] = frase[contador].replace("'", "")
            frase[contador] = frase[contador].replace('"', "")
            frase[contador] = frase[contador].replace('!', "")
            frase[contador] = frase[contador].replace('¡', "")
            frase[contador] = frase[contador].replace('\x9d', "")

            if dic_destacada.get(frase[contador].lower()) is None:
                prob = 1 / (8 + 14) * prob  # cooreccion de laplace
            else:
                prob = float(dic_destacada.get(frase[contador].lower())) * prob
            contador = contador + 1

        dic_probabilidades.update({"Destacada": prob})  # Destacada !!

        contador = 0
        prob = 1 / 8
        while contador < len(frase):
            frase[contador] = frase[contador].replace(",", "")  # Limpio los datos, ya que pueden generar conflictos
            frase[contador] = frase[contador].replace(":", "")
            frase[contador] = frase[contador].replace("+", "")
            frase[contador] = frase[contador].replace("?", "")
            frase[contador] = frase[contador].replace("¿", "")
            frase[contador] = frase[contador].replace("'", "")
            frase[contador] = frase[contador].replace('"', "")
            frase[contador] = frase[contador].replace('!', "")
            frase[contador] = frase[contador].replace('¡', "")
            frase[contador] = frase[contador].replace('\x9d', "")

            if dic_deportes.get(frase[contador].lower()) is None:
                prob = 1 / (8 + 14) * prob  # cooreccion de laplace
            else:
                prob = float(dic_deportes.get(frase[contador].lower())) * prob
            contador = contador + 1

        dic_probabilidades.update({"Deportes": prob})  # Deportes !!

        contador = 0
        prob = 1 / 8
        while contador < len(frase):
            frase[contador] = frase[contador].replace(",", "")  # Limpio los datos, ya que pueden generar conflictos
            frase[contador] = frase[contador].replace(":", "")
            frase[contador] = frase[contador].replace("+", "")
            frase[contador] = frase[contador].replace("?", "")
            frase[contador] = frase[contador].replace("¿", "")
            frase[contador] = frase[contador].replace("'", "")
            frase[contador] = frase[contador].replace('"', "")
            frase[contador] = frase[contador].replace('!', "")
            frase[contador] = frase[contador].replace('¡', "")
            frase[contador] = frase[contador].replace('\x9d', "")

            if dic_salud.get(frase[contador].lower()) is None:
                prob = 1 / (8 + 14) * prob  # cooreccion de laplace
            else:
                prob = float(dic_salud.get(frase[contador].lower())) * prob
            contador = contador + 1

        dic_probabilidades.update({"Salud": prob})  # Salud !!

        contador = 0
        prob = 1 / 8
        while contador < len(frase):
            frase[contador] = frase[contador].replace(",", "")  # Limpio los datos, ya que pueden generar conflictos
            frase[contador] = frase[contador].replace(":", "")
            frase[contador] = frase[contador].replace("+", "")
            frase[contador] = frase[contador].replace("?", "")
            frase[contador] = frase[contador].replace("¿", "")
            frase[contador] = frase[contador].replace("'", "")
            frase[contador] = frase[contador].replace('"', "")
            frase[contador] = frase[contador].replace('!', "")
            frase[contador] = frase[contador].replace('¡', "")
            frase[contador] = frase[contador].replace('\x9d', "")

            if dic_cyt.get(frase[contador].lower()) is None:
                prob = 1 / (8 + 14) * prob  # cooreccion de laplace
            else:
                prob = float(dic_cyt.get(frase[contador].lower())) * prob
            contador = contador + 1

        dic_probabilidades.update({"CyT": prob})  # CyT !!

        contador = 0
        prob = 1 / 8
        while contador < len(frase):
            frase[contador] = frase[contador].replace(",", "")  # Limpio los datos, ya que pueden generar conflictos
            frase[contador] = frase[contador].replace(":", "")
            frase[contador] = frase[contador].replace("+", "")
            frase[contador] = frase[contador].replace("?", "")
            frase[contador] = frase[contador].replace("¿", "")
            frase[contador] = frase[contador].replace("'", "")
            frase[contador] = frase[contador].replace('"', "")
            frase[contador] = frase[contador].replace('!', "")
            frase[contador] = frase[contador].replace('¡', "")
            frase[contador] = frase[contador].replace('\x9d', "")

            if dic_entretenimiento.get(frase[contador].lower()) is None:
                prob = 1 / (8 + 14) * prob  # cooreccion de laplace
            else:
                prob = float(dic_entretenimiento.get(frase[contador].lower())) * prob
            contador = contador + 1

        dic_probabilidades.update({"Entretenimiento": prob})  # Entretenimiento !!

        contador = 0
        prob = 1 / 8
        while contador < len(frase):
            frase[contador] = frase[contador].replace(",", "")  # Limpio los datos, ya que pueden generar conflictos
            frase[contador] = frase[contador].replace(":", "")
            frase[contador] = frase[contador].replace("+", "")
            frase[contador] = frase[contador].replace("?", "")
            frase[contador] = frase[contador].replace("¿", "")
            frase[contador] = frase[contador].replace("'", "")
            frase[contador] = frase[contador].replace('"', "")
            frase[contador] = frase[contador].replace('!', "")
            frase[contador] = frase[contador].replace('¡', "")
            frase[contador] = frase[contador].replace('\x9d', "")

            if dic_economia.get(frase[contador].lower()) is None:
                prob = 1 / (8 + 14) * prob  # cooreccion de laplace
            else:
                prob = float(dic_economia.get(frase[contador].lower())) * prob
            contador = contador + 1

        dic_probabilidades.update({"Economia": prob})  # Economia !!

        contador = 0
        prob = 1 / 8
        while contador < len(frase):
            frase[contador] = frase[contador].replace(",", "")  # Limpio los datos, ya que pueden generar conflictos
            frase[contador] = frase[contador].replace(":", "")
            frase[contador] = frase[contador].replace("+", "")
            frase[contador] = frase[contador].replace("?", "")
            frase[contador] = frase[contador].replace("¿", "")
            frase[contador] = frase[contador].replace("'", "")
            frase[contador] = frase[contador].replace('"', "")
            frase[contador] = frase[contador].replace('!', "")
            frase[contador] = frase[contador].replace('¡', "")
            frase[contador] = frase[contador].replace('\x9d', "")

            if dic_international.get(frase[contador].lower()) is None:
                prob = 1 / (8 + 14) * prob  # cooreccion de laplace
            else:
                prob = float(dic_international.get(frase[contador].lower())) * prob
            contador = contador + 1

        dic_probabilidades.update({"International": prob})  # International !!

        i = i + 1

    return dic_probabilidades

lista = []
clase_maxima()