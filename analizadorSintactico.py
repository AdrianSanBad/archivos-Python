import ply.lex as lex
import ply.yacc as yacc
import tkinter as tk
from tkinter import filedialog

# Definición de tokens
tokens = [
    'NUMERO_ENTERO', 'NUMERO_FLOTANTE', 'VARIABLE',
    'MAS', 'MENOS', 'MULTIPLICACION', 'DIVISION',
    'PARENTESIS_IZQ', 'PARENTESIS_DER', 'ASIGNACION',
    'PALABRA_RESERVADA', 'COMENTARIO',
    'MENOR', 'MENOR_IGUAL', 'MAYOR', 'MAYOR_IGUAL', 'IGUAL', 'DIFERENTE'
]

# Palabras reservadas
reserved_words = {
    'ciclo': 'PALABRA_RESERVADA',
    'terminar': 'PALABRA_RESERVADA'
}

# Reglas de tokens simples
t_MAS = r'\+'
t_MENOS = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_PARENTESIS_IZQ = r'\('
t_PARENTESIS_DER = r'\)'
t_ASIGNACION = r'='
t_MENOR = r'<'
t_MENOR_IGUAL = r'<='
t_MAYOR = r'>'
t_MAYOR_IGUAL = r'>='
t_IGUAL = r'=='
t_DIFERENTE = r'!='

# Reglas avanzadas
def t_COMENTARIO(t):
    r'\|.*?\|'
    pass  # Ignorar comentarios

def t_NUMERO_FLOTANTE(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_NUMERO_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_VARIABLE(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved_words.get(t.value, 'VARIABLE')  # Determina si es palabra reservada
    return t

# Ignorar espacios y saltos de línea
t_ignore = ' \t\n'

# Manejo de errores léxicos
def t_error(t):
    texto_sintactico.insert(tk.END, f"Error léxico: Carácter ilegal '{t.value[0]}'\n")
    t.lexer.skip(1)

# Construcción del lexer
lexer = lex.lex()

# Variables globales para el análisis semántico
variables_definidas = set()

# Gramática del parser
def p_programa(p):
    '''programa : instruccion
                | programa instruccion'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_instruccion(p):
    '''instruccion : asignacion
                   | ciclo'''
    p[0] = p[1]

def p_asignacion(p):
    '''asignacion : VARIABLE ASIGNACION expr'''
    variables_definidas.add(p[1])  # Registrar la variable como definida
    p[0] = ('asignacion', p[1], p[3])

def p_ciclo(p):
    '''ciclo : PALABRA_RESERVADA PARENTESIS_IZQ condicion PARENTESIS_DER bloque'''
    p[0] = ('ciclo', p[3], p[5])

def p_bloque(p):
    '''bloque : PARENTESIS_IZQ programa PARENTESIS_DER'''
    p[0] = p[2]

def p_condicion(p):
    '''condicion : VARIABLE MENOR_IGUAL expr 
                 | VARIABLE MAYOR_IGUAL expr 
                 | VARIABLE IGUAL expr 
                 | VARIABLE DIFERENTE expr 
                 | VARIABLE MENOR expr 
                 | VARIABLE MAYOR expr'''
    if p[1] not in variables_definidas:
        raise ValueError(f"Variable no definida: {p[1]}")
    p[0] = ('condicion', p[1], p[2], p[3])

def p_expr(p):
    '''expr : expr MAS term 
           | expr MENOS term 
           | term'''
    if len(p) == 4:
        p[0] = ('expr', p[1], p[2], p[3])
    else:
        p[0] = p[1]

def p_term(p):
    '''term : term MULTIPLICACION factor 
           | term DIVISION factor 
           | factor'''
    if len(p) == 4:
        p[0] = ('term', p[1], p[2], p[3])
    else:
        p[0] = p[1]

def p_factor(p):
    '''factor : NUMERO_ENTERO 
              | NUMERO_FLOTANTE 
              | VARIABLE'''
    if isinstance(p[1], str) and p[1] not in variables_definidas:
        raise ValueError(f"Variable no definida: {p[1]}")
    p[0] = p[1]

# Manejo de errores sintácticos
def p_error(p):
    if p:
        texto_sintactico.insert(tk.END, f"Error de sintaxis: Token inesperado '{p.value}' en la línea {p.lineno}\n")
    else:
        texto_sintactico.insert(tk.END, "Error de sintaxis: Fin inesperado del archivo.\n")

# Construcción del parser
parser = yacc.yacc()

# Funciones para la interfaz gráfica
def analizar(codigo):
    global variables_definidas
    variables_definidas = set()  # Reiniciar variables definidas
    texto_lexico.delete('1.0', tk.END)
    texto_sintactico.delete('1.0', tk.END)
    texto_semantico.delete('1.0', tk.END)

    lexer.input(codigo)
    tokens_lexicos = [f"{token.value} ({token.type})" for token in lexer]
    texto_lexico.insert(tk.END, "\n".join(tokens_lexicos) + "\n")

    try:
        resultado = parser.parse(codigo)
        tokens_sintacticos = "\n".join(str(item) for item in resultado) if resultado else "No se generaron tokens sintácticos."
        texto_sintactico.insert(tk.END, tokens_sintacticos + "\n")
        semantico = f"Variables definidas: {', '.join(variables_definidas)}\n"
    except ValueError as e:
        semantico = f"Error semántico: {e}\n"
        texto_sintactico.insert(tk.END, "Error en el análisis sintáctico.\n")
    except Exception as e:
        semantico = f"Error: {e}\n"
        texto_sintactico.insert(tk.END, "Error en el análisis sintáctico.\n")

    texto_semantico.insert(tk.END, semantico)

def abrir_archivo():
    ruta = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
    if ruta:
        with open(ruta, 'r') as archivo:
            contenido = archivo.read()
        archivo_actual.set(ruta)
        texto_codigo.delete('1.0', tk.END)
        texto_codigo.insert(tk.END, contenido)

def ejecutar_analisis():
    codigo = texto_codigo.get('1.0', tk.END).strip()
    if not codigo:
        texto_sintactico.insert(tk.END, "Error: El archivo está vacío.\n")
        return
    analizar(codigo)

# Interfaz gráfica
ventana = tk.Tk()
ventana.title("Analizador Léxico, Sintáctico y Semántico")

archivo_actual = tk.StringVar()
archivo_actual.set("ejercicio1.txt")

tk.Label(ventana, text="Archivo:").grid(row=0, column=0, padx=5, pady=5)
tk.Label(ventana, textvariable=archivo_actual).grid(row=0, column=1, padx=5, pady=5)

tk.Button(ventana, text="Abrir archivo", command=abrir_archivo).grid(row=0, column=2, padx=5, pady=5)
tk.Button(ventana, text="Ejecutar análisis", command=ejecutar_analisis).grid(row=0, column=3, padx=5, pady=5)

tk.Label(ventana, text="Código fuente:").grid(row=1, column=0, columnspan=4, padx=5, pady=5)
texto_codigo = tk.Text(ventana, height=10, width=80)
texto_codigo.grid(row=2, column=0, columnspan=4, padx=5, pady=5)

tk.Label(ventana, text="Tokens Léxicos:").grid(row=3, column=0, padx=5, pady=5)
texto_lexico = tk.Text(ventana, height=10, width=30)
texto_lexico.grid(row=4, column=0, padx=5, pady=5)

tk.Label(ventana, text="Tokens Sintácticos:").grid(row=3, column=1, padx=5, pady=5)
texto_sintactico = tk.Text(ventana, height=10, width=30)
texto_sintactico.grid(row=4, column=1, padx=5, pady=5)

tk.Label(ventana, text="Análisis Semántico:").grid(row=3, column=2, padx=5, pady=5)
texto_semantico = tk.Text(ventana, height=10, width=30)
texto_semantico.grid(row=4, column=2, padx=5, pady=5)

ventana.mainloop()
