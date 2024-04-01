""" solicite al usuario un número entero positivo y luego verifique si ese número es primo o no. 
Un número primo es aquel que solo es divisible por 1 y por sí mismo."""
def numPrimo():
    num=int(input("Ingrese un número entero positivo: "))
    if num<=1:
        print("El número no es primo")
    elif num==2:
        print("El número es primo")
    else:
        esPrimo=True
        for i in range(2,num):
            if num%i==0:
                esPrimo=False
                break  
        if esPrimo:
            print("El número es primo")
        else:
            print("El número no es primo")
                   
numPrimo()