from flask import Blueprint, request, jsonify, current_app
from flask_bcrypt import Bcrypt
from models.user import UserSchema
from marshmallow import ValidationError
from pymongo.errors import DuplicateKeyError

user_bp = Blueprint('user_bp', __name__)

# Initialize Bcrypt
bcrypt = Bcrypt()

# User Schema for validation
user_schema = UserSchema()

@user_bp.route('/signup', methods=['POST'])
def signup():
    try:
        # Validate and deserialize input
        data = user_schema.load(request.get_json())

        # Retrieve MongoDB client and database from current app context
        mongo_client = current_app.config['MONGO_CLIENT']
        mongo_db = current_app.config['MONGO_DB']

        # Check if the user already exists
        existing_user = mongo_db.users.find_one({'email': data['email']})
        if existing_user:
            return jsonify({'message': 'User already exists'}), 400

        # Hash the password
        hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
        data['password'] = hashed_password

        # Insert the user document into the database
        result = mongo_db.users.insert_one(data)
        user_id = str(result.inserted_id)

        return jsonify({'message': 'User created successfully', 'user_id': user_id}), 201

    except ValidationError as err:
        return jsonify(err.messages), 400

    except DuplicateKeyError:
        return jsonify({'message': 'User with this email already exists'}), 400
