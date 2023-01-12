from fastapi import FastAPI, Depends
from fastapi import APIRouter
from app.login.login import router as login
from crud_example.crud_example import router as crud

from app.auth.jwt_bearer import jwtBearer
from app.auth.jwt_handler import current_user_info

'''
FOR THIS CMS SYSTEM WE CAN CREATE 3 DIFFERENT APPLICATIONS WITHIN OUR APPLICATION OR 2 FOR THAT MATTER, LET'S SEE
1. CONTAINS THE ENTIRE BACKEND , ABSOLUTELY MUST BE AUTHENTICATED TO GAIN ACCESS
2. WILL CONTAIN LOGIN AND REGISTRATION URLS
3. ANGULAR CODE , THIS CAN BE IN THE MAIN APP AND CAN CO-EXIST WITH (2). bOTH OF THESE CAN EXIST IN THE MAIN APP AS WELL
INSTEAD OF A SEPERATE APPLICATION

'''


app = FastAPI(dependencies= [Depends(jwtBearer())])

app.include_router(crud)
app.include_router(login)




@app.get("/")
def a():
    return current_user_info() #will not work... but why isn't it throwing any error?....NO Idea!