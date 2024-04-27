from ..extensions import db
from ..models.ia_friend import IA_Friend
from ..models.user import User

class IA_FriendService:
    @staticmethod
    def create_ia_friend(name, sex_ia, age_average, user_id):    
        user = User.query.filter_by(id = user_id).first()
        ia_friend_Exist = IA_Friend.query.filter_by(user_id = user_id).first()
        if user is None:
            raise ValueError("User not found!")   
        if ia_friend_Exist != None:
            raise ValueError("User already has IA friend!")   
        new_ia = IA_Friend(
            name = name,
            sex_ia = sex_ia,
            age_average = age_average,
            user_id = user_id

        )
        db.session.add(new_ia)
        db.session.commit()
        return new_ia