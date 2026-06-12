from fastapi import APIRouter

api_safe = APIRouter()


@api_safe.get('/')
async def safe():

    return {'message':'Healthy'}
