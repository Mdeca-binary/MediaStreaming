from fastapi.routing import APIRouter

# INITIATING VIEWS / PAGES OF THE APP
VIEWS = APIRouter()

@VIEWS.get('/')
async def homepage():
    return {'message': 'Hello, world!!'}
