import cv2  #importar cv2
import numpy  #importar libreria para trabajar con arrays
vGauss=5
vKernel=5
original=cv2.imread('monedas.jpg')
mMx=cv2.imread('monedaMx.png')     #Cambiar original a mMx si deseas intentarlo con monedas mx
gris=cv2.cvtColor(original,cv2.COLOR_BGR2GRAY)
desenfoque=cv2.GaussianBlur(gris,(vGauss,vKernel),0)
canny=cv2.Canny(desenfoque,60,100)


kernel=numpy.ones((vKernel,vKernel),numpy.uint8)      #definicion de kernel a 8 bits
cierre=cv2.morphologyEx(canny,cv2.MORPH_CLOSE,kernel)     
contornos,jerarquia=cv2.findContours(cierre.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)     #Definicion de contornos
print("Numero de monedas encontradas: {}" .format(len(contornos))) #Contar cuantas monedas hay a traves de len
cv2.drawContours(original,contornos,-1, (255,0,0),2)  #Dibujar bordes 

#mostrar resultados
cv2.imshow("Grises", gris)     #imagen transformada a escala grises
cv2.imshow("Desenfocado", desenfoque)  #imagen con desenfoque Gaussian
cv2.imshow("Canny", canny)             #deteccion de bordes
cv2.imshow("Cierre",cierre)            #eliminacion de ruido interno(bordes no deseados)
cv2.imshow("ResultadoF",original)     #imagen original con bordes dibujados
cv2.waitKey(0)