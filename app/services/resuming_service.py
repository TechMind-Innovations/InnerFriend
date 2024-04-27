from ..extensions import db
from ..models.user import User
from ..models.resuming_talks import ResumingTalks

class ResumingTalkService:
    @staticmethod
    def create_resuming_talk(message, user_id ):
        user = User.query.filter_by(id = user_id).first()
        if user is None:
            raise ValueError("User not found!") 
        new_resuming_talk = ResumingTalks(
            message= message,
            user_id = user_id
        )
        db.session.add(new_resuming_talk)
        db.session.commit()
        return new_resuming_talk