from utils.db import db
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

class User(db.Model,UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key=True)
    Name = db.Column(db.String(100),nullable=False)
    Password = db.Column(db.String(255),nullable=False)
    Rut = db.Column(db.String(100),nullable=False, unique=True)
    Email = db.Column(db.String(255),nullable=False, unique=True)
    Type = db.Column(db.String(100),nullable=False)

    def __init__(self, name, password, rut, email, type):
        self.Name = name
        self.Password = generate_password_hash(password)
        self.Rut = rut
        self.Email = email
        self.Type = type

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()
        db.session.flush()

    @staticmethod
    def get_by_id(id):
        return User.query.get(id)

    @staticmethod
    def get_by_rut(rut):
        return User.query.filter_by(Rut=rut).first()

    @staticmethod
    def get_by_email(email):
        return User.query.filter_by(Email=email).first()

    def delete_user(self):
        db.session.delete(self)
        db.session.commit()
        db.session.flush()

    def set_password(self,password):
        self.Password = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.Password,password)

    def __repr__(self):
        return "<User {}>".format(self.Rut)