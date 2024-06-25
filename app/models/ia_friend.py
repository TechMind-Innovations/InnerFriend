from ..extensions import db
from sqlalchemy import Column, Enum
from enum import Enum as PyEnum

class SexEnumIA(PyEnum):
    Male = "Male"
    Female = "Female"
    Other = "Other"

class IA_Friend(db.Model):
    __tablename__ = 'ia_friends'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    sex_ia = Column(Enum(SexEnumIA), nullable=False)
    age_average = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    photo = db.Column(db.String(255), nullable=True)
    user = db.relationship('User', back_populates='ia_friends')
