'''
Module, API,library, framework, etc. that provides a set of functions and classes that can be used to build software.
One to many relationship with calls. Collection.
'''
from database import db
import datetime
from .base import Base

class API(Base):
    __tablename__ = 'apis'

    callees = db.relationship('Call', backref='API', lazy='dynamic')

    def __repr__(self):
        return '<API %r>' % self.name
    __tablename__ = 'apis'
