from fastapi import FastAPI

from views import (home, auth, streaming, 
                   user, settings)
#
from logs.logg import Logger

# API INITIALIZATION
API = FastAPI(title="MediaStreaming.API")

logger = Logger(API.title)

# print(logger)

# REGISTERING PAGES
API.include_router(home.MAIN)
API.include_router(auth.AUTH)
API.include_router(user.USER_PROFILE)
API.include_router(streaming.STREAMING)
API.include_router(settings.SETTINGS)