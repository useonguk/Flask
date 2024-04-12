from datetime import datetime
from flask import render_template, request, redirect, url_for, Blueprint
# from index import app
from services.service import PostService

post_blueprint = Blueprint('post', __name__)
post_service = PostService()

@post_blueprint.route('/')
def index():
    tasks = post_service.get_tasks()
    return render_template('index.html', post=tasks)

@post_blueprint.route('/new_post', methods=['POST', 'GET'])
def add_task() :
    if request.method == 'POST' :
        title = request.form['title']
        content = request.form['content']
        author = request.form['author']
        post_service.add_task({'title': title, 'content': content, 'author': author, 'created_at': datetime.today()})
        return redirect(url_for("post.index"))
    return render_template('create.html')

@post_blueprint.route('/update/<int:index>', methods=['POST', 'GET'])
def update(index) :
    tasks = post_service.get(index)
    if request.method == 'POST':
        id = index
        title = request.form['title']
        content = request.form['content']
        author = request.form['author']
        post_service.updata_tasks({"id" : id, 'title': title, 'content': content, 'author': author, 'created_at': datetime.today()})
        return redirect(url_for("post.index", post=tasks))
    return render_template('update.html', post=tasks)

@post_blueprint.route('/delete/<int:index>')
def delete(index) :
    id = index
    post_service.delete_tasks(id)
    return  redirect(url_for("post.index"))