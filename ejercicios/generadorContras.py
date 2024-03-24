"""programa que genera contraseñas aleatorias de 8 caracteres y debe 
contener al menos una letra mayúscula, una letra minúscula, un número y un carácter especial """
import random
import string

def generar_contraseña():
    # Definir conjuntos de caracteres 
    letras_mayusculas = string.ascii_uppercase # A-Z
    letras_minusculas = string.ascii_lowercase # a-z
    numeros = string.digits # 0-9
    caracteresEspeciales = string.punctuation # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

    # Combinar todos los conjuntos de caracteres
    caracteres = letras_mayusculas + letras_minusculas + numeros + caracteresEspeciales #suma de todos los conjuntos

    # Generar una contraseña aleatoria de longitud mínima 8
    longitudMinima = 8 
    contraseña = ''.join(random.choice(caracteres) for i in range(longitudMinima))  #join une los caracteres de la lista generada por random.choice

    while not (any(c.isupper() for c in contraseña) and #any devuelve True si al menos uno de los elementos del iterable es True
               any(c.islower() for c in contraseña) and #isupper() y islower() son métodos de la clase string que devuelven True si el string es mayúscula o minúscula respectivamente
               any(c.isdigit() for c in contraseña) and #isdigit() es un método de la clase string que devuelve True si el string es un dígito
               any(c in caracteresEspeciales for c in contraseña)): #in devuelve True si el caracter está en la cadena caracteresEspeciales
        contraseña = ''.join(random.choice(caracteres) for i in range(longitudMinima)) #si no cumple con las condiciones se genera una nueva contraseña

    print(f"La nueva contraseña generada es: {contraseña} ")


nueva_contraseña = generar_contraseña()

