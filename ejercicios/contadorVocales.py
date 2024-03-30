"""solicite al usuario una frase o un párrafo y luego cuente el número de vocales (mayúsculas y minúsculas) 
en esa entrada. Las vocales son las letras 'a', 'e', 'i', 'o', 'u' (tanto en minúsculas como en mayúsculas)."""

frase = input("Ingrese una frase o párrafo: ")
vocales = "aeiouAEIOU"  
contador = 0
for letra in frase:
    if letra in vocales:
        contador += 1
print(f"El número de vocales en la frase o párrafo es: {contador}")