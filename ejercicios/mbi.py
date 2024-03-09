#Programa que calcula el indice de masa corporal solicitando el peso en kilogramos y la altura en metros
mass=int(input("peso en kilogramos: ")) #input solicita el peso en kilogramos
heigth=float(input("Altura en metros: ")) #input solicita la altura en metros
bmi=(mass)/(heigth**2) #formula para calcular el indice de masa corporal
print(f"{bmi} es tu indice de masa corporal") 