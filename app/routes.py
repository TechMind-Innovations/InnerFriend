from flask import Blueprint
from .controllers.user_controller import UserController
from .controllers.ia_friend_controller import IA_FriendController
from .controllers.resuming_controller import ResumingTalkController
from .controllers.supporting_controller import SupportingTalkController
from flask_jwt_extended import jwt_required

#User
user_bp = Blueprint('user_bp', __name__)
user_controller = UserController()
#Ia_Friend
ia_friend_bp = Blueprint('ia_friend_bp', __name__)
ia_friend_controller = IA_FriendController()
#resuming_talks
resuming_talks_bp = Blueprint('resuming_talks_bp', __name__)
resuming_talks_controller = ResumingTalkController()
#supporintg_talks
supporting_talks_bp = Blueprint('supporting_talks_bp', __name__)
supporting_talks_controller = SupportingTalkController()

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

@user_bp.route('/upsert_photo', methods=['POST'])
@jwt_required()
def upsert_photo():
    return user_controller.upsert_photo()

#/ia_friend
@ia_friend_bp.route('/create', methods=['POST'])
@jwt_required()
def create_ia_friend():
    return ia_friend_controller.create_ia_friend()

@ia_friend_bp.route('/update', methods=['PUT'])
@jwt_required()
def update_ia_friend():
    return ia_friend_controller.update_ia_friend()

@ia_friend_bp.route('/getIA', methods=['GET'])
@jwt_required()
def get_ia_friend():
    return ia_friend_controller.get_ia_friend()

#/resuming_talks
@resuming_talks_bp.route('/create', methods=['POST'])
@jwt_required()
def create_resuming_talks():
    return resuming_talks_controller.create_resuming_talks()

@resuming_talks_bp.route('/update', methods=['PUT'])
@jwt_required()
def update_resuming_talks():
    return resuming_talks_controller.update_resuming_talks()

@resuming_talks_bp.route('/get', methods=['GET'])
@jwt_required()
def get_resuming_talks():
    return resuming_talks_controller.get_resumingTalks()

#/supporting_talks
@supporting_talks_bp.route('/create', methods=['POST'])
@jwt_required()
def create_supporting_talks():
    return supporting_talks_controller.create_supporting_talks()

@supporting_talks_bp.route('/update', methods=['PUT'])
@jwt_required()
def update_supporting_talks():
    return supporting_talks_controller.update_supporting_talks()

@supporting_talks_bp.route('/get', methods=['GET'])
@jwt_required()
def get_supporting_talks():
    return supporting_talks_controller.get_supportingTalks()
