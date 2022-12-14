from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.sql.sqltypes import DateTime


Base = declarative_base()

class Record(Base):
    __tablename__ = "records"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    created = Column(DateTime, default=datetime.now())
    email = relationship('Email', cascade="all, delete", backref="record")
    adress = relationship("Adress", cascade="all, delete", backref="record")
    phone = relationship("Phone", cascade="all, delete", backref="record")
    #tags = relationship("Tag", secondary=note_m2m_tag, backref="notes")


class Email(Base):
    __tablename__ = "emails"
    id = Column(Integer, primary_key=True)
    email_name = Column(String(100), nullable=True)
    rec_id = Column(Integer, ForeignKey(Record.id, ondelete="CASCADE"))


class Adress(Base):
    __tablename__ = "adresses"
    id = Column(Integer, primary_key=True)
    adress_name = Column(String(250), nullable=True)
    rec_id = Column(Integer, ForeignKey(Record.id, ondelete="CASCADE"))


class Phone(Base):
    __tablename__ = "phones"
    id = Column(Integer, primary_key=True)
    phone_name = Column(String(20), nullable=True)
    rec_id = Column(Integer, ForeignKey(Record.id, ondelete="CASCADE"))
