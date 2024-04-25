from ..extensions import db
from sqlalchemy.sql import func

class UserPhoto(db.Model):
    __tablename__ = 'user_photo'

    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    photo = db.Column(db.LargeBinary, nullable=False)
    updated_on = db.Column(db.DateTime(timezone=True), default=func.now(), onupdate=func.now())
    created_on = db.Column(db.DateTime(timezone=True), default=func.now())

    user = db.relationship('User', back_populates='photos', uselist=False)
