from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from bson.objectid import ObjectId

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

# MongoDB connection
client = MongoClient(os.getenv('MONGO_URI'))
db = client.todo_db  # MongoDB database
todos_collection = db.todos  # MongoDB collection for todos


# 1. Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = db.users.find_one({'email': email, 'password': password})
        if user:
            return redirect(url_for('main'))
        else:
            return render_template('login.html', error="Invalid email or password")
    return render_template('login.html')


# 2. Main Page Route
@app.route('/')
def main():
    return render_template('main.html')


# 3. Add New To-Do Task Route
@app.route('/add_new', methods=['GET', 'POST'])
def add_new():
    if request.method == 'POST':
        list_title = request.form['list_title']
        time = request.form['time']
        todo_content = request.form['todo_content']
        status = request.form['status']
        
        todos_collection.insert_one({
            'list_title': list_title,
            'time': time,
            'todo_content': todo_content,
            'status': status
        })
        flash('New to-do task created successfully!')
        return redirect(url_for('main'))
    
    return render_template('add.html')


# 4. Display a Single To-Do Task Route
@app.route('/task/<todo_id>')
def display_todo(todo_id):
    todo = todos_collection.find_one({'_id': ObjectId(todo_id)})
    return render_template('display.html', todo=todo)


# 5. Edit an Existing To-Do Task Route
@app.route('/edit/<todo_id>', methods=['GET', 'POST'])
def edit_todo(todo_id):
    todo = todos_collection.find_one({'_id': ObjectId(todo_id)})

    if request.method == 'POST':
        list_title = request.form['list_title']
        time = request.form['time']
        todo_content = request.form['todo_content']
        status = request.form['status']

        todos_collection.update_one({'_id': ObjectId(todo_id)}, {'$set': {
            'list_title': list_title,
            'time': time,
            'todo_content': todo_content,
            'status': status
        }})
        flash('Task updated successfully!')
        return redirect(url_for('main'))

    return render_template('edit.html', todo=todo)


# 6. Delete To-Do Task Route
@app.route('/delete/<todo_id>', methods=['GET', 'POST'])
def delete_todo(todo_id):
    todos_collection.delete_one({'_id': ObjectId(todo_id)})
    flash('Task deleted successfully!')
    return redirect(url_for('main'))


# 7. Search for a To-Do Task Route
@app.route('/search', methods=['GET'])
def search():
    search_keyword = request.args.get('search_keyword')
    if search_keyword:
        search_results = todos_collection.find({'list_title': {'$regex': search_keyword, '$options': 'i'}})
        return render_template('search.html', search_results=search_results, search_keyword=search_keyword)
    return render_template('search.html', search_results=[])


# 8. View All Tasks Route with Filtering
@app.route('/view_all', methods=['GET', 'POST'])
def view_all():
    filter_status = request.form.get('filter', 'all')
    if filter_status == 'all':
        todos = todos_collection.find()
    else:
        todos = todos_collection.find({'status': filter_status})

    return render_template('view_all.html', todos=todos)


if __name__ == '__main__':
    app.run(debug=True)
