from ..extensions import db
from ..models.user import User
from ..models.supporting_talks import SupportingTalks

class SupportingTalkService:
    @staticmethod
    def create_supporting_talk(message, user_id ):
        user = User.query.filter_by(id = user_id).first()
        if user is None:
            raise ValueError("User not found!") 
        new_supporting_talk = SupportingTalks(
            message= message,
            user_id = user_id
        )
        db.session.add(new_supporting_talk)
        db.session.commit()
        return new_supporting_talk