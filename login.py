from fastapi.requests import Request

def log(tag='MyAPI',message='no message',request:Request=None):
    with open('login.txt','a+') as log:
        log.write(f'{tag} : {message}\n')
        log.write(f'\t{request.url}\n')