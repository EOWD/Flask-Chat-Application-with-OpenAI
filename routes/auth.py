from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models.user import UserSchema
from flask_pymongo import PyMongo
import datetime
from flask_bcrypt import Bcrypt
# Initialize Blueprint
auth_bp = Blueprint('auth_bp', __name__)



# User Schema for validation
user_schema = UserSchema()

@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        # Validate and deserialize input
        data = user_schema.load(request.get_json())

        # Check if user exists in the database
        mongo_db = current_app.config['MONGO_DB']
        existing_user = mongo_db.users.find_one({'email': data['email']})
        user_id = str(existing_user['_id'])
        print(existing_user['_id'])

        if not existing_user:
            return jsonify({"msg": "User not found"}), 404

        # Verify password
        bcrypt = Bcrypt()
        if not bcrypt.check_password_hash(existing_user['password'], data['password']):
            return jsonify({"msg": "Password is incorrect"}), 401

        # Create JWT token
        expires = datetime.timedelta(days=1)
        access_token = create_access_token(identity=str(existing_user['_id']), expires_delta=expires)

        
        return jsonify({'access_token': access_token, 'id': user_id}), 200

    except Exception as e:
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500



@auth_bp.route('/verify', methods=['GET'])
@jwt_required()  # Requires a valid JWT token
def verify_token():
    try:
        # Get the identity (user ID) from the token
        current_user_id = get_jwt_identity()
        
        # If the token is valid, return success message along with the user ID
        return jsonify({'message': 'Token is valid', 'user_id': current_user_id}), 200

    except Exception as e:
        # If an error occurs, return an error message
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500