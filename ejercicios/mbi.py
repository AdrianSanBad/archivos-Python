#Programa que calcula el indice de masa corporal solicitando el peso en kilogramos y la altura en metros
def mbi():
    mass=int(input("peso en kilogramos: ")) #input solicita el peso en kilogramos
    heigth=float(input("Altura en metros: ")) #input solicita la altura en metros
    indice=(mass)/(heigth**2) #formula para calcular el indice de masa corporal
    print(f"{indice} es tu indice de masa corporal") 
    #Se determina el estado de la persona segun el indice de masa corporal
    if indice<18.5:
        print("Bajo peso")
    elif indice>=18.5 and indice<24.9:
        print("Peso normal")
    elif indice>=25 and indice<29.9:
        print("Sobrepeso")
    elif indice>=30 and indice<34.9:
        print("Obesidad tipo I")
    elif indice>=35 and indice<39.9:
        print("Obesidad tipo II")
    else:
        print("Obesidad tipo III (mórbida)")
mbi()
