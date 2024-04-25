from ..extensions import db
from sqlalchemy.sql import func

class ResumingTalks(db.Model):
    __tablename__ = 'resuming_talks'

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    updated_on = db.Column(db.DateTime(timezone=True), default=func.now(), onupdate=func.now())
    created_on = db.Column(db.DateTime(timezone=True), default=func.now())

    user = db.relationship('User', back_populates='resuming_talks')
