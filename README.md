# Task Manager API (SEN Assignment)



=======
## Student Information

- **Name**: Adebayo Stephen Oluwadamilola
- **Matric No**: 23/12018

---


 Full SDLC Documentation

 1. Planning
We identified the need for a simple system to manage tasks. The scope was limited to a RESTful API with CRUD capabilities to demonstrate core backend principles.

 2. Analysis
=======
## Full SDLC Documentation

### 1. Planning
We identified the need for a simple system to manage tasks. The scope was limited to a RESTful API with CRUD capabilities to demonstrate core backend principles.

### 2. Analysis

Requirement analysis identified the following:
- **Functional**: Create, Read, Update, and Delete tasks.
- **Data**: Tasks need a title, description, and completion status.


 3. Design
=======
### 3. Design

The system uses **Python** with the **Flask** microframework.
- **Nomenclature**:
    - `tasks`: List to store task dictionaries.
    - `id`: Unique identifier for each task.
    - `title`: The name of the task.
    - `isCompleted`: Boolean status.
- **Endpoints**:
    - `GET /tasks`
    - `POST /tasks`
    - `PUT /tasks/<id>`
    - `DELETE /tasks/<id>`


 4. Implementation
The project was implemented in a single file `app.py` utilizing Flask. In-memory storage was used to keep it lightweight and easy to run.

 5. Testing
Manual verification was performed using API-based tools (like curl or browser) to ensure all routes return the expected JSON data and status codes (200, 201, 404).

 6. Deployment
=======
### 4. Implementation
The project was implemented in a single file `app.py` utilizing Flask. In-memory storage was used to keep it lightweight and easy to run.

### 5. Testing
Manual verification was performed using API-based tools (like curl or browser) to ensure all routes return the expected JSON data and status codes (200, 201, 404).

### 6. Deployment

The project is initialized as a repository in the `Adebayo Stephen Oluwadamilola` folder and ready for GitHub.

---


 How to Run
=======
## How to Run


1. **Install Python** (if not already installed).
2. **Install Flask**:
   ```bash
   pip install flask
   ```
3. **Run the Application**:

   `bash
=======
   ```bash

   python app.py
   ```
4. **Test the API**:
   - Open your browser or use curl to visit `http://localhost:5000/tasks`.
   ** THANK YOUUUUUUUU **
