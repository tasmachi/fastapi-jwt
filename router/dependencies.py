from fastapi import APIRouter,Depends
from fastapi.requests import Request
from login import log

router=APIRouter(prefix='/depend',tags=['dependencies'],dependencies=[Depends(log)])

def convert_parama(request:Request,separator:str):
    query=[]
    for key, value in request.headers.items():
        query.append(f'{key} {separator} {value}')
    return query 

def convert_headers(request:Request,separator:str='--',query=Depends(convert_parama)):
    out_headers=[]
    for key, value in request.headers.items():
        out_headers.append(f'{key} {separator} {value}')
    return {
        'headers':out_headers,
        'query':query
    } 

@router.get('/')
def get_items(headers=Depends(convert_headers)):
    return {
        'items':['a','b','c'],
        'headers':headers
    }

class Account:
    def __init__(self, name:str,email:str):
        self.name=name
        self.email=email

@router.post('/user')
def add_user(name:str,email:str,password:str,account=Depends(Account)):
    return {
        'name':account.name,
        'email':account.email
    }