from fastapi import APIRouter
from fastapi import FastAPI,status,Response,Depends
from typing import Optional
from router.blog_post import request_func

router=APIRouter(prefix='/blog',tags=['blog'])

@router.get('/fine/ok/{id}',
         summary='just home page as written',
         description='you know i started over it!',
         response_description='ok fine')
def index(id:int):
    return {'message':f'hello world! {id}'}
@router.get('/all')
def get_all_blogs(page:Optional[int]=None,page_size:Optional[int]=None):
    return {
        'page':page,
        'page_size':page_size
    }
@router.get('/line')
def blog(page_size: Optional[int]=None,req_param: dict=Depends(request_func)):
    return {'message':f'the page size {page_size}',
            'req_param':req_param}

@router.get('/got/{id}',status_code=status.HTTP_200_OK)
def combine(id: int,response:Response,gotten:int,phone:Optional[int]=None):
    if id>5:
        response.status_code=status.HTTP_404_NOT_FOUND
        return {'error':f'{id} not found'}
    else:
        return {'message':{
        'id':id,
        'gotten':gotten,
        'phone':phone
    }}