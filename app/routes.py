from flask import Blueprint
from .controllers.user_controller import UserController
from .controllers.ia_friend_controller import IA_FriendController
from flask_jwt_extended import jwt_required

#User
user_bp = Blueprint('user_bp', __name__)
user_controller = UserController()
#Ia_Friend
ia_friend_bp = Blueprint('ia_friend_bp', __name__)
ia_friend_controller = IA_FriendController()

#/user
@user_bp.route('/create', methods=['POST'])
def create_user():
    return user_controller.create_user()

@user_bp.route('/update', methods=['PUT'])
def update_user():
    return user_controller.update_user()


@user_bp.route('/session', methods=['POST'])
def auth_user():
    return user_controller.auth_user()

@user_bp.route('/me', methods=['GET'])
@jwt_required()
def detail_user():
    return user_controller.detail_user()

#/ia_friend
@ia_friend_bp.route('/create', methods=['POST'])
@jwt_required()
def create_ia_friend():
    return ia_friend_controller.create_ia_friend()

#/resuming_talks
