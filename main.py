from fastapi import FastAPI
from fastapi import APIRouter
from app.login.login import router
from crud_example.crud_example import router

app = FastAPI()

app.include_router(router)