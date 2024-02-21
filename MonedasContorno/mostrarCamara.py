#Este codigo nos enseña a usar cv2 para utilizar la camara de nuestra computadora
import cv2 
capVid=cv2.VideoCapture(1) #1 para camaras externas, 0 para internas
if not capVid.isOpened():     #si la camara a usar no se encuentra activa se cierra el ejecucion
    print("no encontro camara")
    exit()
while True:
    _,frame=capVid.read()  #devuelve dos valores, tipo de camara y el video capturado
    cv2.imshow("En vivo",frame)
    if cv2.waitKey(1)==ord("q"):  #Si se presiona la tecla q en ejecucion se termina el programa
        break
capVid.release()    #libera de uso la camara
cv2.destroyAllWindows()