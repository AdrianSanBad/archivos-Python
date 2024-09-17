#Adrian Sanchez Badillo 21200629

#se importan las librerias que sera necesarias para la ejecucion del programa
import threading
import time
import random
import math

# Variables globales para compartir resultados entre hilos
#se declaran none por que aun no se les asigna un valor
resultado_b2 = None
resultado_4ac = None
resultado_raiz = None
resultado_x1 = None
resultado_x2 = None

# Función para imprimir con sangría, dependiendo del proceso en el que se encuentre
def imprimir_con_sangria(mensaje, nivel):
    print(" " * nivel + mensaje)

# Función que calcula b^2 integrando un retardo aleatorio entre 0.1 y 1.0 segundos
def calcular_b2(b):
    global resultado_b2 #se declara la variable como global para poder ser usada en todo el programa
    time.sleep(random.uniform(0.1, 1.0))  # Retardo aleatorio
    resultado_b2 = b ** 2 #se calcula el valor de b^2
    imprimir_con_sangria(f"Proceso 1: Calculando b^2 = {resultado_b2}", 0) #se imprime el resultado dando una sangria 

# Función que calcula 4*a*c 
def calcular_4ac(a, c):
    global resultado_4ac 
    time.sleep(random.uniform(0.1, 3.0))  # Retardo aleatorio de 0.1 a 1.0 segundos
    resultado_4ac = 4 * a * c #se calcula el valor de 4*a*c
    imprimir_con_sangria(f"Proceso 2: Calculando 4*a*c = {resultado_4ac}", 2) #se imprime el resultado dando una sangria

# Función que calcula la raíz cuadrada de (b^2 - 4*a*c) 
def calcular_raiz():
    global resultado_raiz
    while resultado_b2 is None or resultado_4ac is None:
        time.sleep(0.1)  # Espera activa hasta que los valores estén listos
    time.sleep(random.uniform(0.1, 3.0))  # Retardo aleatorio
    discriminante = resultado_b2 - resultado_4ac
    if discriminante >= 0:
        resultado_raiz = math.sqrt(discriminante)
        imprimir_con_sangria(f"Proceso 3: Calculando la raíz de {discriminante} = {resultado_raiz}", 4)
    else:
        imprimir_con_sangria(f"Proceso 3: Discriminante negativo, no hay soluciones reales.", 4)

# Función que calcula las dos soluciones de la ecuación
def calcular_soluciones(a, b):
    global resultado_x1, resultado_x2 #se declaran las variables como globales para poder ser usadas en todo el programa
    while resultado_raiz is None: #mientras que resultado_raiz sea none se espera 0.1 segundos
        time.sleep(0.1)  # Espera activa hasta que la raíz esté lista
    time.sleep(random.uniform(0.1, 2.0))  # Retardo aleatorio
    resultado_x1 = (-b + resultado_raiz) / (2 * a)
    resultado_x2 = (-b - resultado_raiz) / (2 * a)
    imprimir_con_sangria(f"Proceso 4: Calculando x1 = {resultado_x1}", 6)
    imprimir_con_sangria(f"Proceso 5: Calculando x2 = {resultado_x2}", 6)

# Función principal para levantar todos los hilos
def resolver_ecuacion(a, b, c):
    imprimir_con_sangria(f"Resolviendo ecuación {a}x^2 + {b}x + {c} = 0", 0)
    
    # Crear y lanzar los hilos
    hilo_b2 = threading.Thread(target=calcular_b2, args=(b,)) #
    hilo_4ac = threading.Thread(target=calcular_4ac, args=(a, c))
    hilo_raiz = threading.Thread(target=calcular_raiz)
    hilo_soluciones = threading.Thread(target=calcular_soluciones, args=(a, b))
    
    # Iniciar los hilos
    hilo_b2.start()
    hilo_4ac.start()
    hilo_raiz.start()
    hilo_soluciones.start()
    
    # Esperar a que todos los hilos terminen
    hilo_b2.join() 
    hilo_4ac.join()
    hilo_raiz.join()
    hilo_soluciones.join()

    imprimir_con_sangria("Ecuación resuelta.", 0) 

# Ejecución del programa
if __name__ == "__main__":
    a = 1  # Coeficiente de x^2
    b = -3  # Coeficiente de x
    c = 2  # Coeficiente constante

    resolver_ecuacion(a, b, c)
