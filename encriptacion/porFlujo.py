#Encriptacion por flujo de bits usando ASCII y XOR
separada=[]
claveRep=[]
binarioFrase=[]
binarioClave=[]
resultadoXOR=[]
desencriptado=[]

def encriptar(frase,clave):
    iterador=len(clave)
    #guardamos las letras en char usando la lista separada
    for i in frase:
        separada.append(i)
    #Creacion de la claveRep que contiene la repeticion de clave las veces necesarias
    for i in range(len(separada)):
        #hacemos que a claveRep se le guarde el index de clave pero repitiendola usando % regresando lo 
        # restante que nos ayuda a saber en que posicion continuar(si i=5 y iterador=3 entonces regresa 2 que de asb es b)
        claveRep.append(clave[i%iterador])
    #recorremos el tamaño de nuestra frase donde guardamos
    for i in range(len(separada)):
        binarioFrase.append(charToBinario(separada[i]))
        binarioClave.append(charToBinario(claveRep[i]))
        xor=int(binarioFrase[i],2) ^ int(binarioClave[i],2)
        resultadoXOR.append(format(xor,"08b"))
        print(f"letra: {separada[i]} binario: {binarioFrase[i]}")
    print(f"resultado XOR: {resultadoXOR}")



def desencriptar(encriptada,clave):
    for i in range(len(resultadoXOR)):
        xor=int(resultadoXOR[i],2) ^ int(binarioClave[i],2)
        desencriptado.append(binarioToChar(format(xor, '08b')))
        print(desencriptado[i])

#Metodo que convierte de char a binario
def charToBinario(char):
    return bin(ord(char))[2:]
#metodo que convierte de binario a char
def binarioToChar(binario):
    return chr(int(binario, 2))



# Ejemplo de uso
encriptar("ADRIANSANCHEZBADILLO","ASB")
desencriptar(resultadoXOR,"ASB")
