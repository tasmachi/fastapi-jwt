from fastapi import APIRouter,Header,Cookie,Form
from typing import Optional,List
from fastapi.responses import Response,HTMLResponse,PlainTextResponse
from login import log
import time

router=APIRouter(prefix='/product',tags=['product'])

product=['watch','camera','phone']

@router.post('/new')
def create_product(name: str=Form(...)):
     product.append(name)
     return product

# def time_comsuming():
#      time.sleep(7)
#      return 'ok'

@router.get('/all')
async def get_all_product():
    log('myAPI','call to get all products')
    # return product
    data= " ".join(product)
    response=Response(content=data,media_type='text/plain')
    response.set_cookie(key='test_cookie',value='cookie value')
    return response

@router.get('/header')
def get_product(response:Response,
                costum_header:Optional[List[str]]=Header(default=[]),
                test_cookie: Optional[str]=Cookie(None)):
     response.headers['custom_response_header']=", ".join(costum_header)
     return {
          'data':product,
          'custom_header':test_cookie
     }
@router.get('/{id}',responses={
     200:{
          'content':{
               'text/html':{
                    'example':'<div>product</div>'
               }
          },
          'description':'returns the html object'
     },
     404: {
          'content':{
               'text/plain':{
                    'example':'product not avialable'
               }
          },
          'description':'A clear text message error'
     }
})
def get_product(id:int):
    if id >len(product):
        out='product not avialable'
        return PlainTextResponse(status_code=404,content=out,media_type='text/plain')
    else:
          products=product[id]
    out = """
    <head>
<style>
.product {{
width:500px;
height:30pc;
border:2px solid green
background-color:lightyellow;
text-align:center;
}}
</style>
</head>
<div class='product'>{products} </div>
"""
    return HTMLResponse(content=out,media_type='text/html')