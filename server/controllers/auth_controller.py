from flask import Blueprint, request, jsonify

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    return jsonify({"message": "Register route placeholder"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    return jsonify({"message": "Login route placeholder"}), 200
