from flask import jsonify, request
from . import api_v1

@api_v1.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"message": "Get all tasks"})

@api_v1.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    return jsonify({"message": f"Get task {task_id}"})

@api_v1.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    return jsonify({"message": "Create task", "data": data}), 201

@api_v1.route('/tasks/<int:task_id>/status', methods=['PUT'])
def update_task_status(task_id):
    data = request.get_json()
    return jsonify({"message": f"Update task {task_id} status", "data": data})
