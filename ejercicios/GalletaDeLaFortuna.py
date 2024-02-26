# Write code below 💖
import random #Se importa random
def fortune():  #Definir funcion fortuna
  #Se crea lista con todas las opciones
  fortuneList=[
  "Don't pursue happiness – create it.",
  "All things are difficult before they are easy.",
  "The early bird gets the worm, but the second mouse gets the cheese.",
  "Someone in your life needs a letter from you.",
  "Don't just think. Act!",
  "Your heart will skip a beat.",
  "The fortune you search for is in another cookie.",
  "Help! I'm being held prisoner in a Chinese bakery!"]
  ran=random.randint(0,7)  #Genera numero entre 0 y 7
  #Se imprime mensaje dependiendo de numero generado
  if ran==0:
    print(fortuneList[0])
  elif ran==1:
    print(fortuneList[1])
  elif ran==2:
    print(fortuneList[2])
  elif ran==3:
    print(fortuneList[3])
  elif ran==4:
    print(fortuneList[4])
  elif ran==5:
    print(fortuneList[5])
  elif ran==6:
    print(fortuneList[6])
  else:
    print(fortuneList[7])
#Ejecutamos 3 veces
fortune()
fortune()
fortune()