from flask_sqlalchemy import SQLAlchemy

# from config import Config
# from flask_marshmallow import Marshmallow

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.String(8), primary_key=True)
    name = db.Column(db.String(255, collation="utf8mb4_unicode_ci"), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(20), nullable=False)

    def __init__(self, id, name, email, phone):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone


class Supplyment(db.Model):
    id = db.Column(db.String(8), primary_key=True)
    name = db.Column(db.String(255, collation="utf8mb4_unicode_ci"), nullable=False)
    availableOutside = db.Column(db.Integer, nullable=False)
