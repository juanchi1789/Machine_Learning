import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-pastel')

# Cargamos los datos
df =pd.read_csv(r'/Users/juanmedina1810/PycharmProjects/Machine_Learning/TP4/TP/acath.csv')
print(df)

y = df['sigdz']
pos = 0
for i in range(len(y)):
    if y[i] == 1:
        pos = pos + 1

print("De las",len(y),"muestras tenemos:",pos,"Como positivas y",len(y)-pos,"Como negativas")
print("En % se ve como:: pos:",round((pos/len(y))*100,4),"%")
choleste1 = df['choleste']
choleste2 = df['choleste'].interpolate()
choleste3 = df['choleste'].interpolate(method = 'pchip')# Voy a usar este metodo para reemplazar los valores perdidos del Dataframe
choleste4 = df['choleste'].interpolate(method = 'akima')
choleste5 = df['choleste'].fillna(np.mean(df['choleste']))


plt.hist([choleste2,choleste3,choleste4,choleste5],label=['interpolate linear','Iterpolado pchip','interpolado akima','Fill con rMedia'])
plt.grid(True)
plt.xlim([0,600])
plt.legend()
plt.show()
