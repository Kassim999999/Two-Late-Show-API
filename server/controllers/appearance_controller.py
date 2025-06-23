from flask import Blueprint, jsonify

appearance_bp = Blueprint('appearance_bp', __name__)

@appearance_bp.route('/appearances', methods=['POST'])
def create_appearance():
    return jsonify({"message": "Create appearance placeholder"}), 201
