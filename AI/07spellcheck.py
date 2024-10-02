from textblob import TextBlob

textWithMistakes = "I have a good speling!"

text= TextBlob(textWithMistakes)
correctedText= text.correct()

print('Original Text:', textWithMistakes)
print('Corrected Text:', correctedText)