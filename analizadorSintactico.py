import ply.lex as lex #importa la librería ply.lex para hacer el análisis léxico
import ply.yacc as yacc #importa la librería ply.yacc para hacer el análisis sintáctico

# Definición de tokens
tokens = [
    'NUMERO_ENTERO', 'NUMERO_FLOTANTE', 'VARIABLE',
    'MAS', 'MENOS', 'MULTIPLICACION', 'DIVISION',
    'PARENTESIS_IZQ', 'PARENTESIS_DER', 'ASIGNACION','COMENTARIO'
]

# Reglas de expresión regular para tokens simples
t_MAS             = r'\+' #suma
t_MENOS           = r'-' #resta
t_MULTIPLICACION  = r'\*' #multiplicación
t_DIVISION        = r'/' #división
t_PARENTESIS_IZQ  = r'\(' #paréntesis de apertura
t_PARENTESIS_DER  = r'\)' #paréntesis de cierre
t_ASIGNACION      = r'=' #asignación

# Regla para ignorar comentarios delimitados por '|' al inicio y al final
def t_COMENTARIO(t):
    r'\|.*?\|' #expresión regular para un comentario
    pass  # No se hace nada, simplemente se ignora el comentario

# Reglas de expresión regular con acciones
def t_NUMERO_FLOTANTE(t): #definición de un número flotante
    r'\d+\.\d+' #expresión regular para un número flotante
    t.value = float(t.value) #conversión a flotante
    return t

def t_NUMERO_ENTERO(t): #definición de un número entero
    r'\d+' #expresión regular para un número entero
    t.value = int(t.value) #conversión a entero
    return t

def t_VARIABLE(t): #definición de una variable
    r'[a-zA-Z]' #expresión regular para una variable
    return t

# Ignorar espacios en blanco y nuevas líneas
t_ignore = ' \t\n' #ignora espacios en blanco y nuevas líneas

# Manejo de errores
def t_error(t): #función para manejar errores léxicos
    print(f"Carácter ilegal '{t.value[0]}'") #imprime el carácter ilegal
    t.lexer.skip(1) #salta el carácter ilegal

# Construcción del lexer
lexer = lex.lex() #crea el analizador léxico

#analizador sintáctico -->
# Definición de la gramática
def p_programa(p): #definición de un programa
    '''programa : asignacion
                | expr'''
    p[0] = ('programa', p[1]) #almacena el programa

def p_asignacion(p): #definición de una asignación
    '''asignacion : VARIABLE ASIGNACION expr'''
    p[0] = ('asignacion', p[1], p[2], p[3]) #almacena la asignación

def p_expr(p): #definición de una expresión
    '''expr : expr MAS term
            | expr MENOS term
            | term'''
    if len(p) == 4: #si la longitud de p es 4
        p[0] = ('expr', p[1], p[2], p[3]) #almacena la expresión
    else: 
        p[0] = p[1] #almacena el término

def p_term(p): #definición de un término
    '''term : term MULTIPLICACION factor
            | term DIVISION factor
            | factor'''
    if len(p) == 4: #si la longitud de p es 4
        p[0] = ('term', p[1], p[2], p[3]) #almacena el término
    else:
        p[0] = p[1] #almacena el factor

def p_factor(p): #definición de un factor
    '''factor : PARENTESIS_IZQ expr PARENTESIS_DER
              | NUMERO_ENTERO
              | NUMERO_FLOTANTE
              | VARIABLE'''
    if len(p) == 4: #si la longitud de p es 4
        p[0] = ('factor', p[2]) #almacena el factor
    else: 
        p[0] = p[1] #almacena el factor

# Manejo de errores de sintaxis
def p_error(p):
    if p:
        if p.type in ('MAS', 'MENOS', 'MULTIPLICACION', 'DIVISION'):
            print(f"Error de sintaxis en '{p.value}' en la posición {p.lexpos}. Duplicidad de símbolo o uso incorrecto.")
        elif p.type == 'PARENTESIS_IZQ':
            print("Error de sintaxis: Paréntesis de apertura sin paréntesis de cierre.")
        elif p.type == 'PARENTESIS_DER':
            print("Error de sintaxis: Paréntesis de cierre sin paréntesis de apertura.")
        elif p.type == 'VARIABLE':
            print(f"Error de sintaxis: Identificadores consecutivos en la posición {p.lexpos}.")
        else:
            print(f"Error de sintaxis en '{p.value}' en la posición {p.lexpos}.")
    else:
        print("Error de sintaxis en entrada.")

# Construcción del parser que utiliza la gramática definida anteriormente
parser = yacc.yacc()

# Función principal para analizar la entrada
def analizar(codigo): 
    #analizdor léxico
    lexer.input(codigo)
    print("Lexer: Tokeniza la entrada.\n")
    for token in lexer:
        print(f"{token.value} como {token.type}")
    #analizador sintáctico
    print("\nParser: Comienza a analizar la estructura.\n")
    resultado = parser.parse(codigo)
    if resultado:
        print(f"Resultado: {resultado}")

# Solicitar al usuario que ingrese el código
print("Ingresa tu ecuación. Presiona Enter dos veces para finalizar.")
codigo_fuente = ""
while True: #mientras no se presione Enter dos veces
    linea = input()
    if not linea: #si no hay entrada
        break #termina el ciclo
    codigo_fuente += linea + "\n" 

# Llamar al analizador
analizar(codigo_fuente)
