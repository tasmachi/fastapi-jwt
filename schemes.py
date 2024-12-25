from pydantic import BaseModel
from typing import Optional,List

class Article(BaseModel):
    title:str
    content:str
    published:bool
    class Config():
        orm_mode=True


class Image(BaseModel):
    url: str
    alias: str

class BlogModel(BaseModel):
    title:str
    content:str
    published: Optional[bool]
    tags:List[str]=[]
    image:Optional[Image]=None

class UserBase(BaseModel):
    username: str
    email: str
    password: str

class UserDisplay(BaseModel):
    username: str
    email: str
    items: List[Article]=[]
    class Config():
        orm_mode=True

class ArticleBase(BaseModel):
    title:str
    content:str
    published:bool
    creater_id:int

class User(BaseModel):
    username:str
    class Config():
        orm_mode=True


class ArticleDisplay(BaseModel):
    title:str
    content:str
    published:bool
    user:User
    class Config():
        orm_mode=True

class ProductBase(BaseModel):
    title:str
    description:str
    price:float