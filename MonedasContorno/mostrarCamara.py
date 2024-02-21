import cv2 
capVid=cv2.VideoCapture(1) #1 para camaras externas, 0 para internas
if not capVid.isOpened():
    print("no encontro camara")
    exit()
while True:
    _,frame=capVid.read()  #devuelve dos valores, tipo de camara y el video capturado
    cv2.imshow("En vivo",frame)
    if cv2.waitKey(1)==ord("q"):
        break
capVid.release()
cv2.destroyAllWindows()