from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    "Task 1", 
    "Task 2", 
    "Task 3"
]

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/api/tasks', methods=['POST'])
def create_task():
    task = request.json['task']
    tasks.append(task)
    return jsonify({'message': 'Task created'})

@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    new_task = request.json['task']
    tasks[task_id] = new_task
    return jsonify({'message': 'Task updated'})

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    del tasks[task_id]
    return jsonify({'message': 'Task deleted'})

if __name__ == '__main__':
    app.run()
