from schemes import UserBase
from sqlalchemy.orm.session import Session
from db.models import DbUser
from fastapi import HTTPException,status
from db.hash import hash_password

def create_user(db: Session,request:UserBase):
    user=DbUser(
        username=request.username,
        email=request.email,
        password=hash_password(request.password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_all_users(db:Session):
    return db.query(DbUser).all()

def get_user_by_username(db:Session,username: str):
    user=db.query(DbUser).filter(DbUser.username==username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with username {username} not found!')
    return user

def update_user(db: Session, id: int, request: UserBase):
    user=db.query(DbUser).filter(DbUser.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with ID {id} not found!')

    user.update({
        DbUser.username : request.username,
        DbUser.email : request.email,
        DbUser.password : hash_password(request.password)
    })
    db.commit()
    return {'message':f'user with ID {id} updated successfully!'}

def delete_user(db:Session,id: int):
    user=db.query(DbUser).filter(DbUser.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with ID {id} not found!')
    db.delete(user)
    db.commit()
    return {'message':'user deleted successfully!'}

