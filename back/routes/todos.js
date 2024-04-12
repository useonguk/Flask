// routes/todos.js

const express = require("express");
const router = express.Router();
let nextId = 1; // 다음 ID 값 초기화

// 간단한 데이터베이스 대용 배열
let todos = [];

// 투두리스트 전체 조회
router.get("/", (req, res) => {
  res.json(
    todos.map((todo) => ({
      id: todo.id,
      task: todo.task,
      completed: todo.completed,
    }))
  );
});

// 투두리스트 추가
router.post("/", (req, res) => {
  const newTodo = req.body.todo;
  todos.push({ id: nextId++, task: newTodo, completed: false });
  res.status(201).json({ message: "Todo added successfully" });
});

// 투두리스트 삭제
router.delete("/:id", (req, res) => {
  const todoId = req.params.id;
  todos = todos.filter((todo) => todo.id !== parseInt(todoId));
  res.json({ message: "Todo deleted successfully" });
});

// 투두리스트 완료 처리
router.put("/:id/complete", (req, res) => {
  const todoId = req.params.id;
  todos.find((todo) => todo.id === parseInt(todoId)).completed = true;
  res.json({ message: "Todo completed successfully" });
});

// 투두리스트 보기
router.get("/:id", (req, res) => {
  const todoId = req.params.id;
  const foundTodo = todos.find((todo) => todo.id === parseInt(todoId));
  if (foundTodo) {
    res.json(foundTodo);
  } else {
    res.status(404).json({ message: "Todo not found" });
  }
});

module.exports = router;
