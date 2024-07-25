 

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship 
from sqlalchemy.sql import text

from app import db
from app import models

class User(db.Model, UserMixin):

    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    lastname2 = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(256), unique=True, nullable=False)
    local_phone = db.Column(db.String(10), nullable=True)
    mobile_phone = db.Column(db.String(10), nullable=True)
    key_elector = db.Column(db.String(28), nullable=True)
    status = db.Column(db.Integer, default=1)
    password = db.Column(db.String(256), nullable=False)
    rol_id = db.Column(db.Integer, db.ForeignKey('Rol.id', ondelete='CASCADE'), nullable=False)
    rol = relationship("Rol", lazy="joined", innerjoin=True)
    is_admin = db.Column(db.Boolean, default=False)

    def __init__(self, name, lastname,lastname2, email,local_phone,mobile_phone,key_elector,status,rol_id):
        self.name = name
        self.lastname = lastname
        self.lastname2 = lastname2
        self.email = email
        self.local_phone = local_phone
        self.mobile_phone = mobile_phone
        self.key_elector = key_elector
        self.status = status
        self.rol_id = rol_id

    def __repr__(self):
        return f'<User {self.email}>'

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_by_id(id):
        return User.query.get(id)

    @staticmethod
    def get_by_email(email):
        return User.query.filter_by(email=email).first()

    @staticmethod
    def get_all():
        return User.query.all()
    
    @staticmethod
    def all_paginated(page=1, per_page=10):
        session = db.session()
        cursor = session.execute(text("SELECT a.*, b.rol_name from User a inner join Rol b on a.rol_id = b.id ;"))
        results_as_dict = cursor.mappings().all()
        # return session.query(User, Rol).filter(Customer.id == Invoice.custid).all().\
        # return results_as_dict.\
        # return User.query.order_by(User.rol_id.asc()).\
        return User.query.join(models.Rol,User.rol_id==models.Rol.id).all().\
            paginate(page=page, per_page=per_page, error_out=False)
