#con este codigo se podra reconocer monedas en camara y contar su total
import cv2
import numpy
def ordenarPuntos(puntos):
    nPuntos=numpy.concatenate(puntos[0],puntos[1],puntos[2],puntos[3]).tolist() 
    y_order=sorted(nPuntos,key=lambda nPuntos:nPuntos[1])
    x1_order=y_order[0:2]
    x1_order=sorted(x1_order,key=lambda x1_order:x1_order[0])
    x2_order=y_order[2:4]