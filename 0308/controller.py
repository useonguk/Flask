from flask import render_template, request, redirect, url_for, Blueprint
# from index import app
from service import TodoService

todo_blueprint = Blueprint('todo', __name__)
todo_service = TodoService()

@todo_blueprint.route('/new_post')
def index():
    tasks = todo_service.get_tasks()
    return render_template('tasks.html', tasks=tasks)

@todo_blueprint.route('/add', methods=['POST'])
def add_task():
    task = request.form['task']
    todo_service.add_task({'name' : task, 'completed' : False})
    return redirect(url_for('todo.index'))

@todo_blueprint.route('/delete/<int:index>')
def delete_task(index):
    print(index)
    todo_service.delete_task(index)
    return redirect(url_for('todo.index')) # Blueprint('todo', __name__) 여기에 todo 되어있어서 blue print 안에있는 index 함수를 실행함

@todo_blueprint.route('/complete/<int:index>')
def complete_task(index):
    todo_service.com_task(index)
    return redirect(url_for('todo.index'))