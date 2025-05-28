from pydantic import BaseModel
from utils import Role


class userSchemas(BaseModel):
    name : str | None = None
    email: str
    password:str
    role:Role = Role.USER