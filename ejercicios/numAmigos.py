"""solicite al usuario dos números enteros positivos y luego verifique si son números amigos o no. """
def verificarNumerosAmigos():
    numero1= int(input("Ingrese un número entero positivo: "))
    numero2= int(input("Ingrese otro número entero positivo: "))
    divisores1 = []
    divisores2 = []
    if numero1 <=0 or numero2 <=0: #si los números ingresados no son positivos entonces no son números amigos
        print("Los números ingresados no son positivos.")
    else: 
        for i in range(1, numero1): #recorrer los números desde 1 hasta el número ingresado
            if numero1 % i == 0: #si el numero es divisible por i entonces lo agrego a la lista de divisores
                divisores1.append(i)
        for i in range(1, numero2): #lo mismo para el segundo número
            if numero2 % i == 0:
                divisores2.append(i)
        #si la suma de los divisores de un número es igual al otro número y viceversa entonces son números amigos
        if sum(divisores1) == numero2 and sum(divisores2) == numero1:
            print(f"Los números {numero1} y {numero2} son números amigos.")
        else:
            print(f"Los números {numero1} y {numero2} no son números amigos.")
verificarNumerosAmigos()