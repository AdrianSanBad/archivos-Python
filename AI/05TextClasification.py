#importamos las librerias necesarias
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
#generamos los textos que vamos a clasificar
texts = [
  'I love programming.', 'Python is amazing.',
  'I enjoy machine learning.', 'The weather is nice today.', 'I like algo.',
  'Machine learning is fascinating.', 'Natural Language Processing is a part of AI.'
]
#generamos las etiquetas de los textos

labels = [
  'tech', 'tech', 'tech', 'non-tech', 'tech', 'tech', 'tech'
]

#lo siguiente es convertir los textos en vectores de palabras
vectorizer=CountVectorizer()
#convertimos los textos en vectores de palabras
x=vectorizer.fit_transform(texts)
#dividimos los datos en datos de entrenamiento y de prueba mediante la funcion train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, labels, test_size=0.2, random_state=42)

#creamos el modelo de clasificacion
model = MultinomialNB()
#entrenamos el modelo
model.fit(x_train, y_train)

#realizamos la prediccion
y_pred = model.predict(x_test)
#calculamos la precision del modelo
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)