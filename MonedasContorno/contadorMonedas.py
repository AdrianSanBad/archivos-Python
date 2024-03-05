import cv2  #importar cv2
import numpy  #importar libreria para trabajar con arrays
vGauss=5 #definir variable para desenfoque gaussiano
vKernel=5 #definir variable para kernel
original=cv2.imread('MonedasContorno/monedaMX.png.jpg') #leer imagen
gris=cv2.cvtColor(original,cv2.COLOR_BGR2GRAY) #convertir imagen a escala de grises
desenfoque=cv2.GaussianBlur(gris,(vGauss,vKernel),0) #aplicar desenfoque gaussiano
canny=cv2.Canny(desenfoque,60,100) #deteccion de bordes


kernel=numpy.ones((vKernel,vKernel),numpy.uint8)      #definicion de kernel a 8 bits
cierre=cv2.morphologyEx(canny,cv2.MORPH_CLOSE,kernel) #eliminacion de ruido interno(bordes no deseados)
contornos,jerarquia=cv2.findContours(cierre.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) #encontrar contornos en la imagen cierre
print("Numero de monedas encontradas: {}" .format(len(contornos))) #imprimir numero de monedas encontradas
cv2.drawContours(original,contornos,-1, (255,0,0),2) #dibujar contornos en la imagen original

#mostrar resultados
cv2.imshow("Grises", gris)     #imagen transformada a escala grises
cv2.imshow("Desenfocado", desenfoque)  #imagen con desenfoque Gaussian
cv2.imshow("Canny", canny)             #deteccion de bordes
cv2.imshow("Cierre",cierre)            #eliminacion de ruido interno(bordes no deseados)
cv2.imshow("ResultadoF",original)     #imagen original con bordes dibujados
cv2.waitKey(0) #esperar a que se presione una tecla para cerrar las ventanas