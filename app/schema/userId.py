from pydantic import BaseModel

class UserbyIdResponse(BaseModel):
    id:int
    name:str
    age:int

