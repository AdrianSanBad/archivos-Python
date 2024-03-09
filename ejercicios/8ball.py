    #bola 8 programada en python
import random
num=random.randint(1,8) #numero entre 1-8 que definira tu destino
quest=input("Ingresa pregunta: ") #solicita la pregunta
if num== 8:  #si el numero es 8
  print("yes-Definitely")
elif num==7: #si el numero es 7
  print("it is decidedly so")
elif num==6: #si el numero es 6
  print("Without a doubt.") 
elif num==5: #si el numero es 5
  print("Reply hazy, try again.")
elif num==4: #si el numero es 4
  print("Better not tell you now.") 
elif num==3: #si el numero es 3
  print("my sources say no")
elif num==2: #si el numero es 2
  print("Outlook not so good.") 
else:        #si el numero es 1
  print("Very doubtful")
