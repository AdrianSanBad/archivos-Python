#recordamos que de un modulo se puede importar directamente una funcion o clase
#este programa calcula el area de un planeta aleatorio seleccionado con choice
from math import pi  #importamos la constante pi
from random import choice as ch #importamos la funcion choice de la libreria random
#definimos una lista de planetas
planets = [
  'Mercury',
  'Venus',
  'Earth',
  'Mars',
  'Saturn'
]
#seleccionamos un planeta aleatorio
random_planet=ch(planets)
#asignamos el radio del planeta seleccionado
if random_planet == 'Mercury':
    r = 2440
elif random_planet == 'Venus':
    r = 6052
elif random_planet == 'Earth':
    r = 6371
elif random_planet == 'Mars':
    r = 3390
elif random_planet == 'Saturn':
    r = 58232
else:
    print("Oops! An error occurred.")
#calculamos el area del planeta seleccionado
area=4*pi*r**2
#mostramos el planeta seleccionado y su area
print(f"Planet {random_planet} with area of {area}")