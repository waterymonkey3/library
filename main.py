from fastapi import FastAPI
from api.safe import api_safe

app = FastAPI(title='Library API', description='the API of library manage system')

app.include_router(api_safe,prefix="/safe",tags=['API Health'])



@app.middleware("http")
async def middleware1(request, call_next):
    print("middleware1 start")
    response = await call_next(request)
    print("middleware1 end")
    return response



@app.get('/')
async def root():
    return{'message':'hello world'}



if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app")
