import pymongo
from pymongo import MongoClient
client = pymongo.MongoClient("mongodb+srv://pathaksudarshan27:ACetWTXzFQHXBw3d@cluster0.ic9pqga.mongodb.net/")
db = client["kurakani"]
collection = db["usre detail"]

data = {"name": "sudarshan pathak", "user_Id": "SEC079BEI009"}
result = collection.insert_one(data)

print(f"Inserted document ID: {result.inserted_id}")
