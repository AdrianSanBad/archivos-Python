import random

def adivinaNum():
    print("Tienes que adivinar un numero que pense entre 1 y 100")
    num=random.randint(1,100)
    intentos=0
    while True:
        intentos+=1
        numIngresado=int(input("Ingresa que numero crees que sea entre el 1 y 100 en forma de numero no palabras: "))
        if numIngresado<num:
            print("El numero que ingresaste es menor al numero que pense")
        elif numIngresado>num:
            print("El numero que ingresaste es mayor al numero que pense")
        else:
            print(f"Lo lograste, el numero era {num} y lo adivinaste a los {intentos} intentos")
            respuesta=input("Quieres volver a jugar? Si/No:")
            if respuesta=="Si":
                adivinaNum()
            else:
                break
adivinaNum()