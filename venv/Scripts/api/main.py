from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from views.pages import VIEWS
from configurations.config import StaticConfig

# INITIATE FASTAPI,  ROOT OF THE ENTIRE API
API = FastAPI()

# STATIC FILES FOR SERVING CSS AND JAVASCRIPT
static_config = StaticConfig()
API.mount("/static", StaticFiles(directory=("%s"%static_config.STORED_TO)), name="static")

# REGISTERING PAGES/ ROUTES
API.include_router(VIEWS)