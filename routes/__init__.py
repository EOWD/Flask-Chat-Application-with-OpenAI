from flask import Blueprint
from .user_routes import user_bp
from .auth import auth_bp
from .fine_tuning import lm_bp
from .chat import chat_bp
def register_routes(app):
    app.register_blueprint(user_bp, url_prefix='/signup')
    app.register_blueprint(auth_bp, url_prefix='auth')
    app.register_blueprint(lm_bp, url_prefix='/fine_tuning')
    app.register_blueprint(chat_bp, url_prefix='/chat')
