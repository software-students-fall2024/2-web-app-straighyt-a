import os
from flask import Flask, render_template, request, redirect, url_for, flash, session
import pymongo
from bson.objectid import ObjectId
from dotenv import load_dotenv

load_dotenv()  # load environment variables from .env file

def create_app():
    """
    Create and configure the Flask application.
    returns: app: the Flask application object
    """

    app = Flask(__name__)

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
