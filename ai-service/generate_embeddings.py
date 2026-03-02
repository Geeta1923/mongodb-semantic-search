import requests
from pymongo import MongoClient

# MongoDB connection
MONGO_URI = "mongodb+srv://myAtlasDBUser:Mongodb123@myatlasclusteredu.3leu0wh.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(MONGO_URI)

db = client["semantic_search_db"]
collection = db["student_notes"]

# Ollama embedding endpoint
OLLAMA_URL = "http://localhost:11434/api/embeddings"

for doc in collection.find():
    text = doc["content"]

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "nomic-embed-text",
            "prompt": text
        }
    )

    embedding = response.json()["embedding"]

    collection.update_one(
        {"_id": doc["_id"]},
        {"$set": {"embedding": embedding}}
    )

print("✅ Embeddings generated locally using Ollama!")