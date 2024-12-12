from typing import Union
from fastapi import FastAPI
from server.cruds import crud_router_v1
app = FastAPI()
app.include_router(crud_router_v1, prefix="/v1")
