// models/todoModel.js

// Todo 항목을 저장하는 배열입니다.
let todos = [];

// Todo 모델 객체입니다.
const Todo = {
  // 모든 Todo 항목을 반환합니다.
  getAllTodos: () => todos,

  // 새로운 Todo 항목을 추가합니다.
  addTodo: (todo) => todos.push(todo),

  // 특정 ID를 가진 Todo 항목을 삭제합니다.
  deleteTodo: (id) => {
    todos = todos.filter((todo) => todo.id !== id);
  },
};

// Todo 모델을 외부에서 사용할 수 있도록 내보냅니다.
module.exports = Todo;
