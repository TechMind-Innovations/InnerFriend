from ..extensions import db, bcrypt 
from ..models.user import User
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token

def adjust_sex(sex):
    if sex.lower() == 'female':
        sex = 'Female'
    elif sex.lower() == 'male':
        sex = 'Male'
    elif sex.lower() == 'other':
        sex = 'Other'
    return sex

class UserService:
    @staticmethod
    def create_user(name, social_name, year, email, password, sex, region):
        if User.query.filter_by(email=email).first():
            raise ValueError("Email already exists!")
        sex = adjust_sex(sex)
        
        password_hash = bcrypt.generate_password_hash(password).decode('utf-8')  
        new_user = User(
            name=name,
            social_name=social_name,
            year=year,
            email=email,
            password=password_hash,  
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
    
    @staticmethod
    def update_user(user_id, data):
        
        user = User.query.get(user_id)
        if not user:
            raise ValueError("User not found")

        for key, value in data.items():
            setattr(user, key, value)

        db.session.commit()
        return user
