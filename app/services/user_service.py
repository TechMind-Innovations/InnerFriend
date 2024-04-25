from ..extensions import db, bcrypt 
from ..models.user import User
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token

class UserService:
    @staticmethod
    def create_user(name, social_name, year, email, password, sex, region):
        if User.query.filter_by(email=email).first():
            raise ValueError("Email already exists!")
        password_hash = bcrypt.generate_password_hash(password).decode('utf-8')  # Correção aqui
        new_user = User(
            name=name,
            social_name=social_name,
            year=year,
            email=email,
            password=password_hash,  # Use o hash
            sex=sex,
            region=region
        )
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @staticmethod
    def authenticate_user(email, password):
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            token = create_access_token(identity=user.id)
            return {"token": token, "id": user.id, "name": user.name, "email": user.email}
        else:
            raise ValueError("Invalid credentials")

    @staticmethod
    def get_user_details(user_id):
        user = User.query.get(user_id)
        if not user:
            raise ValueError("User not found")
        return user
