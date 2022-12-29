from main import APIRouter

router = APIRouter(prefix='/crud')

@router.get('/')
async def get():
    return {"message" : "hi"}
    
@router.post('/{id}')
async def post():
    return{"message" : "hi"}

@router.get('/{id}')
async def get():
    return {"message" : "hi"}

@router.put('/')
async def put():
    return {"message" : "hi"}
    
@router.delete('/{id}')
async def delete():
    return{"message" : "hi"}