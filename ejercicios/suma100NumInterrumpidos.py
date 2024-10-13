#esta es la suma de numeros del n al m, donde n y m son ingresados por el usuario, y asi mismo n o m pueden ser el mayor o menor numero

"""def sumaNumInterrumpidos(n,m):
    if n==m:
        return n
    elif n>m:
        return n + sumaNumInterrumpidos(n-1,m)
    else:
        return m + sumaNumInterrumpidos(n,m-1)
    
    
print(sumaNumInterrumpidos(3,1))
"""

def sumNum(n,m):
    mayor = max(n,m)+1
    menor = min(n,m)
    total=[num for num in range(menor,mayor) if num<=mayor]
    return sum(total)
print(sumNum(3,1))

