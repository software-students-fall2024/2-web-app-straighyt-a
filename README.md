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

1. **Install Python**:
   - Make sure Python 3.8 or higher is installed on your system. You can download it from python.org.

2. **Clone the repository**:
   - Run the following commands to create and activate the virtual environment:
     ```bash
     git clone https://github.com/software-students-fall2024/2-web-app-straighyt-a.git
     cd your-repository-folder
     ```

3. **Set up a Virtual Environment**:
   - Run the following commands to create and activate the virtual environment:
     ```bash
     python3 -m venv venv
     ```
   - Activate the virtual environment:
     - On Windows:
       ```bash
       .\venv\Scripts\activate
       ```
     - On macOS/Linux:
       ```bash
       source venv/bin/activate
       ```

4. **Install Dependencies**:
   - Use the `requirements.txt` file to install the necessary Python libraries:
     ```bash
     pip install -r requirements.txt
     ```

5. **Set up Environment Variables**:
   - Create a `.env` file in the root directory of your project and add the following variables:
     ```env
     MONGO_DBNAME=todo_db
     MONGO_URI=mongodb://localhost:27017/todo_db
     #MONGO_URI=mongodb+srv://zl3927:PKXFzrHguY8QDwd6@cluster0.tem8w.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
     FLASK_APP=app.py
     FLASK_ENV=development
     FLASK_PORT=3000
     ```

6. Run MongoDB (if using Docker)
   - If you’re running MongoDB locally using Docker, start the MongoDB container:
   ```bash
   docker run --name my-mongo -d -p 27017:27017 mongo:latest
   ```
   - If any container has name conflicts (my-mongo):
      - stop the old containter by:
      ```bash
      docker stop my-mongo
      ```
      - After stopping, remove it with:
      ```bash
      docker rm my-mongo
      ```
      - Then start the MongoDB container.
7. Run the Flask Application
   - In the terminal (with the virtual environment activated), run: 
   ```bash
   python app.py
   ```
   - or using Flask if above command not working:
    ```bash
   flask run --port=3000
   ```

8. Access the Application
   - Open a web browser and go to `http://127.0.0.1:3000/` 
   This will take you to the login page.

9. Deactivate the Virtual Environment (Optional)
   - When finished, deactivate the virtual environment by typing:
     ```bash
     deactivate
     ```

10. Troubleshooting Tips
If MongoDB is running on Atlas, ensure that the IP address whitelist includes 0.0.0.0/0 or your current IP.
If using local MongoDB, ensure the server is running:

sudo systemctl start mongod  # Linux
brew services start mongodb-community  # macOS with Homebrew

## Task boards

1. **Sprint 1** [Task Boards](https://github.com/orgs/software-students-fall2024/projects/51/views/1)
2. **Sprint 2** [Task Boards](https://github.com/orgs/software-students-fall2024/projects/80)