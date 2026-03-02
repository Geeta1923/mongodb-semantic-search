# 🚀 SemanticForge – Semantic Search Engine for MongoDB Documents

An AI-powered semantic search system that enables context-aware document retrieval using **MongoDB Atlas Vector Search**, **NLP embeddings**, and a **MERN + Python microservice architecture**.

---

## 📌 Problem Statement

Traditional database search relies on keyword matching, which fails when users phrase queries differently from stored documents. This leads to poor discoverability and inefficient information retrieval.

SemanticForge solves this problem by enabling **meaning-based search** using AI embeddings and MongoDB vector similarity search.

---

## ✨ Features

✅ Context-aware semantic search  
✅ Natural language query support  
✅ MongoDB Atlas Vector Search integration  
✅ AI-generated explanations  
✅ Topic-aware ranking  
✅ Confidence threshold filtering  
✅ Duplicate result removal  
✅ JWT Authentication system  
✅ MERN + FastAPI microservice architecture  

---

## 🧠 How It Works

1. Documents are stored in MongoDB.
2. AI generates vector embeddings for each document.
3. MongoDB Atlas creates a vector index.
4. User query → converted into embedding.
5. MongoDB performs similarity search.
6. Relevant documents are ranked and returned.
7. AI generates a short explanation.

---

## 🏗️ Architecture
User
↓
React Frontend
↓
Node.js Backend (API + Auth)
↓
Python FastAPI AI Service
↓
MongoDB Atlas Vector Search
↓
Ranked Results + AI Summary


---

## 🛠️ Technology Stack

| Layer | Technology |
|------|------------|
| Frontend | React.js |
| Backend | Node.js, Express.js |
| AI Service | Python, FastAPI |
| Database | MongoDB Atlas |
| Vector Search | MongoDB Atlas Vector Search |
| Embeddings | Ollama (nomic-embed-text) |
| AI Model | Lightweight Local LLM |
| Authentication | JWT |

---

## 📂 Project Structure
mongodb-semantic/
│
├── frontend/ # React UI
├── backend/ # Node.js API
├── ai-service/ # FastAPI AI processing
├── generate_embeddings.py
└── README.md


---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```
git clone https://github.com/Geeta1923/mongodb-semantic-search.git
cd semanticforge

    2️⃣ Start Ollama (AI Models)

Install models:
ollama pull nomic-embed-text
ollama pull phi3:mini

Run:

ollama serve

3️⃣ Run AI Service (FastAPI)
cd ai-service
uvicorn app:app --reload
Runs at:http://localhost:8000

4️⃣ Run Backend Server
cd backend
npm install
node server.js
Runs at: http://localhost:5000

5️⃣ Run Frontend
cd frontend
npm install
npm start
Runs at:http://localhost:3000

🔎 Example Queries

Explain database normalization
What is CPU scheduling?
Difference between TCP and UDP
What is Python?
Explain supervised learning


---

### Demo Documents

### 🔐 Login Page
![Login Page](screenshots/login.png)

---

### 🔎 Search Interface
![Search Interface](screenshots/search.png)

---

### 🤖 AI Answer Output
![AI Answer](screenshots/ai_answer.png)

---

### 📊 Ranked Results
![Ranked Results](screenshots/results.png)



🌍 Use Cases

Educational content search
Enterprise documentation retrieval
Knowledge base systems
FAQ and support platforms

🚀 Future Enhancements

Hybrid keyword + semantic search
External dataset integration
Multi-language support
Cloud deployment
Personalized ranking

👩‍💻 Author

Geeta Galagali
SemanticForge – hack-n-go-with-mongodb Project

📜 License

This project is developed for educational and hackathon purposes.

