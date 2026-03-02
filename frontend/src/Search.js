import { useState } from "react";
import axios from "axios";

export default function Search() {

  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false); 
  const [answer, setAnswer] = useState("");

  const search = async () => {
    setLoading(true);

    try {
      const token = localStorage.getItem("token");

      const res = await axios.post(
        "http://localhost:5000/search",
        { query },
        { headers: { Authorization: token } }
      );

      setResults(res.data.results);
      setAnswer(res.data.ai_answer);

    } catch (err) {
      console.error(err);
      alert("Search failed");
    }

    setLoading(false);
  };
  const getRelevance = (score) => {
  if (score >= 0.85)
    return { label: "Highly Relevant", color: "#16a34a" };

  if (score >= 0.75)
    return { label: "Relevant", color: "#eab308" };

  return { label: "Related", color: "#2563eb" };
};

  return (
  <div style={{maxWidth:"700px", margin:"40px auto"}}>
    <h1>🔎 AI Semantic Search</h1>

    <input
      placeholder="Ask something..."
      onChange={(e)=>setQuery(e.target.value)}
    />

    <button onClick={search}>Search</button>

    {loading && <p>🤖 Searching intelligently...</p>}

    {answer && (
      <div className="card" style={{background:"#eef2ff"}}>
        <h3>🤖 AI Answer</h3>
        <p>{answer}</p>
      </div>
    )}

    {results.map((r,i)=>(
      <div className="card" key={i}>
        <h3>{r.title}</h3>
        <p>{r.content}</p>
        <div className="score">Score: {r.score}</div>
      </div>
    ))}
  </div>
);
}