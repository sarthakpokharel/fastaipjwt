from main import APIRouter

router = APIRouter(prefix='/api')

class crud:
    @router.get('/crud')
    async def greet():
        return {"message" : "hi"}
    
    @router.post('/crud/post')
    async def post():
        return{"message" : "hi"}
