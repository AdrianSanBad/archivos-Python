"""solicite al usuario un número entero positivo y luego verifique si ese número es un número perfecto o no."""
def verificarNumerosPerfectos():
    divisores = [] # Lista para almacenar los divisores propios del número ingresado
    numero = int(input("Ingrese un número entero positivo: "))
    if numero <= 0: # Verificar si el número ingresado es positivo ya que los números perfectos son positivos
        print("El número ingresado no es positivo.")
    else:
        for i in range(1, numero):  # Recorrer los números desde 1 hasta el número ingresado
            if numero % i == 0:  #si el numero es divisible por i entonces lo agrego a la lista de divisores
                divisores.append(i)  
        if sum(divisores) == numero: #si la suma de los divisores es igual al número ingresado entonces es un número perfecto
            print(f"El número {numero} es un número perfecto.")
        else:
            print(f"El número {numero} no es un número perfecto.")
verificarNumerosPerfectos()