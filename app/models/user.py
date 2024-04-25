# models/user.py
from sqlalchemy import Column, Integer, String, DateTime, Enum
from enum import Enum as PyEnum
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from ..extensions import db, bcrypt

class SexEnum(PyEnum):
    Male = "Male"
    Female = "Female"
    Other = "Other"

class User(db.Model):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    social_name = Column(String(255))
    year = Column(Integer)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    sex = Column(Enum(SexEnum), nullable=False)
    region = Column(String(255))
    created_on = Column(DateTime(timezone=True), server_default=func.now())
    updated_on = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # Definições de relacionamento
    ia_friends = relationship('IA_Friend', back_populates='user', cascade="all, delete-orphan")
    supporting_talks = relationship('SupportingTalks', back_populates='user', cascade="all, delete-orphan")
    resuming_talks = relationship('ResumingTalks', back_populates='user', cascade="all, delete-orphan")
    photos = relationship('UserPhoto', back_populates='user', uselist=False)
    
    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "sex": self.sex.value,  # Asumindo que sex é um enum e você quer retornar o valor
            "region": self.region,
            "social_name": self.social_name,
            "year": self.year
        }

