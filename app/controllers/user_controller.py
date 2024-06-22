from flask import request, jsonify
from ..services.user_service import UserService
from flask_jwt_extended import get_jwt_identity
from ..services.auth_service import AuthService

class UserController:
    def create_user(self):
        data = request.get_json()
        try:
            user = UserService.create_user(
                name=data['name'],
                social_name=data.get('social_name', None),
                year=data.get('year', None),
                email=data['email'],
                password=data['password'],
                sex=data['sex'],
                region=data.get('region', None)
            )
            return jsonify({"id": user.id, "name": user.name, "email": user.email}), 201
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except KeyError as e:
            return jsonify({"error": f"Missing field: {str(e)}"}), 400
        except Exception as e:
            return jsonify({"error": "Server error"}), 500

    def auth_user(self):
        data = request.get_json()
        try:
            auth_data = AuthService.authenticate_user(data['email'], data['password'])
            return jsonify(auth_data), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 401
        
    def detail_user(self):
        user_id = get_jwt_identity()
        try:
            user_data = UserService.get_user_details(user_id)
            return jsonify(user_data), 200 
        except Exception as e:
            return jsonify({"error": str(e)}), 404
        
    def update_user(self):
        user_id = get_jwt_identity()
        data = request.get_json()
        data.pop('password', None)
        try:
            updated_user = UserService.update_user(user_id, data)
            return jsonify({"id": updated_user.id, "name": updated_user.name, "email": updated_user.email}), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": "Server error"}), 500
        
    def upsert_photo(self):
            user_id = get_jwt_identity()
            photo_data = request.files['photo'].read()  # Assumindo que a foto é enviada como um arquivo

            try:
                updated_photo = UserService.upsert_photo(user_id, photo_data)
                return jsonify({"id": updated_photo.id, "user_id": updated_photo.id, "updated_on": updated_photo.updated_on}), 200
            except ValueError as e:
                return jsonify({"error": str(e)}), 400
            except Exception as e:
                return jsonify({"error": "Server error"}), 500
