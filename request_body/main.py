from fastapi import FastAPI, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from userschemas import userSchemas

app = FastAPI()

@app.post("/", tags=["Create User"])
async def store(user:userSchemas) -> userSchemas:
    print(user)
    #return{"Hello":"World"}
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=jsonable_encoder(user))

@app.get("/")
async def index():
    return {"message":"Welcome"}