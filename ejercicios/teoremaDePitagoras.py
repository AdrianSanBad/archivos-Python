 #programa que calcula la hipotenusa de un triangulo rectangulo
import math
a=int(input("Lado a: ")) #solicita el valor del lado a del triangulo
b=int(input("Lado b: ")) #solicita el valor del lado b del triangulo
c=math.sqrt(a**2+b**2) #formula para calcular la hipotenusa de un triangulo rectangulo
print(f"Lado c(hipotenusa) es igual a {c}") #imprime el valor de la hipotenusa