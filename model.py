#from flask_sqlalchemy import SQLAlchemy
#from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Boolean, Integer, String, Date, ForeignKey

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
engine = create_engine("mysql+mysqlconnector://root:My1566@localhost/lab62", echo=True)
Base = declarative_base()
metadata = Base.metadata

class User(Base):
    __tablename__='user'
    id=Column(Integer, primary_key=True)
    username=Column(String(45))
    firstname=Column(String(45))
    email=Column(String(45))
    password=Column(String(45))
    number=Column(String(45))

class Category(Base):
    __tablename__ = 'category'
    id=Column(Integer, primary_key=True)
    name = Column(String(45))

class Tag(Base):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True)
    name = Column(String(45))

class Editors(Base):
    __tablename__ = 'editors'
    id = Column(Integer, primary_key=True)
    Notes_id = Column(Integer, ForeignKey('notes.id'))
    User_id = Column(Integer, ForeignKey('user.id'))
    user= relationship("User")
    notes=relationship("Notes")

class Notes(Base):
    __tablename__ = 'notes'
    id = Column(Integer, primary_key=True)
    title = Column(String(45))
    text = Column(String(45))
    Tag_id=  Column(Integer, ForeignKey('tag.id'))
    Category_id = Column(Integer, ForeignKey('category.id'))
    User_id=Column(Integer, ForeignKey('user.id'))

    tag=relationship("Tag")
    user=relationship("User")
    category = relationship("Category")
