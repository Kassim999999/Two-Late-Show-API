from flask import Blueprint, jsonify

guest_bp = Blueprint('guest_bp', __name__)

@guest_bp.route('/guests', methods=['GET'])
def get_guests():
    return jsonify({"message": "Guests route placeholder"}), 200
