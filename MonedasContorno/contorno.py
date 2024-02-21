#Este codigo nos enseña a usar los conceptos basicos de cv2
import cv2
imagen = cv2.imread('contorno.jpg') #Esta es la variable que contendra la imagen a usar , se recomienda usar el directorio raiz completo
grises=cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY) #convertir la imagen a escala de grises
_,umbral=cv2.threshold(grises,100,255,cv2.THRESH_BINARY) # convertir la imagen a grises a escala de umbrales
contornos, jerarquia= cv2.findContours(umbral,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE) #detectar los contornos de la imagen a umbrales
cv2.drawContours(imagen,contornos,-1,(210,10,5),3) #dibujar los contornos detectados a la imagen original
# Mostrar
cv2.imshow('imagen original',imagen) #muestra la imagen original con los contornos aplicados
#cv2.imshow('imagen a grises',grises) #muestra la imagen a escala de grises
cv2.imshow('imagen umbral',umbral) #muestra la imagen con umbrales a binarios
cv2.waitKey(0)
cv2.destroyAllWindows()
