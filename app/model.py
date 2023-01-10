from pydantic import BaseModel

class UserSchema(BaseModel):
    username: str 
    email : str
    password: str
    user_role:str
    # class Config:
    #         the_schema = {
    #             "userdemo" : {
    #             "name" : "Bek",
    #             "email": "help@beckbrace.com",
    #             "password": "123"
    #             }
    #         }

class UserLoginSchema(BaseModel):
    username : str
    password: str
    # class Config:
    #         the_schema = {
    #             "userdemo" : {
    #             "email": "help@beckbrace.com",
    #             "password": "123"
    #             }
    #         }
