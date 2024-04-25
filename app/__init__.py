# __init__.py
from flask import Flask
from flask_migrate import Migrate
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

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=2)

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
        
    from .routes import user_bp
    app.register_blueprint(user_bp, url_prefix='/inner-friend')

    return app
