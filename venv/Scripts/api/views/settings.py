from fastapi import APIRouter

SETTINGS = APIRouter(
    prefix="/settings", 
    tags=["Settings"]
)

@SETTINGS.get("/config")
def root():
    return