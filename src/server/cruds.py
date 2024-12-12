from fastapi import APIRouter
from server.app_controller import app_controller as ac
crud_router_v1 = APIRouter(prefix="/resource", tags=["resources"])

@crud_router_v1.get("/resource/{name}", description="Our first get endpoint.")
async def get_resource(name:str):
    return ac.get_resource(name)
