from fastapi import  APIRouter
from app.schema.userschema import UserResponse
from app.schema.createuser import UserCreate
from typing import List
from fastapi import Response, status

routing = APIRouter(prefix="/welcome", tags=["USERS"])

@routing.get("/user", response_model=List[UserResponse])
def greet_user():
    return [{ "id":1, "name":"olawale",}]

@routing.post("/user", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def createUser(user:UserCreate):
    return { "id":user.id, "name":user.name}
