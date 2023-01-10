from fastapi import FastAPI, Depends
from fastapi import APIRouter
from app.login.login import router as login
from crud_example.crud_example import router as crud

from app.auth.jwt_bearer import jwtBearer
from app.auth.jwt_handler import current_user_info

app = FastAPI()

app.include_router(crud, dependencies= [Depends(jwtBearer())])
app.include_router(login)



@app.get("/")
def a():
    return current_user_info() #will not work... but why isn't it throwing any error?....NO Idea!