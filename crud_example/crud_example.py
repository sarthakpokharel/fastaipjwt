from main import APIRouter
from .crud_example_model import CRUD

router = APIRouter(prefix='/crud')

@router.get('/')
async def get():
    return {"message" : "get"}
    
@router.post('/{id}')
async def post():
    return{"message" : "post"}

@router.get('/{id}')
async def get():
    return {"message" : "getId"}

@router.put('/')
async def put():
    return {"message" : "put"}
    
@router.delete('/{id}')
async def delete():
    return{"message" : "delete"}