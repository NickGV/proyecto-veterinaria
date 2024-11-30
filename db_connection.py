import pymongo

url = "mongodb://localhost:27017/"
client = pymongo.MongoClient(url)

db = client["tiendaveterinaria"]
catalogos_collection = db["catalogos"]
compras_collection = db["historial_compras"]
ventas_collection = db["historial_ventas"]