# Funciones del Ej 2: Noticias argentinas

# Funciones para la etapa de Inicial y la de filtrado

clases = ["Nacional", "Entretenimiento", "Deportes", "Salud"]

palabras_spam = ['trabajadores',"el", "la", "los", "y", "de", "ellos", "que", "qué", "del", "pero", "ademas", "sin", "con", "la",
                 "que", "se"
    , "su", "lo", "las", "me", "son", "pero", "porque", "|", "cómo", "no", "en", "para", "es", "[video]", "...",
                 "después",
                 'de', 'por',"al","un","a"]


def words_split(lista):
    palabras = []
    i = 0
    while i < len(lista):
        palabras = palabras + lista[i].split()
        i = i + 1
    return palabras

def lower_converter(lista):
    i = 0
    while i < len(lista):
        lista[i] = lista[i].lower()
        i = i + 1
    return lista

def filter(list):
    i = 0
    while i < len(list):
        list[i] = list[i].replace(",", "")  # Limpio los datos, ya que pueden generar conflictos
        list[i] = list[i].replace(":", "")
        list[i] = list[i].replace("+", "")
        list[i] = list[i].replace("?", "")
        list[i] = list[i].replace("¿", "")
        list[i] = list[i].replace("'", "")
        list[i] = list[i].replace('"', "")
        list[i] = list[i].replace('!', "")
        list[i] = list[i].replace('¡', "")
        list[i] = list[i].replace(',', "")
        list[i] = list[i].replace('¡', "")
        list[i] = list[i].replace(':', "")
        list[i] = list[i].replace('%', "")
        list[i] = list[i].replace('\x9d', "")
        i = i + 1
    return list

def filtrado(lista):  # es aplicar la funcion filter
    palabras = filter(lower_converter(words_split(lista)))
    return palabras

def filtrado_test(lista):  # es aplicar la funcion filter
    palabras = filter(lower_converter(lista))
    return palabras

def filtrado_dic(dic):
    i = 0
    while i < len(clases):
        print(clases[i] + " ---> Empieza a ser filtrada")
        dic[clases[i]] = filtrado(dic.get(clases[i]))
        print(clases[i] + " ---> Filtrada")
        i = i + 1
    return dic

def mostrar_cantidad_de_titulos(dic_in):
    i = 0
    while i < len(clases):
        print(clases[i] + ": " + str(len(dic_in.get(clases[i]))))
        i = i + 1

def mostrar_cantidad_de_palabras(dic_in):
    i = 0
    while i < len(clases):
        print(clases[i] + ": " + str(len(dic_in.get(clases[i]))))
        i = i + 1

def entrenador(dic): # el diccionario va a ser el que tiene {"Clase":[Lista de palabras de la clase]}
    clases = ["Nacional", "Entretenimiento", "Deportes", "Salud"]
    total = len(dic[clases[0]]) + len(dic[clases[1]]) + len(dic[clases[2]]) + len(dic[clases[3]]) # palabras totales
    dic_out = {}
    contador = 0
    while contador < len(clases):  # vamos cargando clase a clase
        i = 0
        dic_de_palabras = {}

        while i < len(dic[clases[contador]]):
            if not (dic[clases[contador]][i] in dic_de_palabras.keys()):

                veces_totales_palabra = dic[clases[0]].count(dic[clases[contador]][i])+dic[clases[1]].count(dic[clases[contador]][i])+\
                                        dic[clases[2]].count(dic[clases[contador]][i])+dic[clases[3]].count(dic[clases[contador]][i])

                dic_de_palabras.update({dic[clases[contador]][i]: (
                    ((1+(dic[clases[contador]].count(dic[clases[contador]][i]))) / (1*4+(total)))*(total/veces_totales_palabra))})# el 1 es el coef de smothing

                # Esto es: Las veces que una palabra aparece en una clase dividido la cantidad de palabras en esa
                # clase.
                #  en esa clase dividido la cantidad de total de palabras (la suma de la cantidad de palabras en cada
                #  clase).

            i = i + 1
        dic_out.update({clases[contador]: dic_de_palabras})
        contador = contador + 1
    return dic_out

def mostrar_cantidad_de_palabras_entrenadas(dic):
    i = 0
    while i < dic.keys().__len__():
        print(clases[i] + ": " + str(dic[clases[i]].__len__()))
        i = i + 1

def limpiador(dic):
    contador = 0
    while contador < len(clases):
        i = 0
        while i < len(palabras_spam):

            if palabras_spam[i] in (dic[clases[contador]]):

                dic[clases[contador]].pop(palabras_spam[i])

            i = i + 1

        contador = contador + 1

def limpiador_test(list):
    i = 0
    while i < len(palabras_spam):
        contador = 0
        while contador < len(list):
            if palabras_spam[i] in list:
                list.remove(palabras_spam[i])
            contador = contador + 1
        i = i + 1

def probabilidades_roc(dic):
    clases = ["Nacional", "Entretenimiento", "Deportes", "Salud"]
    total = len(dic[clases[0]]) + len(dic[clases[1]]) + len(dic[clases[2]]) + len(dic[clases[3]]) # cantidad de palabras totales
    dic_out = {}
    contador = 0
    while contador < len(clases):  # vamos cargando clase a clase
        i = 0
        dic_de_palabras = {}
        while i < len(dic[clases[contador]]):
            if not (dic[clases[contador]][i] in dic_de_palabras.keys()):
                total_palabra =(dic[clases[0]].count(dic[clases[contador]][i]))+(dic[clases[1]].count(dic[clases[contador]][i]))+\
                               (dic[clases[2]].count(dic[clases[contador]][i]))+(dic[clases[3]].count(dic[clases[contador]][i]))

                dic_de_palabras.update({dic[clases[contador]][i]: (
                    (((dic[clases[contador]].count(dic[clases[contador]][i]))*total) /(total_palabra*(len(dic[clases[contador]])))))})

                # Esto es: Las veces que una palabra aparece en una clase dividido la cantidad de palabras en esa
                # clase, Lodo esto por la probabilidad de cada clase. que esta definida como la cantidad de palabras
                #  en esa clase dividido la cantidad de total de palabras (la suma de la cantidad de palabras en cada
                #  clase).
                # print("Las probabilidades de la clase: "+ clases[contador] +" son: " + str((len(dic[clases[0]]))/total))

            i = i + 1
        dic_out.update({clases[contador]: dic_de_palabras})
        contador = contador + 1
    return dic_out

def divisor_de_listas(lista, divisor):
    i = 0
    while i < len(lista):
        lista[i] = lista[i] / divisor
        i = i + 1

    return lista