from app.model import UserSchema, UserLoginSchema
from app.auth.jwt_handler import signJWT
from main import APIRouter
from app.database import db
from app.encryption import Encryption

en = Encryption
router = APIRouter()

users = []

#User Sign UP
@router.post("/user/signup", tags = ["user"])
def user_signup(user: UserSchema):
    users.append(user)
    return signJWT(user.email, user.user_role)


def check_user(data: UserLoginSchema):
    query = "SELECT password, user_role FROM users WHERE username=%s"
    query_execution = db.execute_query(query, (data.username,), True)
    try:        
        if query_execution:
            pwd, admin_role = query_execution[0]
            if en.check_password(data.password,pwd.encode()):
                return {"success":True,
                        "admin_role": admin_role.replace(" ", "")
                        }
        return {"success":False}
    except:
        return {"success":False}

@router.post("/user/login", tags=["user"])
def user_login(user: UserLoginSchema):           
    ck = check_user(user)
    if ck.get('success'):
        return signJWT(user.username, ck.get('admin_role'))
    else:
        return{
            "error" : "Invalid Login Credentials"
        }
        
        
        
        
        
        
        
        
        
        
# def check_user(data: UserLoginSchema):
#     #first check if the said user exists
#     q = "SELECT username FROM users WHERE username='" +data.username+"';"
#     if len(db.execute_query(q, res=True))==0:
#         return {"success":False}
#     query = "SELECT password, user_role FROM users WHERE username='"+data.username+"'" 
#     query_execution = db.execute_query(query, res=True)
#     if len(query_execution) == 0:
#         return False
#     else:
#         pwd = []
#         admin_role: str
#         for tup in query_execution:
#             pwd.append(tup[0])
#             admin_role = tup[1]
#         # return (first_values[0])
#         chk = en.check_password(data.password,pwd[0].encode())
#         if chk:
#             return {"success":True,
#                     "admin_role": admin_role.replace(" ", "")
#                     }
        # return {"success":False}