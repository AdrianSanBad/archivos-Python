"""imprimimos del 1 al 100, si es multiplo de 3 imprimimos fizz, si es multiplo de 5 
imprimimos buzz, si es multiplo de ambos imprimimos fizzbuzz
"""
for i in range(1,101): #Se establece un rango de 1 a 100
#Si el residuo de i/3=0 entonces es multiplo, lo mismo con 5  
  if i%3==0 and i%5==0: #imprimimos fizzbuzz si es multiplo de ambos
    print("FizzBuzz")
  elif i%3==0: #imprimimos fizz si es multiplo de 3
    print("Fizz")
  elif i%5==0:
    print("Buzz") #imprimimos buzz si es multiplo de 5
  else:
    print(i)  #si no imprimimo el numero solamente
