import math #se usa math para uso de pow(raiz)
def formulaGeneral(a,b,c): #definicion de funcion con recibo de a,b,c
    x1=(-b-math.pow(b**2-4*a*c,0.5))/(2*a) #calculo raiz 1
    x2=(-b+math.pow(b**2-4*a*c,0.5))/(2*a) # calculo raiz 2
    return x1,x2 #se regresa resultado
print(formulaGeneral(1,5,6)) #se muetra el resultado