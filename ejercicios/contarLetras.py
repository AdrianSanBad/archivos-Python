"""solicite al usuario una frase o un párrafo y luego cuente el número de veces que aparece cada letra en la entrada. 
El programa debe ignorar los espacios y considerar las letras mayúsculas y minúsculas como iguales. Luego, 
imprime el recuento de cada letra en orden alfabético."""
def contarLasLetras():
    letras={} #diccionario donde se guardaran las letras
    frase=input("ingresa la frase a contar: ")
    frase=frase.replace(" ","") #elimina los espacios
    frase=frase.lower() #convierte todo a minusculas
    for i in frase: #recorre la frase
        if i.isalpha(): #si es una letra
            if i in letras: #si ya esta en el diccionario
                letras[i]+=1 
            else: #si no esta en el diccionario
                letras[i]=1 
    for i in sorted(letras): #imprime las letras ordenadas
        print(i,letras[i])

contarLasLetras()