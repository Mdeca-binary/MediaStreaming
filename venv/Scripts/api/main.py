from fastapi import FastAPI

from views.pages import VIEWS

# INITIATE FASTAPI,  ROOT OF THE ENTIRE API
API = FastAPI()

API.include_router(VIEWS)