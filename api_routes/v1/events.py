from flask import jsonify, request
from . import api_v1

@api_v1.route('/events', methods=['GET'])
def get_events():
    return jsonify({"message": "Get all events"})

@api_v1.route('/events/<int:event_id>', methods=['GET'])
def get_event(event_id):
    return jsonify({"message": f"Get event {event_id}"})

@api_v1.route('/events', methods=['POST'])
def create_event():
    data = request.get_json()
    return jsonify({"message": "Create event", "data": data}), 201
