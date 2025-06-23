from flask import Blueprint, jsonify

episode_bp = Blueprint('episode_bp', __name__)

@episode_bp.route('/episodes', methods=['GET'])
def get_episodes():
    return jsonify({"message": "Episodes route placeholder"}), 200

@episode_bp.route('/episodes/<int:id>', methods=['GET', 'DELETE'])
def episode_detail(id):
    return jsonify({"message": f"Episode {id} placeholder"}), 200
