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
            user = UserService.get_user_details(user_id)
            return jsonify(user.serialize()), 200  # Usando o método serialize aqui
        except Exception as e:
            return jsonify({"error": str(e)}), 404

