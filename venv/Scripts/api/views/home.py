from fastapi.routing import APIRouter


MAIN = APIRouter(prefix="", 
                 tags=["Home"])

@MAIN.get("/")
def homepage():
    return