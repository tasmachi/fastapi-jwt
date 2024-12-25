from fastapi import APIRouter
from fastapi import FastAPI,status,Response,Query,Path,Body
from typing import Optional,List
from schemes import BlogModel

router=APIRouter(prefix='/post',tags=['post'])

@router.post('/')
def post_blog(blog: BlogModel):
    return {'blog':blog}

@router.post('/new/{id}/comment')
def create_comment(blog:BlogModel,id:int=Path(...,ge=4),
                   comment_id: int=Query(None,
                                        title='ID of the comment',
                                         description='some description for the comment_id',
                                          alias='commentID' ,
                                          deprecated=True),
                                          content: str=Body(...,regex='^[a-z\s]*$'),
                                          v: Optional[List[str]]=Query(None)
                                          ):
    return {
        'blog':blog,
        'id':id,
        'comment_id':comment_id,
        'content':content,
        'v':v
    }

def request_func():
    return {'message':'learning fastapi is important'}