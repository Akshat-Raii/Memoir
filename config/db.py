from pymongo import MongoClient


client = MongoClient("mongodb+srv://akshat:akshat0365@memoir.do177tt.mongodb.net/")
db = client["notes"]
collection = db["notes"]
