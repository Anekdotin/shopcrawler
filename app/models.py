# coding=utf-8
from app import db
from datetime import datetime


class Nvidia3060(db.Model):
    __tablename__ = 'nvidia3600'
    __bind_key__ = 'cardchecker'
    __table_args__ = {"schema": "public", 'useexisting': True}

    id = db.Column(db.Integer, primary_key=True)
    # amazon, newegg, etc
    seller = db.Column(db.INTEGER)
    # url of item
    url = db.Column(db.TEXT)
    # sold out or in stock
    status = db.Column(db.INTEGER)
    # last seen in stock
    last_available = db.Column(db.TIMESTAMP())
    # total times seen
    total_times_seen = db.Column(db.INTEGER)

    msrp = db.Column(db.DECIMAL(20, 2))
    asking = db.Column(db.DECIMAL(20, 2))


class Nvidia3070(db.Model):
    __tablename__ = 'nvidia3700'
    __bind_key__ = 'cardchecker'
    __table_args__ = {"schema": "public", 'useexisting': True}

    id = db.Column(db.Integer, primary_key=True)
    # amazon, newegg, etc
    seller = db.Column(db.INTEGER)
    # url of item
    url = db.Column(db.TEXT)
    # sold out or in stock
    status = db.Column(db.INTEGER)
    # last seen in stock
    last_available = db.Column(db.TIMESTAMP())
    # total times seen
    total_times_seen = db.Column(db.INTEGER)

    msrp = db.Column(db.DECIMAL(20, 2))
    asking = db.Column(db.DECIMAL(20, 2))


class Nvidia3080(db.Model):
    __tablename__ = 'nvidia3800'
    __bind_key__ = 'cardchecker'
    __table_args__ = {"schema": "public", 'useexisting': True}

    id = db.Column(db.Integer, primary_key=True)
    # amazon, newegg, etc
    seller = db.Column(db.INTEGER)
    # url of item
    url = db.Column(db.TEXT)
    # sold out or in stock
    status = db.Column(db.INTEGER)
    # last seen in stock
    last_available = db.Column(db.TIMESTAMP())
    # total times seen
    total_times_seen = db.Column(db.INTEGER)

    msrp = db.Column(db.DECIMAL(20, 2))
    asking = db.Column(db.DECIMAL(20, 2))


class Nvidia3090(db.Model):
    __tablename__ = 'nvidia3900'
    __bind_key__ = 'cardchecker'
    __table_args__ = {"schema": "public", 'useexisting': True}

    id = db.Column(db.Integer, primary_key=True)
    # amazon, newegg, etc
    seller = db.Column(db.INTEGER)
    # url of item
    url = db.Column(db.TEXT)
    # sold out or in stock
    status = db.Column(db.INTEGER)
    # last seen in stock
    last_available = db.Column(db.TIMESTAMP())
    # total times seen
    total_times_seen = db.Column(db.INTEGER)

    msrp = db.Column(db.DECIMAL(20, 2))
    asking = db.Column(db.DECIMAL(20, 2))


db.configure_mappers()
db.create_all()
db.session.commit()