import os
from sqlalchemy import Column, String, create_engine, Integer
from flask_sqlalchemy import SQLAlchemy
import json
from datetime import date

database_path = os.environ.get('DATABASE_URL')

if not database_path:
    database_name = "telecomsite"
    database_path = "postgres://{}/{}".format('localhost:5432', database_name)

db = SQLAlchemy()

'''
setup_db(app)
'''


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)

    db.create_all()


def db_drop_and_create():
    db.drop_all()
    db.create_all()



class Site(db.Model):
    __tablename__ = "sites"
    site_id = Column(Integer, primary_key=True)
    site_name = Column(String)
    region = Column(String, nullable=False)

    def __init__(self, site_name, region):
        self.site_name = site_name
        self.region = region

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            "site_id": self.id,
            "site_name": self.site_name,
            "region": self.region
        }


class Inventory(db.Model):
    __tablename__ = "Inventories"
    site_id = Column(Integer, primary_key=True)
    site_name = Column(String, nullable=False)
    technology = Column(String, nullable=False)

    def __init__(self, name, age):
        self.site_name = site_name
        self.technology = technology

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            "site_name": self.site_name,
            "age": self.technology,
        }
