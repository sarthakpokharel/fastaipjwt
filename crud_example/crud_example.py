from main import APIRouter
from .crud_example_model import Users
from app.database.db import execute_query

router = APIRouter(prefix='/crud', tags=['CRUD'])

# crud = CRUD
query :str
table = "users"

@router.get('/')
async def get(req: Users):
    base_query = "select username, email from " + table
    return {"message": "True"}
    
@router.post('/')
async def post(model: Users):
    query = "INSERT INTO "+ table + " (username, email, password, user_role) VALUES ('{}', '{}', '{}', '{}');".format(model.username, model.email, model.password, model.admin_role)
    return execute_query (query, res = False)


@router.get('/{id}')
async def get():
    query = "SELECT username, email FROM " +table+ " WHERE id = " + {id} +" );"
    return execute_query(query)

@router.put('/')
async def put(model : Users):
    query = "UPDATE " +table+ " SET username={}, email={}, password={}, user_role={} WHERE id ={}".format(model.username, model.email, model.password, model.admin_role)
    return {"message" : "put"}
    
@router.delete('/{id}')
async def delete():
    query = 'DELETE FROM '+table+' WHERE id = ' + {id} +' );'
    return execute_query(query)