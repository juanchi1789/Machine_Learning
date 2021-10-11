# <-----------------------------------------------------------------------------> Fotos para probar el modelo
# <--------------------------------------------> COW 1

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