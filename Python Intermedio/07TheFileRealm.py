#uso de diccionarios para escribir en un archivo de texto las canciones que me gustan
liked_songs={
  "From the start": "Laufey",
  "Feel it": "D4vd",
  "ARE WE STILL FRIENDS?": "Tyler, The Creator"
}
def write_liked_songs_to_file(liked_songs,file_name):
  documento=open(file_name,"w")
  documento.write("Canciones que me gustan: \n")
  for titulo,artista in liked_songs.items():
    documento.write(f"{titulo} by {artista} \n")

#write_liked_songs_to_file(liked_songs, "canciones.txt")

documento=open("canciones.txt","r")
print(documento.read())