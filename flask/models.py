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


class Reservation(db.Model):
    reservation_id = db.Column(db.String(8), primary_key=True,nullable=False, default='a')
    user_id = db.Column(db.String(8), primary_key=True)
    supplyment_id = db.Column(db.String(8), primary_key=True)
    start_date = db.Column(db.String(12), primary_key=True)
    start_time = db.Column(db.String(12), primary_key=True)
    return_date = db.Column(db.String(12), primary_key=True)
    return_time = db.Column(db.String(12), primary_key=True)
    reservation_date = db.Column(db.String(12), primary_key=True)


    def __init__(
            self, reservation_id,
            user_id,supplyment_id,
            start_date,start_time,
            return_date,return_time,
            reservation_date
            ):
        self.reservation_id = reservation_id
        self.user_id = user_id
        self.supplyment_id = supplyment_id
        self.start_date = start_date
        self.start_time = start_time
        self.return_date = return_date
        self.return_time = return_time
        self.reservation_date = reservation_date