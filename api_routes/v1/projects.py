from flask import jsonify, request
from . import api_v1

@api_v1.route('/projects', methods=['GET'])
def get_projects():
    return jsonify({"message": "Get all projects"})

@api_v1.route('/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    return jsonify({"message": f"Get project {project_id}"})

@api_v1.route('/projects', methods=['POST'])
def create_project():
    data = request.get_json()
    return jsonify({"message": "Create project", "data": data}), 201

@api_v1.route('/projects/<int:project_id>/members', methods=['GET'])
def get_project_members(project_id):
    return jsonify({"message": f"Get members of project {project_id}"})
