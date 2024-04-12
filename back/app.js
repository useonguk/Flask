// // app.js

// const express = require("express");
// const app = express();
// const PORT = process.env.PORT || 3000;
// const bodyParser = require("body-parser");
// const todosRouter = require("./routes/todos");

// // 바디 파서 미들웨어 설정
// app.use(bodyParser.json());

// // todos 라우터 설정
// app.use("/todos", todosRouter);

// // 서버 시작
// app.listen(PORT, () => {
//   console.log(`Server is running on port ${PORT}`);
// });
const express = require("express");
const app = express();
const PORT = process.env.PORT || 3000;
const bodyParser = require("body-parser");
const cors = require("cors"); // cors 미들웨어 추가
const todosRouter = require("./routes/todos");

// 바디 파서 미들웨어 설정
app.use(bodyParser.json());

// CORS 미들웨어 추가
app.use(cors());

// todos 라우터 설정
app.use("/todos", todosRouter);

// 서버 시작
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
