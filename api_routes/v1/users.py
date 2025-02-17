from flask import jsonify, request
from . import api_v1

@api_v1.route('/users', methods=['GET'])
def get_users():
    return jsonify({"message": "Get all users"})

@api_v1.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return jsonify({"message": f"Get user {user_id}"})

@api_v1.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    return jsonify({"message": "Create user", "data": data}), 201

@api_v1.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    return jsonify({"message": f"Update user {user_id}", "data": data})

@api_v1.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    return jsonify({"message": f"Delete user {user_id}"}), 204
