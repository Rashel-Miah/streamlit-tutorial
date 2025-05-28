from enum import Enum
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

app = FastAPI()

class role(str, Enum):
    ADMIN = "ADMIN"
    USER = "USER"

@app.get("/user/{role}")
async def user(role:role):
    if role is role.ADMIN:
        return JSONResponse(status_code=200, content={
            "Message": "You are admin"
        })
    else:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={
            "message": "sorry, you are not admin"
        })
    
@app.get("/")
async def hello():
    return {
        "message": "welcome"
    }

