#en este codigo aprendimos a usar List Comprehensions o comprensiones de listas en python
#creamos una lista de numeros
numbers = [57, 10, 82, 36, 89, 46, 13, 23, 92, 48]
#creamos una lista de numeros divisibles entre 2
divisibles2= [num for num in numbers if num%2==0 ]
#imprimimos los numeros originales y los divisibles entre 2
print(f"los numeros originales: {numbers}")
print(f"los numeros divisibles son: {divisibles2}")
#creamos una lista de numeros impares
impares= [num for num in numbers if num%2==1]
#imprimimos los numeros impares
print(f"los numeros impares son: {impares}")