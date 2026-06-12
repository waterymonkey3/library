from fastapi import FastAPI


app = FastAPI(title='测试API', description='整体描述')


@app.get('/')
async def root():
    return{'message':'hello world'}


@app.get(path='/safe', summary='接口安全', description='接口健康监测', tags=['Health'])
async def safe():

    return {'message':'healthy'}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app")
