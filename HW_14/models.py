from sqlalchemy import create_engine, Column, Table, ForeignKey, MetaData
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Date, DateTime, Float, Boolean, Text
from sqlalchemy.sql.schema import ForeignKey, Table, MetaData


Base = declarative_base()
CONNECTION_STRING = "sqlite:///scrapy_quotes.db"

def db_connect():
      return create_engine('sqlite:///sqlalchemy_example.db')


def create_table(engine):
     Base.metadata.create_all(engine)


class Author(Base):
    __tablename__ = "author"

    id = Column(Integer, primary_key=True)
    name = Column('name', String(50), unique=False)
    ref = Column('ref', String(100), unique=False)
    birthday = Column('birthday', String(50), unique=False)
    bornlocation = Column('bornlocation', String(150))


class Quote(Base):
    __tablename__ = "quote"

    id = Column(Integer, primary_key=True)
    quote_content = Column('quote_content', Text())
    author_id = Column(Integer, ForeignKey('author.id'))
    author = relationship (Author)
    tags = relationship('Tag',secondary='link', backref='quote')



class Tag(Base):
    __tablename__ = "tag"

    id = Column(Integer, primary_key=True)
    name = Column('name', String(30), unique=True)
    quote_id = Column(Integer, ForeignKey('quote.id'))  # Many tags to one quote
    quotes = relationship('Quote', secondary='link')


class Link(Base):
    __tablename__ = 'link'
    quote_id = Column(Integer,ForeignKey('quote.id'), primary_key=True)
    tag_id = Column(Integer,ForeignKey('tag.id'), primary_key = True)
