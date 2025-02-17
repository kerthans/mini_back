from flask import jsonify, request
from . import api_v1

@api_v1.route('/stuff', methods=['GET'])
def get_stuff_list():
    return jsonify({"message": "Get all stuff"})

@api_v1.route('/stuff/<int:stuff_id>', methods=['GET'])
def get_stuff(stuff_id):
    return jsonify({"message": f"Get stuff {stuff_id}"})

@api_v1.route('/stuff', methods=['POST'])
def add_stuff():
    data = request.get_json()
    return jsonify({"message": "Add new stuff", "data": data}), 201

@api_v1.route('/stuff/categories', methods=['GET'])
def get_stuff_categories():
    return jsonify({"message": "Get stuff categories"})
