import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Load environment variables from .env file
load_dotenv()

# Get the MongoDB URI from the environment variables
MONGO_URI = os.getenv("MONGO_URI")

# Connect to the database using the URI
client = MongoClient(MONGO_URI)
db = client["notes"]
collection = db["notes"]

# print("Successfully connected to MongoDB!")