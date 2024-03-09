#Estas list@ para saber a que casa de Hogwarts perteneces?
gry,raven, huff, sly=0,0,0,0 #variables para cada casa inicializadas en 0
q1=int(input("Q1) Do you like Dawn(1) or Dusk(2) ")) #pregunta 1
if q1==1: #si la respuesta es 1
  #sumar 1 a gryffindor y ravenclaw
  gry+=1
  raven+=1
elif q1==2:#si la respuesta es 2
  #sumar 1 a hufflepuff y slytherin
  huff+=1
  sly+=1
else: #si la respuesta no es 1 ni 2
  print("Ingresaste un dato incorrecto por favor reinicia")

print("Q2) When I’m dead, I want people to remember me as") #pregunta 2
print("1) The Good, 2) The Great, 3) The Wise, 4) The Bold")
q2=int(input("")) 
if q2==1: #si la respuesta es 1
  #sumar 2 a hufflepuff
  huff=huff+2
elif q2==2: #si la respuesta es 2
  #sumar 2 a slytherin
  sly=sly+2
elif q2==3: #si la respuesta es 3
  #sumar 2 a ravenclaw
  raven=raven+2
elif q2==4: #si la respuesta es 4
  #sumar 2 a gryffindor
  gry=gry+2
else:
  print("Ingresaste un dato incorrecto por favor reinicia")

print("Q3) Which kind of instrument most pleases your ear?")  #pregunta 3
print("   1) The violin, 2) The trumpet, 3) The piano, 4) The drum")
q3=int(input(""))
if q3==2: #si la respuesta es 2
  #sumar 4 a hufflepuff
  huff=huff+4
elif q3==1: #si la respuesta es 1
  #sumar 4 a slytherin
  sly=sly+4
elif q3==3: #si la respuesta es 3
  #sumar 4 a ravenclaw
  raven=raven+4
elif q3==4: #si la respuesta es 4
  #sumar 4 a gryffindor
  gry=gry+4
else:
  print("Ingresaste un dato incorrecto por favor reinicia")
if gry> raven and gry > huff and gry >sly: #si gryffindor tiene mas puntos
  print(f"gano gryffindor con {gry} puntos")
elif raven> gry and raven > huff and raven >sly: #si ravenclaw tiene mas puntos
  print(f"gano ravenclaw con {raven} puntos")
elif huff> raven and huff > gry and huff >sly: #si hufflepuff tiene mas puntos
  print(f"gano hufflepuff con {huff} puntos")
elif sly> raven and sly > huff and sly >gry: #si slytherin tiene mas puntos
  print(f"gano Slytherin con {sly} puntos")
else: #si hay un empate
  print("Ingresaste datos incorrectamente, intenta de nuevo")
