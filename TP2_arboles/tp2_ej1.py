# <-------------------------------------------------------------------------------------------------------------------->
# Ej 1: Desition Trees and Random Forest
import funciones
import random
import matplotlib.pyplot as plt
import pandas as pd  # solo para importar el archivo
import numpy as np
import math as mt

array = pd.read_csv("german_credit.csv", low_memory=False)

data = (array.values)  # lista que contiene la información de cada individuo en forma de lista, REGISTROS TOTALES

