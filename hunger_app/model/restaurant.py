# -*- coding: utf-8 -*-
from hunger_app import db
from hunger_app.model.base import Base


class Restaurant(Base):
    __tablename__ = 'restaurant'

    contact_person_name = db.Column(db.String, nullable=True)
    restaurant_name = db.Column(db.String, nullable=True)
    phone = db.Column(db.String, nullable=True)
    city = db.Column(db.String, nullable=True)
    country = db.Column(db.String, nullable=True)
    address = db.Column(db.String, nullable=True)
    serving_per_person = db.Column(db.Integer, nullable=False)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<collection %r>' % self.restaurant_name