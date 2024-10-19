import os
from flask import Flask, render_template, request, redirect, url_for, flash, session
import pymongo
from bson.objectid import ObjectId
from dotenv import load_dotenv

#import ssl
#print(ssl.OPENSSL_VERSION)


load_dotenv()  # load environment variables from .env file

def create_app():
    """
    Create and configure the Flask application.
    returns: app: the Flask application object
    """

    app = Flask(__name__)
    app.secret_key = os.getenv('SECRET_KEY') or 'default_secret_key'

    client = pymongo.MongoClient(os.getenv("MONGO_URI"))
    db = client.todolist
    users_collection = db.users
    todos_collection = db.todos

    try:
        client.admin.command("ping")
        print(" *", "Connected to MongoDB!")
    except Exception as e:
        print(" * MongoDB connection error:", e)

    # 1. Signup Route
    @app.route('/signup', methods=['GET', 'POST'])
    def signup():
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']

            # Check if the user already exists
            existing_user = users_collection.find_one({'email': email})
            if existing_user:
                flash('Email already registered. Please log in.', 'danger')
                return redirect(url_for('login'))

            # Insert new user
            users_collection.insert_one({'email': email, 'password': password})
            flash('Signup successful! Please log in.', 'success')
            return redirect(url_for('login'))

        return render_template('signup.html')
    # 2. Login Route
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']

            user = users_collection.find_one({'email': email, 'password': password})
            if user:
                session['user_id'] = str(user['_id'])
                flash('Login successful!', 'success')
                return redirect(url_for('main'))
            else:
                flash('Invalid credentials.', 'danger')

        return render_template('login.html')
    # 3. Main Page Route
    @app.route('/')
    def main():
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return render_template('main.html')
    
    # 4. Add New To-Do Task Route
    @app.route('/add_new', methods=['GET', 'POST'])
    def add_new():
        if 'user_id' not in session:
            return redirect(url_for('login'))

        if request.method == 'POST':
            task = {
                'user_id': session['user_id'],
                'list_title': request.form['list_title'],
                'time': request.form['time'],
                'todo_content': request.form['todo_content'],
                'status': request.form['status']
            }
            todos_collection.insert_one(task)
            flash('New task added!', 'success')
            return redirect(url_for('view_all'))

        return render_template('add.html')
    
    # 5. View All Tasks for Logged-in User
    @app.route('/view_all', methods=['GET','POST'])
    def view_all():
        if 'user_id' not in session:
            return redirect(url_for('login'))

        user_id = session['user_id']
        filter_value = 'all' #default

        if request.method == 'POST':
            filter_value = request.form.get('filter')

            if filter_value == 'to_do':
                todos = todos_collection.find({'user_id': user_id, 'status': 'to_do'})
            elif filter_value == 'in_progress':
                todos = todos_collection.find({'user_id': user_id, 'status': 'in_progress'})
            elif filter_value == 'done':
                todos = todos_collection.find({'user_id': user_id, 'status': 'done'})
            else:
                todos = todos_collection.find({'user_id': user_id})
        #default display
        else:
            todos = todos_collection.find({'user_id': user_id})

        return render_template('view_all.html', todos=todos, filter_value=filter_value)
    
    # 6. Display a Single Task Route
    @app.route('/task/<todo_id>')
    def display_todo(todo_id):
        if 'user_id' not in session:
            return redirect(url_for('login'))

        todo = todos_collection.find_one({'_id': ObjectId(todo_id)})
        return render_template('display.html', todo=todo)
    
    # 7. Edit Task Route
    @app.route('/edit/<todo_id>', methods=['GET', 'POST'])
    def edit_todo(todo_id):
        if 'user_id' not in session:
            return redirect(url_for('login'))

        todo = todos_collection.find_one({'_id': ObjectId(todo_id)})

        if not todo:
            flash('Task not found!', 'danger')
            return redirect(url_for('view_all'))

        if request.method == 'POST':
            updated_task = {
                'list_title': request.form['list_title'],
                'time': request.form['time'],
                'todo_content': request.form['todo_content'],
                'status': request.form['status']
            }
            todos_collection.update_one({'_id': ObjectId(todo_id)}, {'$set': updated_task})
            flash('Task updated!', 'success')
            return redirect(url_for('view_all'))

        return render_template('edit.html', todo=todo)

    # 8. Delete Task Route
    @app.route('/delete/<todo_id>', methods=['POST'])
    def delete_todo(todo_id):
        if 'user_id' not in session:
            return redirect(url_for('login'))

        todos_collection.delete_one({'_id': ObjectId(todo_id), 'user_id': session['user_id']})
        flash('Task deleted!', 'info')
        return redirect(url_for('view_all'))

    # 9. Search Task Route
    @app.route('/search', methods=['GET', 'POST'])
    def search():
        if 'user_id' not in session:
            return redirect(url_for('login'))

        search_keyword = request.args.get('search_keyword', '')

        if search_keyword:
            search_results = todos_collection.find({
                'user_id': session['user_id'],
                'list_title': {'$regex': search_keyword, '$options': 'i'}
            })
        else:
            search_results = []

        return render_template('search.html', search_results=search_results, search_keyword=search_keyword)

    # 10. Logout
    @app.route('/logout')
    def logout():
        # Clear the user session
        session.clear()
        flash('You have been logged out.', 'info')
        return redirect(url_for('login'))
    
    if __name__ == '__main__':
        app = create_app()
        app.run(debug=True,port=3000)
        
    return app