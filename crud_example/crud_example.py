from main import APIRouter
from .crud_example_model import Users, searchables, required
from app.database.db import execute_query
from app.pagination import Pagination
from app.vaidator import Validator

router = APIRouter(prefix='/crud', tags=['CRUD'])

# crud = CRUD
query :str
table = "users"

@router.get('/')
async def get(): 
    perPage = 10
    pageNo = 1
    search_term = 'string'
    order_by = "ASC"
    orand = "OR"
    column_names = ['username', 'email', 'user_role']
    queries = Pagination.page(table, perPage, pageNo, searchables, search_term, order_by, column_names, orand)
    get_data= execute_query(queries['base_query'], res=True)
    count_value= execute_query(queries['count_query'], res=True)
    return {"data": get_data , "count_value" : count_value}
    
@router.post('/')
async def post(model: Users):
    # query = "INSERT INTO "+ table + " (username, email, password, user_role) VALUES ('{}', '{}', '{}', '{}');".format(model.username, model.email, model.password, model.admin_role)
    # return execute_query (query, res = False)
    Validator.validation(model, required)
    # print (type(model))

@router.get('/{id}')
async def get():
    query = "SELECT username, email FROM " +table+ " WHERE id = " + {id} +" );"
    return execute_query(query)

@router.put('/{id}')
async def put(model : Users):
    query = "UPDATE " +table+ " SET username={}, email={}, password={}, user_role={} WHERE id ={id}".format(model.username, model.email, model.password, model.admin_role)
    return {"message" : "put"}
    
@router.delete('/{id}')
async def delete():
    query = 'DELETE FROM '+table+' WHERE id = ' + {id} +' );'
    return execute_query(query)