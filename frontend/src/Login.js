import { useState } from "react";
import axios from "axios";
import { useNavigate, Link } from "react-router-dom";

export default function Login() {

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const login = async () => {
    try {
      const res = await axios.post("http://localhost:5000/login", {
        email,
        password
      });

      localStorage.setItem("token", res.data.token);

      alert("Login successful ✅");
      navigate("/search");

    } catch (err) {
      alert("Login failed ❌");
    }
  };

  return (
  <div className="container">
    <h2>🔐 Login</h2>

    <input placeholder="Email"
      onChange={(e)=>setEmail(e.target.value)} />

    <input type="password"
      placeholder="Password"
      onChange={(e)=>setPassword(e.target.value)} />

    <button onClick={login}>Login</button>

    <p style={{textAlign:"center"}}>
      Don't have an account? <Link to="/register">Register</Link>
    </p>
  </div>
);
}