import nltk
# se tuvo que descargar extension: nltk.download('punkt_tab')
textoDeEjemplo="debo aprender a leer primero la documentacion por que abajo decia que tenia que instalar la extencion punkt_tab"
tokens= nltk.word_tokenize(textoDeEjemplo.lower())
print(f"Tokens: {tokens}")