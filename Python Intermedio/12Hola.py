""" First, define a translator() function that takes a single language parameter.

Inside the function, add a translations dictionary that contains translations for common phrases in different languages:

translations = {
  'spanish': {'hello': 'hola', 'goodbye': 'adiós', 'thank you': 'gracias'},
  'french': {'hello': 'bonjour', 'goodbye': 'au revoir', 'thank you': 'merci'},
  'italian': {'hello': 'ciao', 'goodbye': 'arrivederci', 'thank you': 'grazie'}
}

Next, define an inner translate_word() function that takes a word parameter and returns a translation if the word exists in a specific language.

Return the inner translate_word() function from the outer translator() function. """

def translator(language):# Define la funcion traslator con un parametro language
    translations = {
        'spanish': {'hello': 'hola', 'goodbye': 'adiós', 'thank you': 'gracias'},
        'french': {'hello': 'bonjour', 'goodbye': 'au revoir', 'thank you': 'merci'},
        'italian': {'hello': 'ciao', 'goodbye': 'arrivederci', 'thank you': 'grazie'}
    }
    #define la funcion interna translate_word que toma un parametro word
    def translate_word(word):
        #si la palabra esta en las traducciones de la lengua
        if word in translations[language]:
            #retorna la palabra traducida
            return translations[language].get(word)
        else:
            #si no esta retorna un mensaje
            print('Word not found')
    return translate_word

traductor = translator('spanish')
print(traductor('hello'))