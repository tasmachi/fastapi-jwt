from fastapi import APIRouter,Depends
from schemes import UserBase,UserDisplay
from sqlalchemy.orm import Session
from typing import List
from db import db_user
from auth.oauth2 import get_current_user
from db.database import get_db

router=APIRouter(prefix='/user',tags=['User'])

@router.post('/',response_model=UserDisplay)
def create_user(request:UserBase,db: Session=Depends(get_db)):
    return db_user.create_user(db,request)

@router.get('/',response_model=List[UserDisplay])
def get_all_user(db: Session=Depends(get_db),current_user:UserBase=Depends(get_current_user)):
    return db_user.get_all_users(db)

@router.get('/{username}',response_model=UserDisplay)
def get_user(username: str,db: Session=Depends(get_db),current_user:UserBase=Depends(get_current_user)):
    return db_user.get_user_by_username(db,username)

@router.post('/{id}/update')
def update_user(id: int,request: UserBase,db: Session=Depends(get_db),current_user:UserBase=Depends(get_current_user)):
    return db_user.update_user(db,id,request)

@router.get('/{id}/delete')
def delete_user(id:int,db: Session=Depends(get_db),current_user:UserBase=Depends(get_current_user)):
    return db_user.delete_user(db,id)