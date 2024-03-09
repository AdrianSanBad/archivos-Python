#este programa determina si un ph es acido, basico o neutro

ph=int(input("ph value?:")) #solicita el valor del ph
if ph> 7:   #si el ph es mayor a 7 es basico
  print("ph Basic")
elif ph <7: #si el ph es menor a 7 es acido
  print("ph Acidic")
else:       #si no es ni mayor ni menor a 7 es neutro
  print("ph Neutral")