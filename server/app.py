from flask import Flask, jsonify, current_app
from dotenv import load_dotenv
import os
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from pymongo import MongoClient

# Load environment variables
load_dotenv()

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": os.getenv('ORIGIN')}}) 


app.config['JWT_SECRET_KEY'] = os.getenv('SECRET_KEY')

# MongoDB connection URI
mongo_uri = os.getenv('MONGODB_URI')

try:
    # Connect to MongoDB Atlas
    client = MongoClient(mongo_uri)
    db = client["Intellikaam"]  # Use the default database from the URI
    print("Connected to MongoDB Atlas!")

    # Set MongoDB client and database in the app configuration
    app.config['MONGO_CLIENT'] = client
    app.config['MONGO_DB'] = db

except Exception as e:
    print(f"Error connecting to MongoDB Atlas: {e}")

bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Import and register routes
from routes import register_routes
register_routes(app)

@app.route('/')
def home():
    return "Hello, Flask MongoDB "

if __name__ == '__main__':
    app.run(debug=True)
