from flask_jwt_extended import create_access_token
from ..models.user import User

class AuthService:
    @staticmethod
    def authenticate_user(email, password):
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            token = create_access_token(identity=user.id)
            return {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "token": token
            }
        else:
            raise Exception("Invalid credentials")
