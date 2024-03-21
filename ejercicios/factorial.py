#programa que calcula el factorial de un numero ingresado por el usuario
def factorial():
        n =int(input("Ingrese un numero entero positivo: ")) #se pide un numero entero positivo
        while n < 0: #en caso de que el numero sea negativo
            n =int(input("Por favor, ingrese un número entero positivo: "))
        factorial = 1 #en caso de que el numero sea 0 o 1
        for i in range(1, n+1): #se calcula el factorial
            factorial *= i 
        print(f"El factorial de {n} es: {factorial}")
        
factorial()