import numpy as np
from sklearn import svm
import matplotlib.pyplot as plt
from matplotlib import image
from matplotlib import pyplot
import random


# load image as pixel array
cielo = image.imread('cielo.jpeg')
pasto = image.imread('pasto.jpeg')
vaca = image.imread('vaca.jpeg')

# summarize shape of the pixel array
# print(image.dtype)
# print(image.shape)
# display the array of pixels as an image
# pyplot.imshow(image)
# pyplot.show()

print("Las imagenes tienen la sieguiete forma:")
print("El cielo: ", cielo.shape[0], "x", cielo.shape[1], "La cantidad de pixels es: ", cielo.shape[0] * cielo.shape[1])
print("El pasto: ", pasto.shape[0], "x", pasto.shape[1], "La cantidad de pixels es: ", pasto.shape[0] * pasto.shape[1])
print("La vaca: ", vaca.shape[0], "x", vaca.shape[1], "La cantidad de pixels es: ", vaca.shape[0] * vaca.shape[1])

# 0 = cielo, 1 = pasto, 2 = vaca

pyplot.imshow(cielo)
plt.show()

# <------------------------------------------------------------> Clase 0: Cielo
indices = []
for i in range(cielo.shape[0]):
    n = random.sample(range(cielo.shape[1]), 172)
    indices.append(n)
indices = np.sort(np.array(indices))

samples = []
for row in range(len(indices)):# recorre las filas
    for col in range(len(indices[row])): # recorre las columnas
        samples.append(cielo[row][col])
samples_cielo = np.array(samples)

clase_cielo = np.full(len(samples),0)
# <------------------------------------------------------------>
# <------------------------------------------------------------> Clase 1: Pasto
indices = []
for i in range(cielo.shape[0]):
    n = random.sample(range(pasto.shape[1]), 172)
    indices.append(n)
indices = np.sort(np.array(indices))

samples = []
for row in range(len(indices)):# recorre las filas
    for col in range(len(indices[row])): # recorre las columnas
        samples.append(cielo[row][col])
samples_pasto = np.array(samples)

clase_pasto = np.full(len(samples),0)
# <------------------------------------------------------------>
# <------------------------------------------------------------> Clase 2: Vaca
indices = []
for i in range(cielo.shape[0]):
    n = random.sample(range(vaca.shape[1]), 172)
    indices.append(n)
indices = np.sort(np.array(indices))

samples = []
for row in range(len(indices)):# recorre las filas
    for col in range(len(indices[row])): # recorre las columnas
        samples.append(cielo[row][col])
samples_vaca = np.array(samples)

clase_vaca = np.full(len(samples),0)
# <------------------------------------------------------------>

datos = np.array([samples_cielo,samples_vaca,samples_pasto])
clase = np.array([clase_cielo,clase_pasto,clase_vaca])

# <------------------------------------------------------------>

# hasta aca tengo las muestras que le tengro que pasar al SVM
# Entonces le paso la info al SVM

#clf = svm.SVC(kernel='linear', C=1000)
#clf.fit(datos, clase[0])


