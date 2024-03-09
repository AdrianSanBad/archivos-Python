#subiras a la montaña rusa? tienes la altura y los creditos necesarios?
heigth=int(input("altura en Cm?: ")) #solicita la altura en cm
credits=int(input("Creditos restantes?: ")) #solicita los creditos
if heigth >=137 and credits >=10: #si altura y creditos son suficientes
  print("disfruta el viaje")        #subiras a la montaña rusa
elif heigth <137 and credits >=10:#si no tienes la altura pero si los creditos
  print("No eres lo suficientemente alto para subir")
elif heigth >=137 and credits <10:#si tienes la altura pero no los creditos
  print("No tienes creditos suficientes")
else:                             #si no cumples ningun requerimiento
  print("No cumples ambos requerimentos")
