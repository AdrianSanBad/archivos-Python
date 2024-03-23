#programa que pedira un texto y verificara que sea un palindromo
#ejemplo: anita lava la tina
def palindromo():
    texto=input("Ingresa un texto que sospeches que es palindromo: ")
    texto=texto.lower()
    texto=texto.replace(" ","")
    cadena2=texto[::-1]
    print(f"El texto ingresado es: {texto}")
    print(f"El texto invertido es: {cadena2}")
    if texto==cadena2:
        print("Es palindromo")
    else:
        print("No es palindromo")
palindromo()