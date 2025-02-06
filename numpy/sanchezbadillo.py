#Instituto Tecnologico de Pachuca
#Sanchez Badillo Adrian
#Maggi Natale Carlos Eduardo

#Matriz 5x4 usando numpy y calculando promedios de filas, columnas y general con data science
#importamos numpy
import numpy as np

#Matriz a usar
matriz = (
    [1.2, 3.4, 5.6, 7],
    [9.0, 1.1, 2.2, 3.3],
    [4.4, 5.5, 6.6, 7.7],
    [8.8, 9.9, 0.1, 1.2],
    [2.3, 3.4, 4.5, 5.6]
)

#Revisamos que si sea de 5x4
print("la forma de la matriz es de: ", np.shape(matriz))


#Promedio de cada fila
for i in range (0,5):
    print("Promedio de la fila", i+1, ":", np.average(matriz[i]))

#Promedio de las columnas
promedioColumnas=np.average(matriz, axis=0)
for i in range (0,4):
    print("Promedio de la columna", i+1, ":", promedioColumnas[i])

#Promedio general con solo 2 decimales
print("Promedio de toda la matriz:", np.average(matriz).round(2))