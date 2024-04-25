from flask import Blueprint
from .controllers.user_controller import UserController
from flask_jwt_extended import jwt_required

user_bp = Blueprint('user_bp', __name__)
user_controller = UserController()

@user_bp.route('/users', methods=['POST'])
def create_user():
    return user_controller.create_user()

@user_bp.route('/session', methods=['POST'])
def auth_user():
    return user_controller.auth_user()

@user_bp.route('/me', methods=['GET'])
@jwt_required()
def detail_user():
    return user_controller.detail_user()
