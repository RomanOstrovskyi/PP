from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+mysqlconnector://root:MyZno26112003@localhost:3306/BDfor7lab", echo=True)
Base = declarative_base()
metadata = Base.metadata




class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(VARCHAR(length=45), nullable=False)
    email = Column(VARCHAR(length=45), nullable=False)
    password = Column(VARCHAR(length=2000), nullable=False)

    notes = relationship("NoteStatistics", back_populates="user")

class NoteStatistics(Base):
    __tablename__ = 'notestatistics'
    id = Column(Integer, primary_key=True)
    time = Column(Date)
    userId = Column(Integer, ForeignKey('user.id'))
    noteId = Column(Integer, ForeignKey('note.id'))

    user = relationship("User", back_populates="notes")
    note = relationship("Note", back_populates="users")

class Tag(Base):
    __tablename__ = "tag"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(VARCHAR(length=45), nullable=False)

class Note(Base):

    __tablename__ = "note"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(VARCHAR(length=45), nullable=False)
    text = Column(VARCHAR(length=404), nullable=False)

    idTag = Column(Integer, ForeignKey('tag.id'), nullable=False)
    tag = relationship(Tag, backref="note", lazy=False)

    idOwner = Column(Integer, ForeignKey('user.id'), nullable=False)
    owner = relationship(User, backref="note", lazy=False)

    users = relationship("NoteStatistics", back_populates="note")


