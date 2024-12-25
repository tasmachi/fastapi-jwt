from schemes import ArticleBase
from exceptions import StoryException
from sqlalchemy.orm import Session
from db.models import DbArticle
from fastapi import HTTPException,status

def create_article(db:Session,request:ArticleBase):
    if request.content.startswith('Once open a time'):
        raise StoryException('no stories please')
    article=DbArticle(
        title=request.title,
        content=request.content,
        published=request.published,
        user_id=request.creater_id
    )
    db.add(article)
    db.commit()
    db.refresh(article)
    return article

def get_article(db:Session,id:int):
    article=db.query(DbArticle).filter(DbArticle.id==id).first()
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Article with ID {id} not found!')
    return article