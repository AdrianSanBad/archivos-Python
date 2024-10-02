from translate import Translator

#generemos una variable que traduzca de ingles a español
Translator= Translator(to_lang="es")
#traducimos un texto
text = "Hello, how are you?, whasu up?"

#realizamos la traduccion
translation= Translator.translate(text)

#imprimimos la traduccion
print(translation)