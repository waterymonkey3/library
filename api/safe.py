from fastapi import APIRouter, Request,Depends

api_safe = APIRouter()

async def commonvar(
        num1: int = 1,
        num2: int = 2
):
    return num1+num2

@api_safe.get('/')
async def safe():

    return {'message':'Healthy'}


@api_safe.get('/get_test')
async def get_safe(request: Request):
    get_safe = request.query_params
    print(get_safe)
    return {'message':'get_safe'}



@api_safe.post('/post_test')
async def post_safe(request: Request, common=Depends(commonvar)):
    try:
        num = await commonvar()
        print(num)
        post_safe = await request.json()
        print(post_safe)
        return {'message':post_safe}
    except Exception as e:
        print("error:"+str(e))
        return {"error:"+str(e)}