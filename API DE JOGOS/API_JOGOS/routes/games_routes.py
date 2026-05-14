from flask import Blueprint, request, jsonify
from controllers.games_controller import (
    create_game,
    get_all_games,
    get_game_by_id,
    update_game
)

game_bp = Blueprint('game_bp', __name__)


@game_bp.route('/Games', methods=['POST'])
def add_game():
    data = request.get_json()
    result, status = create_game(data)
    return jsonify(result), status


@game_bp.route('/Games', methods=['GET'])
def list_games():
    result, status = get_all_games()
    return jsonify(result), status


@game_bp.route('/Games/<int:id>', methods=['GET'])
def get_game(id):
    result, status = get_game_by_id(id)
    return jsonify(result), status

@game_bp.route('/Games/<int:id>', methods=['PUT'])
def update_game_route(id):
    data = request.get_json()
    result, status = update_game(id, data)
    return jsonify(result), status