from flask import jsonify, request
from . import api_v1

@api_v1.route('/rules', methods=['GET'])
def get_rules():
    return jsonify({"message": "Get all rules"})

@api_v1.route('/rules/<int:rule_id>', methods=['GET'])
def get_rule(rule_id):
    return jsonify({"message": f"Get rule {rule_id}"})

@api_v1.route('/rules', methods=['POST'])
def create_rule():
    data = request.get_json()
    return jsonify({"message": "Create rule", "data": data}), 201
