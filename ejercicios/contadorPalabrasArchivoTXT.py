"""lea un archivo de texto dado por el usuario y cuente el número total de palabras en ese archivo. 
El programa debe ser capaz de manejar archivos de texto de cualquier tamaño y debe ignorar los espacios en blanco, 
signos de puntuación y caracteres especiales al contar las palabras."""
def contadorPalabrasArchivoTXT(ruta):
    try:
        with open(ruta, "r") as file:
            texto=file.read()
            palabras=texto.split()
            print(f"El numero de palabras en el texto es de: {len(palabras)}")
    except FileNotFoundError:
        print("El archivo no existe")

def main():
    ruta=input("Ingrese la ruta del archivo: ")
    contadorPalabrasArchivoTXT(ruta)
main()
#D:/ProyectosPython/ejercicios/texto.txt
#ruta de ejemplo archivo