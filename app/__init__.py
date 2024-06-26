from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
import os
from dotenv import load_dotenv
import logging
from .extensions import db, bcrypt, jwt
from datetime import timedelta


logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

def create_app():
    app = Flask(__name__)
    load_dotenv()
    app.secret_key = 'wisley'
    CORS(app)

    print("DATABASE_URL:", os.getenv('DATABASE_URL'))
    print("OPENAI_API_KEY:", os.getenv('OPENAI_API_KEY'))

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=30)

    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    Migrate(app, db)

    with app.app_context():
        # Importação de modelos
        from .models.user import User
        from .models.ia_friend import IA_Friend
        from .models.resuming_talks import ResumingTalks
        from .models.supporting_talks import SupportingTalks
        from .models.user_photo import UserPhoto
        
    from .routes import user_bp, ia_friend_bp, supporting_talks_bp, resuming_talks_bp, chatbot_bp
    app.register_blueprint(user_bp, url_prefix='/user')
    app.register_blueprint(ia_friend_bp, url_prefix='/ia_friend')
    app.register_blueprint(supporting_talks_bp, url_prefix='/supporting_talks')
    app.register_blueprint(resuming_talks_bp, url_prefix='/resuming_talks')
    app.register_blueprint(chatbot_bp, url_prefix='/chatGPT')

    return app
