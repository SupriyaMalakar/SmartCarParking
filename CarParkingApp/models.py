from datetime import datetime
from CarParkingApp import db


class User(db.Model):
   
    email = db.Column(db.String(120), unique=True, nullable=False)
    Phone_Number = db.Column(db.String(10), unique=True, nullable=False)
    Car_Number = db.Column(db.String(11), unique=True, nullable=False,primary_key=True)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    ParkingLot = db.relationship('ParkingLot', backref='Owner', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class ParkingLot(db.Model):
    ParkingLot_id = db.Column(db.Integer, primary_key=True)
    ParkingLot_name = db.Column(db.String(100), nullable=False)
    Entry_Time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    Exit_Time = db.Column(db.DateTime, nullable=True)
    Car_Number = db.Column(db.String(11), db.ForeignKey('user.Car_Number'), nullable=False)

    def __repr__(self):
        return f"Post('{self.Car_Number}', '{self.Entry_Time}')"