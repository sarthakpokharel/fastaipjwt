from pydantic import BaseModel

class Users(BaseModel):
    username : str
    email: str
    password: str
    admin_role:str
    
    def items(self):
        return self.dict().items()

searchables = ['username','email']

required = ['username', 'email', 'password', 'admin_role']