#programa que contara las palabras de un texto introducido por el usuario
def contarPalabras():
    texto = input("Introduce un texto: ") #se pide al usuario que introduzca un texto
    palabras = texto.split() #se separa el texto en palabras y se guardan en una lista
    for palabra in palabras: #se recorre la lista de palabras
        print(palabra) #se imprime cada palabra
    print(f"Hay en total {len(palabras)} Palabras en el texto.") #se imprime el total de palabras en el texto
contarPalabras()