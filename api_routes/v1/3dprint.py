from flask import jsonify, request
from . import api_v1

@api_v1.route('/3dprint/jobs', methods=['GET'])
def get_print_jobs():
    return jsonify({"message": "Get all print jobs"})

@api_v1.route('/3dprint/jobs', methods=['POST'])
def create_print_job():
    data = request.get_json()
    return jsonify({"message": "Create print job", "data": data}), 201

@api_v1.route('/3dprint/queue', methods=['GET'])
def get_print_queue():
    return jsonify({"message": "Get print queue"})
