from fastapi import  APIRouter
from app.schema.userschema import UserResponse
from app.schema.createuser import UserCreate
from app.schema.userId import UserbyIdResponse
from typing import List
from fastapi import Response, status

routing = APIRouter(prefix="/welcome", tags=["USERS"])

@routing.get("/user", response_model=List[UserResponse])
def greet_user():
    return [{ "id":1, "name":"olawale",}]
@routing.get("/user/{id}", response_model=UserbyIdResponse, status_code=status.HTTP_200_OK)
def get_user_by_id(id:int,):
    return{ "id":13,
           "name":"Olawale",
           "age": 22}

@routing.post("/user", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def createUser(user:UserCreate):
    return { "id":user.id, "name":user.name, "age":user.age}
