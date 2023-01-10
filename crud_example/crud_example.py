from main import APIRouter
from .crud_example_model import Users, searchables, required
from app.database.db import execute_query
from app.pagination import Pagination
from app.vaidator import Validator
from app.messages import Messages
from app.encryption import Encryption

router = APIRouter(prefix='/crud', tags=['CRUD'])

query :str
table = "users"
messages = Messages

en = Encryption

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
    val = Validator.validation(model, required, table)
    if val is True:
        query = "INSERT INTO "+ table + " (username, email, password, user_role) VALUES ('{}', '{}', '{}', '{}');".format(model.username, model.email, en.encrypt(model.password), model.admin_role)
        return execute_query (query, res = False)
    elif val['validation_code'] is False:
        return messages.custom_message(val['message'])
    elif val['validation_code'] == 0:
        return messages.custom_message(val['message'])
    elif val['validation_code'] == 1:
        return messages.custom_message(val['message'])
    else:
        return messages.custom_message("Unknown Error")

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