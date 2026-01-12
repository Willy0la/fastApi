from fastapi import FastAPI
from app.routes.user import routing as userRouting

app = FastAPI()

@app.get("/")
def server():
    return{"message":"server is running"}

app.include_router(userRouting)