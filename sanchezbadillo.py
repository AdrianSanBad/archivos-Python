a= 1 
x= 2
expresion1= (2*x)/(a+x)+3*x/(a-x)+(3*x**2+a**2)/(a**2-x**2)
expresion2= (2*x * (a**2 - x**2) / (a + x)) + (3*x * (a**2 - x**2) / (a - x)) + ((3*x**2 + a**2) * (a**2 - x**2) / (a**2 - x**2))/ (a**2 - x**2)
expresion3= (2*x * (a**2 - x**2) / (a + x)) + (3*x * (a**2 - x**2) / (a - x)) + ((3*x**2 + a**2) * (a**2 - x**2) / (a**2 - x**2)) /(a**2 - x**2)
expresion4= ((2*a*x) - (2*x**4) + 3*a*x + 3*x**2 + 3*x**2 + a**2) / (a**3 - x**3)

print(expresion1)
print(expresion2)
print(expresion3)
print(expresion4)