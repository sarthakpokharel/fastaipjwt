from pydantic import BaseModel

class UserSchema(BaseModel):
    fullname: str 
    email : str
    password: str
    class Config:
            the_schema = {
                "userdemo" : {
                "name" : "Bek",
                "email": "help@beckbrace.com",
                "password": "123"
                }
            }

class UserLoginSchema(BaseModel):
    email : str
    password: str
    class Config:
            the_schema = {
                "userdemo" : {
                "email": "help@beckbrace.com",
                "password": "123"
                }
            }
