from fastapi import FastAPI
from pymongo import MongoClient
import requests

app = FastAPI()


def detect_topic(query):
    q = query.lower()

    if any(word in q for word in ["database", "dbms", "normalization", "sql", "index"]):
        return "DBMS"

    if any(word in q for word in ["cpu", "process", "deadlock", "memory", "scheduling"]):
        return "OS"

    if any(word in q for word in ["tcp", "udp", "network", "protocol"]):
        return "CN"

    if any(word in q for word in ["search", "sort", "array", "algorithm"]):
        return "DSA"

    if any(word in q for word in ["learning", "model", "training", "ai"]):
        return "ML"

    return None



MONGO_URI = "mongodb+srv://myAtlasDBUser:Mongodb123@myatlasclusteredu.3leu0wh.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(MONGO_URI)

db = client["semantic_search_db"]
collection = db["student_notes"]

OLLAMA_URL = "http://localhost:11434/api/embeddings"
OLLAMA_GENERATE_URL = "http://localhost:11434/api/generate"

def generate_summary(query, content):
    try:
        prompt = f"""
        Answer the user's question using the provided context.

        Question: {query}

        Context:
        {content}

        Give a short clear explanation.
        """

        response = requests.post(
            OLLAMA_GENERATE_URL,
            json={
                "model": "phi3:mini",
                "prompt": prompt,
                "stream": False,
                "options": {
                    "maxTokens": 150,
                    "temperature": 0.3,
                    "num_predict": 80
                }
            },
            timeout=20
        )

        data = response.json()
        return data.get("response", "")

    except Exception as e:
     print("SUMMARY ERROR:", e)
    return "Relevant documents retrieved successfully."



@app.post("/semantic-search")
def semantic_search(query: str):

    print("QUERY RECEIVED:", query)

    topic = detect_topic(query)
    print("DETECTED TOPIC:", topic)

    
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "nomic-embed-text",
            "prompt": query
        }
    )

    query_embedding = response.json()["embedding"]

    
    vector_stage = {
        "$vectorSearch": {
            "index": "vector_index",   # put your real index name
            "path": "embedding",
            "queryVector": query_embedding,
            "numCandidates": 100,
            "limit": 5
        }
    }

  
    if topic:
        vector_stage["$vectorSearch"]["filter"] = {
            "topic": topic
        }

    
    results_cursor = collection.aggregate([
        vector_stage,
        {
            "$project": {
                "title": 1,
                "subject": 1,
                "content": 1,
                "topic": 1,
                "score": {"$meta": "vectorSearchScore"}
            }
        }
    ])

    results = list(results_cursor)

   
    CONFIDENCE_THRESHOLD = 0.75
    filtered = []
    seen_titles = set()

    for doc in results:
       if doc["score"] >= CONFIDENCE_THRESHOLD:

        # remove duplicates
        if doc["title"] in seen_titles:
            continue

        seen_titles.add(doc["title"])

        filtered.append({
            "title": doc["title"],
            "subject": doc["subject"],
            "content": doc["content"],
            "score": round(doc["score"], 4)
        })
        ai_answer = ""

       if filtered and filtered[0]["score"] > 0.80:
         ai_answer = generate_summary(query, filtered[0]["content"])

    return {"results": filtered, "ai_answer": ai_answer}