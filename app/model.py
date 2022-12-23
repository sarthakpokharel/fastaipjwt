from pydantic import BaseModel, Field, EmailStr

class PostSchema(BaseModel):
    id: int = Field(default=None)
    title: str = Field(...)
    content: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "title": "Securing FastAPI applications with JWT.",
                "content": "In this tutorial, you'll learn how to secure your application by enabling authentication using JWT. We'll be using PyJWT to sign, encode and decode JWT tokens...."
            }
        }

class UserSchema(BaseModel):
    fullname: str = Field(default=None)
    email : EmailStr = Field (default=None)
    password: str = Field(default=None)
    class Config:
            the_schema = {
                "userdemo" : {
                "name" : "Bek",
                "email": "help@beckbrace.com",
                "password": "123"
                }
            }

class UserLoginSchema(BaseModel):
    email : EmailStr = Field (default=None)
    password: str = Field(default=None)
    class Config:
            the_schema = {
                "userdemo" : {
                "email": "help@beckbrace.com",
                "password": "123"
                }
            }
