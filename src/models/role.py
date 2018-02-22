"""
Role Model
"""

from .__include__ import *

class Role(db.Model):
    """
    Roles Table
    """
    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), unique = True)
    description = db.Column(db.String(200))
    users = db.relationship("User", backref="role", lazy="dynamic")

    def __init__(self, **kwargs):
        self.name = kwargs.get("name", "Administrator")
        self.description = kwargs.get("description", None)

    @property
    def as_dict(self):
        result = dict()
        result["id"] = self.id
        result["name"] = self.name
        result["description"] = self.description

        return result

    def __repr__(self):
        return '<Role({0}): {1}>'.format(self.id, self.name)
