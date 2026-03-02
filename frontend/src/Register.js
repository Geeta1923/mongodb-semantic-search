import { useState } from "react";
import axios from "axios";
import { useNavigate, Link } from "react-router-dom";

export default function Register() {

  const navigate = useNavigate();

  const [user, setUser] = useState({
    username: "",
    email: "",
    password: ""
  });

  const register = async () => {
    try {
      await axios.post("http://localhost:5000/register", user);

      alert("Registration successful ✅");
      navigate("/");

    } catch (err) {
      alert("Registration failed ❌");
    }
  };

return (
  <div className="container">
    <h2>🧾 Register</h2>

    <input placeholder="Username"
      onChange={(e)=>setUser({...user, username:e.target.value})} />

    <input placeholder="Email"
      onChange={(e)=>setUser({...user, email:e.target.value})} />

    <input type="password"
      placeholder="Password"
      onChange={(e)=>setUser({...user, password:e.target.value})} />

    <button onClick={register}>Register</button>

    <p style={{textAlign:"center"}}>
      Already have an account? <Link to="/">Login</Link>
    </p>
  </div>
);
}