"""solicite al usuario ingresar una contraseña y luego verifique si cumple con los siguientes requisitos:

Debe tener al menos 8 caracteres de longitud.
Debe contener al menos una letra mayúscula, una letra minúscula, un número y un carácter especial (como @, #, $, etc.)."""
def validarContrasenas():
    contra=input("Ingrese una contraseña: ")
    if len(contra)<8:
        print("La contraseña debe tener al menos 8 caracteres")
    else:
        mayuscula=False
        minuscula=False
        numero=False
        especial=False
        for i in contra:
            if i.isupper():
                mayuscula=True
            if i.islower():
                minuscula=True
            if i.isdigit():
                numero=True
            if i in ["@","#","$","%","&"]:
                especial=True
        if mayuscula and minuscula and numero and especial:
            print("La contraseña es valida")
        else:
            print("La contraseña no es valida")
validarContrasenas()