from flask_pymongo import PyMongo

db = PyMongo()  # No need to call init_app here

# Function to initialize PyMongo with app context (if needed)
def get_db():
    return db

