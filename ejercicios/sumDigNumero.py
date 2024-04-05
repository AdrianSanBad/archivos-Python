#Suma los digitos de un numero ingresado
def sumDigNumeros():
    numero=input("Ingrese un numero: ")
    lista=[]
    for i in numero:
        i=int(i)
        lista.append(i)
    print(sum(lista))
sumDigNumeros()