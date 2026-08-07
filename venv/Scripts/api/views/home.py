from fastapi.routing import APIRouter


MAIN = APIRouter()

@MAIN.get("/")
def homepage():
    return {"message": "Hello, World."}