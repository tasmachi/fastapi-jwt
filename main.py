from fastapi import FastAPI,HTTPException,WebSocket,WebSocketDisconnect
from typing import Optional
from exceptions import StoryException
from fastapi.responses import HTMLResponse
from router import blog_get,blog_post,user,article,product,file,dependencies
from auth import authentication
from db.database import engine
from starlette.responses import PlainTextResponse
from db import models
from client import html
from templates import templates
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import time

app=FastAPI()

app.include_router(dependencies.router)
app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(article.router)
app.include_router(product.router)
app.include_router(file.router)
app.include_router(templates.router)

@app.exception_handler(StoryException)
def story_exception_handler(request: Request,exc:StoryException):
    return JSONResponse(
        status_code=418,
        content={'detail':exc.name}
    )
@app.exception_handler(HTTPException)
def http_handler(request:Request,exc:StoryException):
    return PlainTextResponse(str(exc),status_code=400)

origins=[
    'http://localhost:3000'
]

@app.get('/')
async def get():
    return HTMLResponse(html)

clients=[]

@app.websocket("/chat")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            for client in clients:
                if client != websocket:  # Avoid sending to the same client
                    await client.send_text(data)
    except WebSocketDisconnect:
        # Handle client disconnection (optional)
        clients.remove(websocket)
        print(f"Client disconnected!")

models.Base.metadata.create_all(engine)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.mount('/files',StaticFiles(directory='files'),name='files')
app.mount('/templates/static',StaticFiles(directory='templates/static'),name='static')