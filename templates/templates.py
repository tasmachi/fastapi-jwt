from fastapi import APIRouter,BackgroundTasks
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from schemes import ProductBase
from login import log

router=APIRouter(
    prefix='/temaplates',
    tags=['templates']
)

templates=Jinja2Templates(directory='templates')

@router.post('products/{id}',response_class=HTMLResponse)
def get_product(id:int,product:ProductBase,request:Request,bt: BackgroundTasks):
    bt.add_task(log_templates_call,f'template read for product with id {id}')
    return templates.TemplateResponse(
        'product.html',
        {
            'request':request,
            'id':id,
            'title':product.title,
            'description':product.description,
            'price':product.price
        }
    )

def log_templates_call(message: str):
    log('myAPI',message)