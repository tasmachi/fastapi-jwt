from passlib.context import CryptContext
import bcrypt

def hash_password(password):
    salt=bcrypt.gensalt()
    hash_password=bcrypt.hashpw(password.encode(),salt)
    return hash_password.decode()

def verify_password(hashed_password,plain_password):
    return bcrypt.checkpw(plain_password.encode(),hashed_password.encode())

pwd_cxt=CryptContext(schemes='bcrypt',deprecated='auto')

class Hash():
    @staticmethod
    def bcrypt(password:str):
        return pwd_cxt.hash(password)
    
    @staticmethod
    def verify(hashed_password,plain_password):
        return pwd_cxt.verify(plain_password,hashed_password)