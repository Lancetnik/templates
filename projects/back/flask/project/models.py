from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.inspection import inspect

db = SQLAlchemy()


class SerializerMixin():
    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]


class SomeModel(db.Model, SerializerMixin):
    name = db.Column(db.String(80), primary_key=True)

    def __repr__(self):
        return self.name