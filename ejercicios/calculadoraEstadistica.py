"""solicite al usuario una lista de números separados por comas y luego calcule y muestre las siguientes estadísticas 
básicas de los números"""
mum = input("Ingrese una lista de números separados por comas: ")
numeros = mum.split(",")
numeros = [int(i) for i in numeros]
print(f"Lista de números: {numeros}")
print(f"Número de elementos: {len(numeros)}")
print(f"Suma: {sum(numeros)}")
print(f"Promedio: {sum(numeros)/len(numeros)}")
print(f"Máximo: {max(numeros)}")
print(f"Mínimo: {min(numeros)}")

