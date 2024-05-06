#Uso de filter() reduce() y map()
from functools import reduce
# List of songs with their durations (in minutes) (datos a usar)
playlist = [('What Was I Made For?', 3.42), ('Just Like That', 5.05), ('Song 3', 6.8), ('Leave The Door Open', 4.02), ('I Can\'t Breath', 4.47), ('Bad Guy', 3.14)]
#First, use the filter() function to pick out the songs that are longer than 5 minutes (i.e., 5.00).
def filtroMayor5(x):
    return x[1] >= 5.00 #si la duracion de la cancion es mayor o igual a 5 minutos
mayor5 = list(filter(filtroMayor5, playlist))
print(mayor5)

#Next, use map() to convert all the durations of the songs in your playlist from minutes to seconds.
def minutosASec(x):
    return(x[0],x[1]*60) #x[0] es el nombre de la cancion, x[1] es la duracion en minutos
convertSec= list(map(minutosASec, playlist))
print(convertSec)

#Lastly, add up the total playtime of the playlist with reduce().
def totalPlaylistDuration(x,y): #x=acumulador, y=elemento
    return x+y[1]
total= reduce(totalPlaylistDuration, playlist, 0)
print(total) #26.9 minutos
