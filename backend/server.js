require("./db");

const bcrypt = require("bcryptjs");
const jwt = require("jsonwebtoken");
const User = require("./models/User");
const SECRET = "mysecretkey";




const express = require("express");
const axios = require("axios");
const cors = require("cors");

const app = express();

app.use(cors());
app.use(express.json());


function auth(req, res, next) {
  const token = req.headers.authorization;

  if (!token)
    return res.status(401).json({ error: "Access denied" });

  try {
    jwt.verify(token, SECRET);
    next();
  } catch {
    res.status(401).json({ error: "Invalid token" });
  }
}




app.post("/register", async (req, res) => {
  try {
    const { username, email, password } = req.body;

    const hashedPassword = await bcrypt.hash(password, 10);

    const user = new User({
      username,
      email,
      password: hashedPassword
    });

    await user.save();

    res.json({ message: "User registered successfully" });

  } catch (err) {
    res.status(500).json({ error: "Registration failed" });
  }
});

app.post("/login", async (req, res) => {
  try {
    const { email, password } = req.body;

    const user = await User.findOne({ email });

    if (!user)
      return res.status(400).json({ error: "User not found" });

    const valid = await bcrypt.compare(password, user.password);

    if (!valid)
      return res.status(400).json({ error: "Invalid password" });

    const token = jwt.sign({ id: user._id }, SECRET, {
      expiresIn: "1h"
    });

    res.json({ token });

  } catch (err) {
    res.status(500).json({ error: "Login failed" });
  }
});





// call Python AI service
app.post("/search", auth, async (req, res) => {
  try {
    const { query } = req.body;

    const response = await axios({
      method: "post",
      url: "http://127.0.0.1:8000/semantic-search",
      params: { query: query }
    });

    res.json(response.data);

  } catch (error) {
    console.error(error);
    res.status(500).json({ error: "Search failed" });
  }
});

app.listen(5000, () => {
  console.log("✅ Node backend running on port 5000");
});