#Programa que simula el lanzar una moneda al aire de manera "aleatoria"
import random
num= random.randint(0,1) #genera un numero aleatorio entre 0 y 1 con la funcion randint de random
if num>0.5: #si el numero es mayor a 0.5 imprime cara
  print("Cara")
else: #si no imprime cruz
  print("Cruz")