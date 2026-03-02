import requests
from pymongo import MongoClient

# MongoDB connection
MONGO_URI = "mongodb+srv://myAtlasDBUser:Mongodb123@myatlasclusteredu.3leu0wh.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(MONGO_URI)

db = client["semantic_search_db"]
collection = db["student_notes"]

# Ollama endpoint
OLLAMA_URL = "http://localhost:11434/api/embeddings"

# 🔎 Ask user for query
query = input("Enter your search query: ")

# Convert query to embedding
response = requests.post(
    OLLAMA_URL,
    json={
        "model": "nomic-embed-text",
        "prompt": query
    }
)

query_embedding = response.json()["embedding"]

# Perform vector search
results = list(collection.aggregate([
    {
        "$vectorSearch": {
            "index": "vector_index",
            "path": "embedding",
            "queryVector": query_embedding,
            "numCandidates": 100,
            "limit": 3,
            "similarity": "cosine"
        }
    },
    {
        "$project": {
            "title": 1,
            "subject": 1,
            "content": 1,
            "score": {"$meta": "vectorSearchScore"}
        }
    }
]))

# Hybrid ranking boost
boosted_results = []

query_lower = query.lower()

for doc in results:
    boost = 0
    
    if doc["title"].lower() in query_lower:
        boost += 0.05
        
    if any(word in doc["title"].lower() for word in query_lower.split()):
        boost += 0.03

    final_score = doc["score"] + boost
    
    boosted_results.append((final_score, doc))

# Sort by boosted score
boosted_results.sort(reverse=True, key=lambda x: x[0])

CONFIDENCE_THRESHOLD = 0.75

print("\n🔎 Final Filtered Results:\n")

found = False

for score, doc in boosted_results:
    if score >= CONFIDENCE_THRESHOLD:
        found = True
        print("Title:", doc["title"])
        print("Final Score:", round(score, 4))
        print("Subject:", doc["subject"])
        print("Content:", doc["content"][:150], "...\n")

if not found:
    print("No highly confident results found.")









