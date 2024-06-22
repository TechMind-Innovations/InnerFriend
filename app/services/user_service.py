from ..extensions import db, bcrypt 
from ..models.user import User
from ..models.user_photo import UserPhoto
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token
import base64

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
        userPhoto = UserPhoto.query.filter_by(id=user_id).first()
        if not user:
            raise ValueError("User not found")
        user_data = {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "sex": user.sex.value,  # Assumindo que sex é um enum e você quer retornar o valor
            "region": user.region,
            "social_name": user.social_name,
            "year": user.year,
            "photo": base64.b64encode(userPhoto.photo).decode('utf-8') if userPhoto else None
        }
        return user_data
    
    
    @staticmethod
    def update_user(user_id, data):
        user = User.query.get(user_id)
        if not user:
            raise ValueError("User not found")

        for key, value in data.items():
            setattr(user, key, value)

        db.session.commit()
        return user

    @staticmethod
    def upsert_photo(user_id, photo_data):
            # Verificar se o usuário existe
            user = User.query.get(user_id)
            if not user:
                raise ValueError("User not found")

            # Tente encontrar a foto existente com base no user_id
            photo = UserPhoto.query.filter_by(id=user_id).first()
            if photo:
                # Atualizar os dados binários da foto existente
                photo.photo = photo_data
            else:
                # Criar uma nova foto se não houver uma existente
                photo = UserPhoto(id=user_id, photo=photo_data)
                db.session.add(photo)

            # Commit das mudanças no banco de dados
            db.session.commit()
            return photo
