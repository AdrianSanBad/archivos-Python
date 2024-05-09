#en este codigo aprendimos a usar List Comprehensions o comprensiones de listas en python
numbers = [57, 10, 82, 36, 89, 46, 13, 23, 92, 48]
divisibles2= [num for num in numbers if num%2==0 ]
print(f"los numeros originales: {numbers}")
print(f"los numeros divisibles son: {divisibles2}")
impares= [num for num in numbers if num%2==1]
print(f"los numeros impares son: {impares}")