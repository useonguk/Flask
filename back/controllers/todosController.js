// controllers/todosController.js

// 간단한 데이터베이스 대용 배열
let todos = [];

// 투두리스트 전체 조회
exports.getTodos = (req, res) => {
  res.json(todos);
};

// 투두리스트 추가
exports.addTodo = (req, res) => {
  const newTodo = req.body.todo;
  todos.push({ task: newTodo, completed: false });
  res.status(201).json({ message: "Todo added successfully" });
};

// 투두리스트 삭제
exports.deleteTodo = (req, res) => {
  const todoId = req.params.id;
  todos.splice(todoId, 1);
  res.json({ message: "Todo deleted successfully" });
};

// 투두리스트 완료 처리
exports.completeTodo = (req, res) => {
  const todoId = req.params.id;
  todos[todoId].completed = true;
  res.json({ message: "Todo completed successfully" });
};

// 투두리스트 보기
exports.getTodo = (req, res) => {
  const todoId = req.params.id;
  res.json(todos[todoId]);
};
