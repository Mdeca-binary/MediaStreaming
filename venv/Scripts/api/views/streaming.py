from fastapi import APIRouter


STREAMING = APIRouter(
    prefix="/streaming", 
    tags=["Streaming"]
)

@STREAMING.get("/vidstreaming")
def streamingVideoPageView():
    return