from flask import jsonify, request
from . import api_v1

@api_v1.route('/stuff-borrow', methods=['GET'])
def get_borrow_records():
    return jsonify({"message": "Get all borrow records"})

@api_v1.route('/stuff-borrow', methods=['POST'])
def create_borrow_record():
    data = request.get_json()
    return jsonify({"message": "Create borrow record", "data": data}), 201

@api_v1.route('/stuff-borrow/<int:record_id>/return', methods=['PUT'])
def return_stuff(record_id):
    return jsonify({"message": f"Return stuff for record {record_id}"})
