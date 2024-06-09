from ..extensions import db
from ..models.user import User
from ..models.resuming_talks import ResumingTalks
from sqlalchemy import func

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
    
    @staticmethod
    def update_resuming_talks(id, data):
        resuming_talks = ResumingTalks.query.filter_by(id = id).first()

        if not resuming_talks:
            raise ValueError("Resuming_talks not found")

        for key, value in data.items():
            setattr(resuming_talks, key, value)

        db.session.commit()
        return resuming_talks
    
    def get_resuming_talks(user_id, created_on):
        supporting_talks = ResumingTalks.query.filter(
            ResumingTalks.user_id == user_id,
            func.date(ResumingTalks.created_on) == created_on
        ).first()
        if supporting_talks is None:
            raise ValueError("User does not have any supporting talks for the specified date")
        return supporting_talks
