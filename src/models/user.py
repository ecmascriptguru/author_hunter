"""
User model
"""

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from .__include__ import db
from src import login_manager

class User(UserMixin, db.Model):
    """
    Users Table
    """
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(60), index = True, unique = True)
    username = db.Column(db.String(60), index = True, unique = True)
    first_name = db.Column(db.String(40))
    last_name = db.Column(db.String(40))
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    is_admin = db.Column(db.Boolean, default = False)

    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    @property
    def as_dict(self):
        result = dict()
        result["id"] = self.id
        result["first_name"] = self.first_name
        result["last_name"] = self.last_name
        result["email"] = self.email
        result["is_admin"] = self.is_admin
        result["role"] = self.role.as_dict if self.role else None

        return result

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name

    @full_name.setter
    def full_name(self, full_name):
        [first_name, last_name] = full_name.split(" ")
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return '<User: {}>'.format(self.username)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
