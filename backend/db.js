const mongoose = require("mongoose");

mongoose.connect(
  "mongodb+srv://myAtlasDBUser:Mongodb123@myatlasclusteredu.3leu0wh.mongodb.net/?retryWrites=true&w=majority"
).then(() => {
  console.log("✅ MongoDB connected (Node)");
}).catch(err => console.log(err));