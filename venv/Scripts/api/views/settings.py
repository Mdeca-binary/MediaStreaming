from fastapi import APIRouter

SETTINGS = APIRouter(
    prefix="/settings", 
    tags=["Settings"]
)

@SETTINGS.get("/config")
def root():
    return

@SETTINGS.get("/credits")
def creditsPageView():
    return

@SETTINGS.get("/mode")
def modePageView():
    return

@ SETTINGS.get("/account")
def accountPageView():
    return