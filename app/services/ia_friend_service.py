from ..extensions import db
from ..models.ia_friend import IA_Friend
from ..models.user import User
from ..services.user_service import adjust_sex

class IA_FriendService:
    @staticmethod
    def create_ia_friend(name, sex_ia, age_average, user_id): 
        user = User.query.filter_by(id=user_id).first()
        ia_friend = IA_Friend.query.filter_by(user_id=user_id).first()

        if user is None:
            raise ValueError("User not found!")   

        if ia_friend is None:
            ia_friend = IA_Friend(
                name=name,
                sex_ia=adjust_sex(sex_ia),
                age_average=age_average,
                user_id=user_id
            )
            db.session.add(ia_friend)
        else:
            ia_friend.name = name
            ia_friend.sex_ia = adjust_sex(sex_ia)
            ia_friend.age_average = age_average

        db.session.commit()
        return ia_friend

    @staticmethod
    def update_ia_friend(user_id, data):
        ia_friend = IA_Friend.query.filter_by(user_id = user_id).first()

        if not ia_friend:
            raise ValueError("User not has IA_Friend")

        for key, value in data.items():
            setattr(ia_friend, key, value)

        db.session.commit()
        return ia_friend
    
    @staticmethod
    def get_ia_friend(user_id):
        ia_friend = IA_Friend.query.filter_by(user_id=user_id).first()
        if ia_friend is None:
            raise ValueError("User does not have an IA_Friend")
        return ia_friend
