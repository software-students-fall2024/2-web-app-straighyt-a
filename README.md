# Web Application Exercise

A little exercise to build a web application following an agile development process. See the [instructions](instructions.md) for more detail.

## Product vision statement

The To-Do List web application enables users to efficiently organize, manage, and track their tasks through a user-friendly interface, offering features like task creation, editing, filtering, and search to enhance productivity and streamline task management.

## User stories

- As a student, I want to be able to check my created to-do list so I can review my tasks easily. 
- As a student, I want to be able to add a new to-do list, with a title, time, and content so I can manage my deadlines and identify each task easily.
- As a user, I want to search for a specific task by their title, so I can easily find the task I am looking for, following with edition or deletion.
- As a user, I want to filter my to-do lists by "completed" or "pending" tasks so that I can quickly sort and view tasks based on their status, making it easier to track my progress and manage my workload efficiently.
- As a user, I want to edit my existing to-do lists so that I can modify task details and update deadlines as needed, ensuring my tasks are accurate and up-to-date.
- As a user, I want to delete tasks from my to-do lists so that I can remove irrelevant or completed items, keeping my lists clean and organized.

## Steps necessary to run the software

1. Install Python
Make sure Python 3.8 or higher is installed on your system. You can download it from python.org.

2. Clone the Repository
Download the project by cloning the GitHub repository or downloading the project files manually:

git clone https://github.com/software-students-fall2024/2-web-app-straighyt-a.git
cd YOUR_PROJECT_FOLDER

3. Set up a Virtual Environment
Run the following commands to create and activate the virtual environment:

python3 -m venv venv

Activate the virtual environment:

On Windows:
.\venv\Scripts\activate

On macOS/Linux:
source venv/bin/activate

4. Install Dependencies
Use the requirements.txt file to install the necessary Python libraries:

pip install -r requirements.txt

5. Set up Environment Variables
Create a .env file in the root directory of your project and add the following variables:

MONGO_DBNAME=todo_db
MONGO_URI=mongodb+srv://zl3927:PKXFzrHguY8QDwd6@cluster0.tem8w.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
FLASK_APP=app.py
FLASK_ENV=development
Note: Replace <username> and <password> with your MongoDB Atlas credentials.


6. Run MongoDB (if using Docker)
If you’re running MongoDB locally using Docker, start the MongoDB container:

docker run --name my-mongo -d -p 27017:27017 mongo:latest

7. Run the Flask Application
In the terminal (with the virtual environment activated), run:

python app.py

8. Access the Application
Open a web browser and go to:

http://127.0.0.1:5000/
This will take you to the login page.

9. Deactivate the Virtual Environment (Optional)
When you are finished, deactivate the virtual environment by typing:

deactivate

10. Troubleshooting Tips
If MongoDB is running on Atlas, ensure that the IP address whitelist includes 0.0.0.0/0 or your current IP.
If using local MongoDB, ensure the server is running:

sudo systemctl start mongod  # Linux
brew services start mongodb-community  # macOS with Homebrew

## Task boards

1. Sprint 1 https://github.com/orgs/software-students-fall2024/projects/51/views/1
2. Sprint 2 https://github.com/orgs/software-students-fall2024/projects/80