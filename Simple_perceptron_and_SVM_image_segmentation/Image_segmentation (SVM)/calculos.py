import numpy as np
from sklearn import svm
import matplotlib.pyplot as plt
from PIL import Image
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import seaborn as sns



def image_to_np_array(filename):
    img = Image.open(filename)
    return np.array(img)

def accuracy(y_true, y_predicted):
    accuracy = accuracy_score(y_true, y_predicted)
    return accuracy

# <-----------------------------------------------------------------------------> Conjuntos de datos
# abrir las imagenes

cielo = image_to_np_array('cielo.jpeg')
pasto = image_to_np_array('pasto.jpeg')
vaca = image_to_np_array('vaca.jpeg')

cantidad_cielo = cielo.shape[0] * cielo.shape[1]
cantidad_pasto = pasto.shape[0] * pasto.shape[1]
cantidad_vaca = vaca.shape[0] * vaca.shape[1]

cielito = cielo.reshape(cielo.shape[0] * cielo.shape[1], 3)
pastito = pasto.reshape(pasto.shape[0] * pasto.shape[1], 3)
vaquita = vaca.reshape(vaca.shape[0] * vaca.shape[1], 3)

clase_cielo = np.zeros((cielo.shape[0] * cielo.shape[1], 1))
clase_pasto = np.ones((pasto.shape[0] * pasto.shape[1], 1))
clase_vaca = np.full((vaca.shape[0] * vaca.shape[1], 1), 2)


# <-----------------------------------------------------------------------------> Dividimos en testeo y entrenamiento

X = np.concatenate((cielito, pastito, vaquita), axis=0)
y = np.concatenate((clase_cielo, clase_pasto, clase_vaca), axis=0)

X_train, X_test, y_train, y_test = train_test_split(X, y,random_state=123)# (*)

# <-----------------------------------------------------------------------------> SMV (Estan comentados los Nucleos que use)

#SVM = svm.SVC(kernel='sigmoid',C=100)# (*)  # kernels : rbf, poly (degree), linear, sigmoid
SVM = svm.SVC(kernel='rbf', C = 500)
#SVM = svm.SVC(kernel='linear', C=100,max_iter=10000)
#SVM = svm.SVC(kernel='poly',degree=3,C=1000)

SVM.fit(X_train, y_train)
y_predicted = SVM.predict(X_test)

# <-----------------------------------------------------------------------------> METRICAS

matrix = confusion_matrix(y_test, y_predicted)
print("accuracy: ", accuracy(y_test, y_predicted))
ax = sns.heatmap(matrix, annot=True, fmt="d")
plt.title("Matriz de confusion")
plt.xlabel("Real")
plt.ylabel("Predicted")
plt.show()
print("Metricas")
print(classification_report(y_test, y_predicted))

print("Lo testeamos con otras imagenes!!")


cow = image_to_np_array('cow.jpeg')
cowi = cow.reshape(cow.shape[0] * cow.shape[1], 3)  # para testear
y_predicted_cowi = SVM.predict(cowi)

for i in range(len(y_predicted_cowi)):

    if y_predicted_cowi[i] == 0:  # El cielo es AZUL
        cowi[i][0] = 0
        cowi[i][1] = 0
        cowi[i][2] = 255

    if y_predicted_cowi[i] == 1:  # El pasto es verde
        cowi[i][0] = 0
        cowi[i][1] = 255
        cowi[i][2] = 0

    if y_predicted_cowi[i] == 2:  # La vaca es roja
        cowi[i][0] = 255
        cowi[i][1] = 0
        cowi[i][2] = 0

cowi = cowi.reshape(cow.shape)
plt.imshow(cowi)
plt.title("Imagen 1")
plt.show()

# <--------------------------------------------> COW 2

cow = image_to_np_array('cow_test.jpeg')
cowi = cow.reshape(cow.shape[0] * cow.shape[1], 3)  # para testear
y_predicted_cowi = SVM.predict(cowi)

for i in range(len(y_predicted_cowi)):
    if y_predicted_cowi[i] == 0:  # El cielo es AZUL
        cowi[i][0] = 0
        cowi[i][1] = 0
        cowi[i][2] = 255

    if y_predicted_cowi[i] == 1:  # El pasto es verde
        cowi[i][0] = 0
        cowi[i][1] = 255
        cowi[i][2] = 0

    if y_predicted_cowi[i] == 2:  # La vaca es roja
        cowi[i][0] = 255
        cowi[i][1] = 0
        cowi[i][2] = 0

cowi = cowi.reshape(cow.shape)
plt.imshow(cowi)
plt.title("Imagen 2")
plt.show()

# <--------------------------------------------> COW 3

cow = image_to_np_array('cow_test_2.jpeg')
cowi = cow.reshape(cow.shape[0] * cow.shape[1], 3)  # para testear
y_predicted_cowi = SVM.predict(cowi)

for i in range(len(y_predicted_cowi)):
    if y_predicted_cowi[i] == 0:  # El cielo es AZUL
        cowi[i][0] = 0
        cowi[i][1] = 0
        cowi[i][2] = 255

    if y_predicted_cowi[i] == 1:  # El pasto es verde
        cowi[i][0] = 0
        cowi[i][1] = 255
        cowi[i][2] = 0

    if y_predicted_cowi[i] == 2:  # La vaca es roja
        cowi[i][0] = 255
        cowi[i][1] = 0
        cowi[i][2] = 0

cowi = cowi.reshape(cow.shape)
plt.imshow(cowi)
plt.title("Imagen 3")
plt.show()