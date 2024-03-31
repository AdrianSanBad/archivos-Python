"""convierta una temperatura en grados Celsius a grados Fahrenheit o viceversa, según la elección del usuario. 
El programa debe solicitar al usuario que ingrese la temperatura y luego preguntar si desea convertirla a Celsius o Fahrenheit."""
def convertirTemp():
    print("Desea convertir la temperatura a Celsius o Fahrenheit?")
    seleccion=input("Ingrese C para Celsius o F para Fahrenheit: ")
    temp=float(input("Ingrese la temperatura: "))
    if seleccion.upper()=="C":
        resultado=(temp-32)*(5/9)
        print(f"La temperatura en Celsius es: {resultado}")
    elif seleccion.upper()=="F":
        resultado=(temp*(9/5))+32
        print(f"La temperatura en Fahrenheit es: {resultado}")
    else:
        print("No seleccionaste de manera valida")
convertirTemp()