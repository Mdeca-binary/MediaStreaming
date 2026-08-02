import os
from fastapi.security import OAuth2PasswordBearer
class StaticConfig:
    # CONFIGURATIONS FOR CSS AND JAVASCRIPT
    # CURRENT FOLDER
    _CURRENT_DIR = os.path.abspath(__file__)
    # FOLDER FOR EVERYTHING
    _ROOT_DIR = os.path.dirname(os.path.dirname(_CURRENT_DIR))
    #  root -> static or root/static
    STORED_TO = os.path.join(_ROOT_DIR, "static")
    
class TemplatesConfig:
    # TEMPLATES CONFIGURATIONS
    # CURRENT FOLDER
    _CURRENT_DIR = os.path.abspath(__file__)
    # FOLDER FOR EVERYTHING
    _ROOT_DIR = os.path.dirname(os.path.dirname(_CURRENT_DIR))
    #  root -> templates / root/templates
    STORED_TO = os.path.join(_ROOT_DIR, "templates")


class VideoConfig:
    # VIDEO STORAGE CONFIGURATION
    # CURRENT DIR (e.g configuration/)
    _CURRENT_DIR = os.path.abspath(__file__)
    # ROOT DIR (e.g api/)
    _ROOT_DIR = os.path.dirname(os.path.dirname(_CURRENT_DIR))
    # APPOINTED DIR(e.g storage/video)
    STORED_TO = os.path.join(_ROOT_DIR, "storage", "video")

DATABASE_URL = {
    "drivername": "postgresql+psycopg2", 
    "username": "postgres", 
    "password": "800910156602468", 
    "host": "localhost",
    "database": "users"
}

class APIConfig:
    SECRET_KEY = ""

OAUTH2_SCHEME = OAuth2PasswordBearer(
    tokenUrl="login", 
    scopes={"user": "",
            "information": ""}
)

class JWTConfig:
    PRIVATE_KEY = b""
    PUBLIC_KEY = b""
    ALGORITHM = "PS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30 