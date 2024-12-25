from db.database import Base
from sqlalchemy import Integer,Column,String,Boolean,ForeignKey
from sqlalchemy.orm import relationship

class DbUser(Base):
    __tablename__='user'
    id=Column(Integer,primary_key=True,index=True)
    username=Column(String)
    email=Column(String)
    password=Column(String)
    items=relationship('DbArticle',back_populates='user')

class DbArticle(Base):
    __tablename__='article'
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String)
    content=Column(String)
    published=Column(Boolean)
    user_id=Column(Integer,ForeignKey('user.id'))
    user=relationship('DbUser',back_populates='items')

