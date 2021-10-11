# Ejercicio 2
import pandas as pd

array = pd.read_csv("Noticias_argentinas.csv")
data = array.values

print("Consideraciones iniciales: \n")
print("El dataset de Noticias detacadas no se tomara en cuenta")
print("vamos a usar 4 clases \n")

# <--------------------------------------->
# CLASES:

# Nacional -------> 3860
# Destacada -------> 3859
# Deportes -------> 3855
# Salud -------> 3840

# <--------------------------------------->

# Tenemos que crear nuestra dateset de ENTRENAMIENTO y la de TESTEO

print("Se considero que la mitad de los datos de cada clase son de Entrenamiento y la otra mitad de Testeo")

# Armamos los DATASETS TOTALES:

nacional_total = list()
destacada_total = list()
deportes_total = list()
salud_total = list()

arreglo_total = [nacional_total, destacada_total, deportes_total, salud_total]

nacional_entr = list()
destacada_entr = list()
deportes_entr = list()
salud_entr = list()

nacional_test = list()
destacada_test = list()
deportes_test = list()
salud_test = list()

print("\n")

# CARGAMOS LOS TITULARES A LAS LISTA TOTAL


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

print("Las listas totales fueron creadas \n")

print("Se cargan las listas de testeo y entrenamiento")

contador = 0

i = 0

coef = 1.25    # el coeficiente que determina que porcentaje de la lista original va para el dataset de entenamiento o de testeo

nacional_entr = nacional_total[0:int(len(nacional_total) / coef)]
nacional_test = nacional_total[int(len(nacional_total) / coef):len(nacional_total)-1]

destacada_entr = destacada_total[0:int(len(destacada_total) / coef)]
destacada_test = destacada_total[int(len(destacada_total) / coef):len(destacada_total)-1]

deportes_entr = deportes_total[0:int(len(deportes_total) / coef)]
deportes_test = deportes_total[int(len(deportes_total) / coef):len(deportes_total)-1]

salud_entr = salud_total[0:int(len(salud_total) / coef)]
salud_test = salud_total[int(len(salud_total) / coef):len(salud_total)-1]

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

palabras_totales = len(palabras_nacional) + len(palabras_destacada) + len(palabras_deportes) + len(palabras_salud)

print("La lista de palabras para cada clase de entrenamiento fueron creadas \n")

print("Se procede a armar el diccionario")

# el diccionario que se va a diseñar es de tipo anidado

# La clase va a estar vinculada con las palabras y a su vez estas palabras lo estaran con la cantidad de veces que aparen
# en el arreglo

dic_nacional = {}
dic_destacada = {}
dic_deportes = {}
dic_salud = {}

print("Se procede a calcular las probabilidades 'a priori' \n")

print("Se calculan las probabilidades de cada clase \n")

prob_nacional = len(palabras_nacional) / (palabras_totales)
prob_destacada = len(palabras_destacada) / (palabras_totales)
prob_deportes = len(palabras_deportes) / (palabras_totales)
prob_salud = len(palabras_salud) / (palabras_totales)

print("la probabilidad de que sea Nacional: " + str(prob_nacional))
print("la probabilidad de que sea destacada: " + str(prob_destacada))
print("la probabilidad de que sea deportes: " + str(prob_deportes))
print("la probabilidad de que sea salud: " + str(prob_salud))


print("\n Las probabilidades de cada clase fueron calculadas \n")

print("Se proceden a calcular las probablidades condicionales de cada palbra en cada clase y a armar el diccionario")

i = 0
veces = 0
while i < len(palabras_nacional):
    veces = palabras_nacional.count(palabras_nacional[i])
    dic_nacional.update({palabras_nacional[i]: float((veces / len(palabras_nacional)))})
    i = i + 1
print(len(dic_nacional))

print("Diccionario nacional terminado\n")

veces = 0
i = 0
while i < len(palabras_destacada):
    veces = palabras_destacada.count(palabras_destacada[i])
    dic_destacada.update({palabras_destacada[i]: float(veces / len(palabras_destacada))})
    i = i + 1
print(len(dic_destacada))
print("Diccionario destacada terminado\n")

veces = 0
i = 0
while i < len(palabras_deportes):
    veces = palabras_deportes.count(palabras_deportes[i])
    dic_deportes.update({palabras_deportes[i]: float(veces / len(palabras_deportes))})
    i = i + 1
print(len(dic_deportes))
print("Diccionario deportes terminado\n")

veces = 0
i = 0
while i < len(palabras_salud):
    veces = palabras_salud.count(palabras_salud[i])
    dic_salud.update({palabras_salud[i]: float(veces / len(palabras_salud))})
    i = i + 1
print(len(dic_salud))
print("Diccionario salud terminado\n")


print("Diccionario internacional terminado\n")

print("Diccionarios de probabilidad condicional terminados")

print("El entretenimiento termino, desde aqui comenzamos con la evaluacion de los datesets de Testeo")

# los datasets de testeo son los siguientes:

# nacional_test
# destacada_test
# deportes_test
# salud_test


# voy a ir seccion por seccion calculando las probabilidades de que cada titulo sea de la seccion correspondiente
# y luego tengo que calcular cuan "Eficiente" es mi modelo, para esto tengo que

print("Para la lista que yo se que es nacional: \n")

laplace = 1/(4+palabras_totales)

max_nacional = []
i = 0  # se va a mover sobre los titulos hasta el ultimo de ellos
contador = 0  # se va a mover sobre las palabras del titulo

while i < len(nacional_test):
    frase = nacional_test[i].split()  # Agarramos al titulo
    prob = prob_nacional
    contador = 0
    while contador < len(frase):

        if dic_nacional.get(frase[contador].lower()) is None:
            prob = laplace * prob  # cooreccion de laplace
        else:
            prob = float(dic_nacional.get(frase[contador].lower())) * prob
        contador = contador + 1
    max_nacional.append(prob)
    i = i + 1

max_destacada = []
i = 0  # se va a mover sobre los titulos hasta el ultimo de ellos
contador = 0  # se va a mover sobre las palabras del titulo
while i < len(nacional_test):
    frase = nacional_test[i].split()  # Agarramos al titulo
    prob = prob_destacada
    contador = 0
    while contador < len(frase):
        if dic_destacada.get(frase[contador].lower()) is None:
            prob = laplace * prob  # cooreccion de laplace
        else:
            prob = float(dic_destacada.get(frase[contador].lower())) * prob
        contador = contador + 1
    max_destacada.append(prob)
    i = i + 1

max_deportes = []
i = 0  # se va a mover sobre los titulos hasta el ultimo de ellos
contador = 0  # se va a mover sobre las palabras del titulo
while i < len(nacional_test):
    frase = nacional_test[i].split()  # Agarramos al titulo
    prob = prob_deportes
    contador = 0
    while contador < len(frase):

        if dic_deportes.get(frase[contador].lower()) is None:
            prob = laplace * prob  # cooreccion de laplace
        else:
            prob = float(dic_deportes.get(frase[contador].lower())) * prob
        contador = contador + 1

    max_deportes.append(prob)
    i = i + 1

max_salud = []
i = 0  # se va a mover sobre los titulos hasta el ultimo de ellos
contador = 0  # se va a mover sobre las palabras del titulo
while i < len(nacional_test):
    frase = nacional_test[i].split()  # Agarramos al titulo
    prob = prob_salud
    contador = 0
    while contador < len(frase):

        if dic_salud.get(frase[contador].lower()) is None:
            prob = laplace * prob  # cooreccion de laplace
        else:
            prob = float(dic_salud.get(frase[contador].lower())) * prob
        contador = contador + 1

    max_salud.append(prob)
    i = i + 1

print("Las maximas para la lista de Nacional estan completas \n")
print("Vamos a ver a cuantos no le acertamos")

i = 0
resultados = []
while i < len(max_nacional):
    if max_nacional[i] > max_destacada[i] and max_nacional[i] > max_deportes[i] and max_nacional[i] > max_salud[i]:
        resultados.append("Correcto")
    else:
        resultados.append("Incorrecto")
    i = i + 1

print("Los resultados tan esperados son:")
print("La longitud es: " + str(len(resultados)))

print(resultados)

print("Vamos a ver cuan mal nos fue: ")
i = 0
correctos = 0
incorrectos = 0

while i < len(resultados):
    if resultados[i] == "Correcto":
        correctos = correctos + 1
    else:
        incorrectos = incorrectos + 1
    i = i + 1

print("La probabilidad de acertar " + str(correctos / len(resultados)))
valor_nacional_nacional = correctos / len(resultados)
vp_nac = resultados.count("Correcto")/len(resultados)
fp_nac = resultados.count("Incorrecto")/len(resultados)
print("La probabilidad de no acertar " + str(incorrectos / len(resultados)))
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------

print("Para la lista que yo se que es destacada: \n")

max_nacional = []
i = 0  # se va a mover sobre los titulos hasta el ultimo de ellos
contador = 0  # se va a mover sobre las palabras del titulo

while i < len(destacada_test):
    frase = destacada_test[i].split()  # Agarramos al titulo
    prob = prob_nacional
    contador = 0
    while contador < len(frase):

        if dic_nacional.get(frase[contador].lower()) is None:
            prob = laplace * prob  # cooreccion de laplace
        else:
            prob = float(dic_nacional.get(frase[contador].lower())) * prob
        contador = contador + 1

    max_nacional.append(prob)
    i = i + 1

max_destacada = []
i = 0  # se va a mover sobre los titulos hasta el ultimo de ellos
contador = 0  # se va a mover sobre las palabras del titulo
while i < len(destacada_test):
    frase = destacada_test[i].split()  # Agarramos al titulo
    prob = prob_destacada
    contador = 0
    while contador < len(frase):

        if dic_destacada.get(frase[contador].lower()) is None:
            prob = laplace * prob  # cooreccion de laplace
        else:
            prob = float(dic_destacada.get(frase[contador].lower())) * prob
        contador = contador + 1

    max_destacada.append(prob)
    i = i + 1

max_deportes = []
i = 0  # se va a mover sobre los titulos hasta el ultimo de ellos
contador = 0  # se va a mover sobre las palabras del titulo
while i < len(destacada_test):
    frase = destacada_test[i].split()  # Agarramos al titulo
    prob = prob_deportes
    contador = 0
    while contador < len(frase):

        if dic_deportes.get(frase[contador].lower()) is None:
            prob = laplace * prob  # cooreccion de laplace
        else:
            prob = float(dic_deportes.get(frase[contador].lower())) * prob
        contador = contador + 1

    max_deportes.append(prob)
    i = i + 1

max_salud = []
i = 0  # se va a mover sobre los titulos hasta el ultimo de ellos
contador = 0  # se va a mover sobre las palabras del titulo
while i < len(destacada_test):
    frase = destacada_test[i].split()  # Agarramos al titulo
    prob = prob_salud
    contador = 0
    while contador < len(frase):

        if dic_salud.get(frase[contador].lower()) is None:
            prob = laplace * prob  # cooreccion de laplace
        else:
            prob = float(dic_salud.get(frase[contador].lower())) * prob
        contador = contador + 1

    max_salud.append(prob)
    i = i + 1

print("Las maximas para la lista de Nacional estan completas \n")
print("Vamos a ver a cuantos no le acertamos")

i = 0
resultados = []
while i < len(max_nacional):
    if max_nacional[i] > max_destacada[i] and max_nacional[i] > max_deportes[i] and max_nacional[i] > max_salud[i]:
        resultados.append("Correcto")
    else:
        resultados.append("Incorrecto")
    i = i + 1

print("---------> 2)Los resultados tan esperados son:")
print("De longitud : " + str(len(resultados)))

print(resultados)

print("Vamos a ver cuan mal nos fue: ")
i = 0
correctos = 0
incorrectos = 0

while i < len(resultados):
    if resultados[i] == "Correcto":
        correctos = correctos + 1
    else:
        incorrectos = incorrectos + 1
    i = i + 1

print("La probabilidad de acertar " + str(correctos / len(resultados)))
valor_destacado_destacado = correctos / len(resultados)
vp_dest = resultados.count("Correcto")/len(resultados)
fp_dest = resultados.count("Incorrecto")/len(resultados)
print("La probabilidad de no acertar " + str(incorrectos / len(resultados)))

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------

print("Para la lista que yo se que es de Deportes: \n")

max_nacional = []
i = 0  # se va a mover sobre los titulos hasta el ultimo de ellos
contador = 0  # se va a mover sobre las palabras del titulo

while i < len(deportes_test):
    frase = deportes_test[i].split()  # Agarramos al titulo
    prob = prob_nacional
    contador = 0
    while contador < len(frase):

        if dic_nacional.get(frase[contador].lower()) is None:
            prob = laplace * prob  # cooreccion de laplace
        else:
            prob = float(dic_nacional.get(frase[contador].lower())) * prob
        contador = contador + 1

    max_nacional.append(prob)
    i = i + 1

max_destacada = []
i = 0  # se va a mover sobre los titulos hasta el ultimo de ellos
contador = 0  # se va a mover sobre las palabras del titulo
while i < len(deportes_test):
    frase = deportes_test[i].split()  # Agarramos al titulo
    prob = prob_destacada
    contador = 0
    while contador < len(frase):

        if dic_destacada.get(frase[contador].lower()) is None:
            prob = laplace * prob  # cooreccion de laplace
        else:
            prob = float(dic_destacada.get(frase[contador].lower())) * prob
        contador = contador + 1

    max_destacada.append(prob)
    i = i + 1

max_deportes = []
i = 0  # se va a mover sobre los titulos hasta el ultimo de ellos
contador = 0  # se va a mover sobre las palabras del titulo
while i < len(deportes_test):
    frase = deportes_test[i].split()  # Agarramos al titulo
    prob = prob_deportes
    contador = 0
    while contador < len(frase):

        if dic_deportes.get(frase[contador].lower()) is None:
            prob = laplace * prob  # cooreccion de laplace
        else:
            prob = float(dic_deportes.get(frase[contador].lower())) * prob
        contador = contador + 1

    max_deportes.append(prob)
    i = i + 1

max_salud = []
i = 0  # se va a mover sobre los titulos hasta el ultimo de ellos
contador = 0  # se va a mover sobre las palabras del titulo
while i < len(deportes_test):
    frase = deportes_test[i].split()  # Agarramos al titulo
    prob = prob_salud
    contador = 0
    while contador < len(frase):

        if dic_salud.get(frase[contador].lower()) is None:
            prob = laplace * prob  # cooreccion de laplace
        else:
            prob = float(dic_salud.get(frase[contador].lower())) * prob
        contador = contador + 1

    max_salud.append(prob)
    i = i + 1

print("Las maximas para la lista de Nacional estan completas \n")
print("Vamos a ver a cuantos no le acertamos")

i = 0
resultados = []
while i < len(max_nacional):
    if max_nacional[i] > max_destacada[i] and max_nacional[i] > max_deportes[i] and max_nacional[i] > max_salud[i]:
        resultados.append("Correcto")
    else:
        resultados.append("Incorrecto")
    i = i + 1

print("---------> 3)Los resultados tan esperados son:")
print("De longitud : " + str(len(resultados)))

print(resultados)

print("Vamos a ver cuan mal nos fue: ")
i = 0
correctos = 0
incorrectos = 0

while i < len(resultados):
    if resultados[i] == "Correcto":
        correctos = correctos + 1
    else:
        incorrectos = incorrectos + 1
    i = i + 1

print("La probabilidad de acertar " + str(correctos / len(resultados)))
valor_deportes_deportes = correctos / len(resultados)
vp_dep = resultados.count("Correcto")/len(resultados)
fp_dep = resultados.count("Incorrecto")/len(resultados)
print("La probabilidad no acertar " + str(incorrectos / len(resultados)))

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------


print("Para la lista que yo se que es de Salud: \n")


max_nacional = []
i = 0  # se va a mover sobre los titulos hasta el ultimo de ellos
contador = 0  # se va a mover sobre las palabras del titulo

while i < len(salud_test):
    frase = salud_test[i].split()  # Agarramos al titulo
    prob = prob_nacional
    contador = 0
    while contador < len(frase):
        if dic_nacional.get(frase[contador].lower()) is None:
            prob = laplace * prob  # cooreccion de laplace
        else:
            prob = float(dic_nacional.get(frase[contador].lower())) * prob
        contador = contador + 1
    max_nacional.append(prob)
    i = i + 1

max_destacada = []
i = 0  # se va a mover sobre los titulos hasta el ultimo de ellos
contador = 0  # se va a mover sobre las palabras del titulo
while i < len(salud_test):
    frase = salud_test[i].split()  # Agarramos al titulo
    prob = prob_destacada
    contador = 0
    while contador < len(frase):

        if dic_destacada.get(frase[contador].lower()) is None:
            prob = laplace * prob  # cooreccion de laplace
        else:
            prob = float(dic_destacada.get(frase[contador].lower())) * prob
        contador = contador + 1
    max_destacada.append(prob)
    i = i + 1

max_deportes = []
i = 0  # se va a mover sobre los titulos hasta el ultimo de ellos
contador = 0  # se va a mover sobre las palabras del titulo
while i < len(salud_test):
    frase = salud_test[i].split()  # Agarramos al titulo
    prob = prob_deportes
    contador = 0
    while contador < len(frase):
        if dic_deportes.get(frase[contador].lower()) is None:
            prob = laplace * prob  # cooreccion de laplace
        else:
            prob = float(dic_deportes.get(frase[contador].lower())) * prob
        contador = contador + 1
    max_deportes.append(prob)
    i = i + 1

max_salud = []
i = 0  # se va a mover sobre los titulos hasta el ultimo de ellos
contador = 0  # se va a mover sobre las palabras del titulo
while i < len(salud_test):
    frase = salud_test[i].split()  # Agarramos al titulo
    prob = prob_salud
    contador = 0

    while contador < len(frase):
        if dic_salud.get(frase[contador].lower()) is None:
            prob = laplace * prob  # cooreccion de laplace
        else:
            prob = float(dic_salud.get(frase[contador].lower())) * prob
        contador = contador + 1

    max_salud.append(prob)
    i = i + 1

print("Las maximas para la lista de Nacional estan completas \n")
print("Vamos a ver a cuantos no le acertamos")

i = 0
resultados = []
while i < len(max_nacional):
    if max_nacional[i] > max_destacada[i] and max_nacional[i] > max_deportes[i] and max_nacional[i] > max_salud[i]:
        resultados.append("Correcto")
    else:
        resultados.append("Incorrecto")
    i = i + 1

print("---------> 4)Los resultados tan esperados son:")
print("De longitud : " + str(len(resultados)))

print(resultados)

print("Vamos a ver cuan mal nos fue: ")
i = 0
correctos = 0
incorrectos = 0

while i < len(resultados):
    if resultados[i] == "Correcto":
        correctos = correctos + 1
    else:
        incorrectos = incorrectos + 1
    i = i + 1

print("La probabilidad de acertar " + str(correctos / len(resultados)))
valor_salud_salud = correctos / len(resultados)
vp_salud = resultados.count("Correcto")/len(resultados)
fp_salud = resultados.count("Incorrecto")/len(resultados)
print("La probabilidad de no acertar " + str(incorrectos / len(resultados)))

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------

# Analisis de la metricas


# Verdadero positivo
# Verdadero negativo
# falso positivo
# falso negativo


valores_centrales = [valor_nacional_nacional,valor_destacado_destacado,valor_deportes_deportes,valor_salud_salud]

matrix = [[valor_nacional_nacional,0,0,0],[0,valor_destacado_destacado,0,0],[0,0,valor_deportes_deportes],[0,0,0,valor_salud_salud]]
print(matrix)


vp = vp_nac+vp_dest+vp_dep+vp_salud
print("\nVerdaderos postitivos: " + str(vp))

fp = fp_nac+fp_dest+fp_dep+fp_salud
print("\nFalsos postitivos: "+str(fp))

#------------------------------------------------------------------------------------->

print("Para la lista que yo se que es nacional: \n")

laplace = 1/(8+palabras_totales)

max_nacional = []
i = 0  # se va a mover sobre los titulos hasta el ultimo de ellos
contador = 0  # se va a mover sobre las palabras del titulo

while i < len(nacional_test):
    frase = nacional_test[i].split()  # Agarramos al titulo
    prob = prob_nacional
    contador = 0
    while contador < len(frase):

        if dic_nacional.get(frase[contador].lower()) is None:
            prob = laplace * prob  # cooreccion de laplace
        else:
            prob = float(dic_nacional.get(frase[contador].lower())) * prob
        contador = contador + 1
    max_nacional.append(prob)
    i = i + 1

max_destacada = []
i = 0  # se va a mover sobre los titulos hasta el ultimo de ellos
contador = 0  # se va a mover sobre las palabras del titulo
while i < len(nacional_test):
    frase = nacional_test[i].split()  # Agarramos al titulo
    prob = prob_destacada
    contador = 0
    while contador < len(frase):
        if dic_destacada.get(frase[contador].lower()) is None:
            prob = laplace * prob  # cooreccion de laplace
        else:
            prob = float(dic_destacada.get(frase[contador].lower())) * prob
        contador = contador + 1
    max_destacada.append(prob)
    i = i + 1

max_deportes = []
i = 0  # se va a mover sobre los titulos hasta el ultimo de ellos
contador = 0  # se va a mover sobre las palabras del titulo
while i < len(nacional_test):
    frase = nacional_test[i].split()  # Agarramos al titulo
    prob = prob_deportes
    contador = 0
    while contador < len(frase):

        if dic_deportes.get(frase[contador].lower()) is None:
            prob = laplace * prob  # cooreccion de laplace
        else:
            prob = float(dic_deportes.get(frase[contador].lower())) * prob
        contador = contador + 1

    max_deportes.append(prob)
    i = i + 1

max_salud = []
i = 0  # se va a mover sobre los titulos hasta el ultimo de ellos
contador = 0  # se va a mover sobre las palabras del titulo
while i < len(nacional_test):
    frase = nacional_test[i].split()  # Agarramos al titulo
    prob = prob_salud
    contador = 0
    while contador < len(frase):

        if dic_salud.get(frase[contador].lower()) is None:
            prob = laplace * prob  # cooreccion de laplace
        else:
            prob = float(dic_salud.get(frase[contador].lower())) * prob
        contador = contador + 1

    max_salud.append(prob)
    i = i + 1

print("Las maximas para la lista de Nacional estan completas \n")
print("Vamos a ver a cuantos no le acertamos")

i = 0
resultados = []
while i < len(max_nacional):
    if max_nacional[i] > max_destacada[i] and max_nacional[i] > max_deportes[i] and max_nacional[i] > max_salud[i]:
        resultados.append("Correcto")
    else:
        resultados.append("Incorrecto")
    i = i + 1

print("Los resultados tan esperados son:")
print("La longitud es: " + str(len(resultados)))

print(resultados)

print("Vamos a ver cuan mal nos fue: ")
i = 0
correctos = 0
incorrectos = 0

while i < len(resultados):
    if resultados[i] == "Correcto":
        correctos = correctos + 1
    else:
        incorrectos = incorrectos + 1
    i = i + 1

print("La probabilidad de acertar " + str(correctos / len(resultados)))
valor_nacional_nacional = correctos / len(resultados)
vp_nac = resultados.count("Correcto")/len(resultados)
fp_nac = resultados.count("Incorrecto")/len(resultados)
print("La probabilidad de no acertar " + str(incorrectos / len(resultados)))