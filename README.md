# To-Do Reminder App

## Project Overview
This is a Django-based To-Do Reminder application that allows users to manage tasks with features like adding, editing, and deleting tasks. The backend uses Python Django and PostgreSQL for the database, while the application is deployed on Render.

## Features
- **Add a New To-Do Task**
  - Title, description, priority, due date, and completion status can be set
- **Display List of To-Do Tasks**
  - Tasks are displayed in order of priority and due date
- **Edit a To-Do Task**
  - Update any field of a task
- **Delete a Particular Task**
  - Remove a single task using its unique ID
- **Delete All Tasks**
  - Clear the entire list of tasks

## Tech Stack
- **Backend**: Python, Django
- **Database**: PostgreSQL
- **Hosting**: Render

## Setup and Installation

### 1. Clone the Repository
```bash
git clone https://github.com/harsh0c/todo_django.git
```

### 2. Install Dependencies
Ensure Python 3.10+ but not 3.13 is installed. Use the requirements.txt file to install dependencies:
```bash
   pip install -r requirements.txt
```

### 3. Configure Environment Variables
Create a .env file in the project root with the following: \
Configure `DATABASE_URL` if want to use PostgreSQL :
```env
SECRET_KEY=<your-django-secret-key>
DEBUG=True
DATABASE_URL=<your-render-postgresql-database-url>
ALLOWED_HOSTS=localhost,127.0.0.1,<your-render-app-url>
```

### 4. Apply Migrations
Initialize the database schema:
```bash
python manage.py migrate
```

### 5. Run the Server
Start the development server locally:
```bash
python manage.py runserver
```

### 6. Access the App
Visit http://127.0.0.1:8000/ to interact with the application.

## Running Tests
### 1. Run the Tests
Execute the test suite to ensure all functionalities work as expected:
```bash
python manage.py test
```

### 2. Testing with SQLite
The project is also configured to use SQLite when running tests. No additional setup is required. To run tests, uncomment the code in todo_app/settings.py and simply execute:
```bash
   python manage.py test
```

