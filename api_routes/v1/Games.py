from flask import jsonify, request
from . import api_v1

@api_v1.route('/games', methods=['GET'])
def get_games():
    return jsonify({"message": "Get all games"})

@api_v1.route('/games/<int:game_id>', methods=['GET'])
def get_game(game_id):
    return jsonify({"message": f"Get game {game_id}"})

@api_v1.route('/games/<int:game_id>/participants', methods=['GET'])
def get_game_participants(game_id):
    return jsonify({"message": f"Get participants of game {game_id}"})

@api_v1.route('/games/<int:game_id>/join', methods=['POST'])
def join_game(game_id):
    data = request.get_json()
    return jsonify({"message": f"Join game {game_id}", "data": data})
