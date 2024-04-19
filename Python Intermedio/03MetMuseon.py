#forma de usar un diccionario en python 
artifact={"title":"The Death of Socrates", 
"Artist": "Jacques Louis David (French, Paris 1748–1825 Brussels",
"Date": "1787",
"Medium": "Oil on canvas",
"Dimensions": "51 x 77 1/4 in. (129.5 x 196.2 cm)",
"Classification": "Paintings",
"Credit_Line": "Catharine Lorillard Wolfe Collection, Wolfe Fund, 1931",
"AccessionNumber": "31.45"}
print(artifact["Date"])
print(artifact["Medium"])
print(artifact.keys())
print(artifact.values())
print(artifact.items())