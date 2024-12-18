
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASIGNACION COMENTARIO DIFERENTE DIVISION IGUAL MAS MAYOR MAYOR_IGUAL MENOR MENOR_IGUAL MENOS MULTIPLICACION NUMERO_ENTERO NUMERO_FLOTANTE PALABRA_RESERVADA PARENTESIS_DER PARENTESIS_IZQ VARIABLEprograma : instruccion\n                | programa instruccioninstruccion : asignacion\n                   | cicloasignacion : VARIABLE ASIGNACION exprasignacion : VARIABLE ASIGNACION errorciclo : PALABRA_RESERVADA PARENTESIS_IZQ condicion PARENTESIS_DER bloquecondicion : VARIABLE MENOR_IGUAL expr \n                 | VARIABLE MAYOR_IGUAL expr \n                 | VARIABLE IGUAL expr \n                 | VARIABLE DIFERENTE expr \n                 | VARIABLE MENOR expr \n                 | VARIABLE MAYOR exprcondicion : VARIABLE errorbloque : PARENTESIS_IZQ programa PARENTESIS_DERbloque : PARENTESIS_IZQ errorexpr : expr MAS term \n           | expr MENOS term \n           | termterm : term MULTIPLICACION factor \n           | term DIVISION factor \n           | factorfactor : NUMERO_ENTERO \n              | NUMERO_FLOTANTE \n              | VARIABLE'
    
_lr_action_items = {'VARIABLE':([0,1,2,3,4,7,8,9,10,11,12,13,14,15,16,19,20,21,22,24,25,26,27,28,29,31,32,33,34,35,36,43,44,45,],[5,5,-1,-3,-4,-2,10,18,-25,-5,-6,-19,-22,-23,-24,10,10,10,10,10,10,10,10,10,10,-17,-18,-20,-21,5,-7,5,-16,-15,]),'PALABRA_RESERVADA':([0,1,2,3,4,7,10,11,12,13,14,15,16,31,32,33,34,35,36,43,44,45,],[6,6,-1,-3,-4,-2,-25,-5,-6,-19,-22,-23,-24,-17,-18,-20,-21,6,-7,6,-16,-15,]),'$end':([1,2,3,4,7,10,11,12,13,14,15,16,31,32,33,34,36,44,45,],[0,-1,-3,-4,-2,-25,-5,-6,-19,-22,-23,-24,-17,-18,-20,-21,-7,-16,-15,]),'PARENTESIS_DER':([2,3,4,7,10,11,12,13,14,15,16,17,30,31,32,33,34,36,37,38,39,40,41,42,43,44,45,],[-1,-3,-4,-2,-25,-5,-6,-19,-22,-23,-24,23,-14,-17,-18,-20,-21,-7,-8,-9,-10,-11,-12,-13,45,-16,-15,]),'ASIGNACION':([5,],[8,]),'PARENTESIS_IZQ':([6,23,],[9,35,]),'error':([8,18,35,],[12,30,44,]),'NUMERO_ENTERO':([8,19,20,21,22,24,25,26,27,28,29,],[15,15,15,15,15,15,15,15,15,15,15,]),'NUMERO_FLOTANTE':([8,19,20,21,22,24,25,26,27,28,29,],[16,16,16,16,16,16,16,16,16,16,16,]),'MULTIPLICACION':([10,13,14,15,16,31,32,33,34,],[-25,21,-22,-23,-24,21,21,-20,-21,]),'DIVISION':([10,13,14,15,16,31,32,33,34,],[-25,22,-22,-23,-24,22,22,-20,-21,]),'MAS':([10,11,13,14,15,16,31,32,33,34,37,38,39,40,41,42,],[-25,19,-19,-22,-23,-24,-17,-18,-20,-21,19,19,19,19,19,19,]),'MENOS':([10,11,13,14,15,16,31,32,33,34,37,38,39,40,41,42,],[-25,20,-19,-22,-23,-24,-17,-18,-20,-21,20,20,20,20,20,20,]),'MENOR_IGUAL':([18,],[24,]),'MAYOR_IGUAL':([18,],[25,]),'IGUAL':([18,],[26,]),'DIFERENTE':([18,],[27,]),'MENOR':([18,],[28,]),'MAYOR':([18,],[29,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,35,],[1,43,]),'instruccion':([0,1,35,43,],[2,7,2,7,]),'asignacion':([0,1,35,43,],[3,3,3,3,]),'ciclo':([0,1,35,43,],[4,4,4,4,]),'expr':([8,24,25,26,27,28,29,],[11,37,38,39,40,41,42,]),'term':([8,19,20,24,25,26,27,28,29,],[13,31,32,13,13,13,13,13,13,]),'factor':([8,19,20,21,22,24,25,26,27,28,29,],[14,14,14,33,34,14,14,14,14,14,14,]),'condicion':([9,],[17,]),'bloque':([23,],[36,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> instruccion','programa',1,'p_programa','analizadorSintactico.py',72),
  ('programa -> programa instruccion','programa',2,'p_programa','analizadorSintactico.py',73),
  ('instruccion -> asignacion','instruccion',1,'p_instruccion','analizadorSintactico.py',80),
  ('instruccion -> ciclo','instruccion',1,'p_instruccion','analizadorSintactico.py',81),
  ('asignacion -> VARIABLE ASIGNACION expr','asignacion',3,'p_asignacion','analizadorSintactico.py',85),
  ('asignacion -> VARIABLE ASIGNACION error','asignacion',3,'p_asignacion_error','analizadorSintactico.py',90),
  ('ciclo -> PALABRA_RESERVADA PARENTESIS_IZQ condicion PARENTESIS_DER bloque','ciclo',5,'p_ciclo','analizadorSintactico.py',94),
  ('condicion -> VARIABLE MENOR_IGUAL expr','condicion',3,'p_condicion','analizadorSintactico.py',98),
  ('condicion -> VARIABLE MAYOR_IGUAL expr','condicion',3,'p_condicion','analizadorSintactico.py',99),
  ('condicion -> VARIABLE IGUAL expr','condicion',3,'p_condicion','analizadorSintactico.py',100),
  ('condicion -> VARIABLE DIFERENTE expr','condicion',3,'p_condicion','analizadorSintactico.py',101),
  ('condicion -> VARIABLE MENOR expr','condicion',3,'p_condicion','analizadorSintactico.py',102),
  ('condicion -> VARIABLE MAYOR expr','condicion',3,'p_condicion','analizadorSintactico.py',103),
  ('condicion -> VARIABLE error','condicion',2,'p_condicion_error','analizadorSintactico.py',109),
  ('bloque -> PARENTESIS_IZQ programa PARENTESIS_DER','bloque',3,'p_bloque','analizadorSintactico.py',113),
  ('bloque -> PARENTESIS_IZQ error','bloque',2,'p_bloque_error','analizadorSintactico.py',117),
  ('expr -> expr MAS term','expr',3,'p_expr','analizadorSintactico.py',121),
  ('expr -> expr MENOS term','expr',3,'p_expr','analizadorSintactico.py',122),
  ('expr -> term','expr',1,'p_expr','analizadorSintactico.py',123),
  ('term -> term MULTIPLICACION factor','term',3,'p_term','analizadorSintactico.py',130),
  ('term -> term DIVISION factor','term',3,'p_term','analizadorSintactico.py',131),
  ('term -> factor','term',1,'p_term','analizadorSintactico.py',132),
  ('factor -> NUMERO_ENTERO','factor',1,'p_factor','analizadorSintactico.py',139),
  ('factor -> NUMERO_FLOTANTE','factor',1,'p_factor','analizadorSintactico.py',140),
  ('factor -> VARIABLE','factor',1,'p_factor','analizadorSintactico.py',141),
]
