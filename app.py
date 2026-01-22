from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory Task Database
tasks = [
    {"id": 1, "title": "Study SDLC", "description": "Read about Software Development Life Cycle", "isCompleted": True},
    {"id": 2, "title": "Complete Assignment", "description": "Implement Taskify API", "isCompleted": False}
]

# 1. GET /tasks - List all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

# 2. GET /tasks/<id> - Get a specific task
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(task)

# 3. POST /tasks - Create a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({"error": "Title is required"}), 400
    
    new_task = {
        "id": len(tasks) + 1,
        "title": data['title'],
        "description": data.get('description', ""),
        "isCompleted": False
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

# 4. PUT /tasks/<id> - Update a task
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    data = request.get_json()
    task['title'] = data.get('title', task['title'])
    task['description'] = data.get('description', task['description'])
    task['isCompleted'] = data.get('isCompleted', task['isCompleted'])

    return jsonify(task)


@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    tasks = [t for t in tasks if t["id"] != task_id]
    return jsonify(task)

if __name__ == '__main__':
    print("Task Manager API running at http://localhost:5000")
    app.run(port=5000, debug=True)
