"""Unigram, for a single character or word (ex. "I").
Bigram, for two consecutive characters or words (ex. "I am").
Trigram, for three consecutive characters or words (ex. "I am learning")."""


from nltk import ngrams, word_tokenize
sample_text = 'estoy aprendiendo que son y como funcionan los tokens, es esta ocasion acerca de los n-grams'
tokens = word_tokenize(sample_text)

unigrams= list(ngrams(tokens, 1))
bigrams= list(ngrams(tokens, 2))
trigram=list(ngrams(tokens,3))
print(f"los unigrams son{unigrams}, \n los bigrams son{bigrams}, \n los trigrams son{trigram}")