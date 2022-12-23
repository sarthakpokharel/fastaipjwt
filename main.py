from fastapi import FastAPI, Body, Depends
from app.model import PostSchema, UserSchema, UserLoginSchema
from app.auth.jwt_handler import signJWT
from app.auth.jwt_bearer import jwtBearer


app = FastAPI()

posts = [
    {
    "id": 1,
    "title": "penguins",
    "text": "Penguins are gods"
    },
    {
    "id": 1,
    "title": "dogs",
    "text": "dogs are gods"
    },
    {
    "id": 1,
    "title": "whales",
    "text": "whales are gods"
    },
]


users = []

#GET - for test
@app.get("/", tags=["Initial"])
async def greet():
    return {"message": posts}


# Get Posts
@app.get("/posts", dependencies=[Depends(jwtBearer())], tags=["posts"])
def get_posts():
    return { "dataa": posts }


@app.get("/posts/{id}", tags=["posts"])
def get_single_post(id: int):
    if id > len(posts):
        return {
            "error": "No such post with the supplied ID."
        }

    for post in posts:
        if post["id"] == id:
            return {
                "data": post
            }

#User Sign UP
@app.post("/user/signup", tags = ["user"])
def user_signup(user: UserSchema=Body(default = None)):
    users.append(user)
    return signJWT(user.email)

def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password:
            return True
        return False

@app.post("/user/login", tags=["user"])
def user_login(user: UserLoginSchema=Body(default=None)):
    if check_user(user):
        return signJWT(user.email)
    else:
        return{
            "error" : "Invalid Login Credentials"
        }