"""solicite al usuario una frase o un párrafo y luego cuente el número de palabras únicas en esa entrada."""
def contar_palabras_unicas():
    frase = input("Ingrese una frase o párrafo a su gusto: ")
    palabras = frase.lower().split() # Convertir a minúsculas y dividir en palabras
    contador_palabras = {} # Diccionario para contar las palabras
    for palabra in palabras: # Contar las palabras
        if palabra in contador_palabras: # Si la palabra ya está en el diccionario, incrementar el contador
            contador_palabras[palabra] += 1 
        else:   # Si la palabra no está en el diccionario, agregarla con un contador de 1
            contador_palabras[palabra] = 1
    # Contar el número de palabras únicas mediante un for que recorre el diccionario y suma 1 por cada palabra que tenga un conteo de 1
    palabrasUnicas = sum(1 for palabra, conteo in contador_palabras.items() if conteo == 1) 
    print(f"El número de palabras únicas es: {palabrasUnicas}")

contar_palabras_unicas()
