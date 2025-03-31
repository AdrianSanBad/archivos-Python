from pymongo import MongoClient

cliente = MongoClient("mongodb://localhost:27017/")
db = cliente["tienda"]
coleccion = db["productos"]
coleccion.insert_one({"nombre": "TV", "categoria": "Electrónica", "precio": 1200})
print(list(coleccion.find()))
