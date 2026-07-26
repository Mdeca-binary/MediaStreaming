import os

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
    "drivename": None, 
    "username": "root",
    "password": "mASWIKANENG", 
    "host": "localhost", 
    "database": "users"
}