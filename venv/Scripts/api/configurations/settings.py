import os

class APIConfig:
    pass

class DBConfiguration:
    URL = "postgresql://postgres:800910156602468@localhost/postgres"

class ImageConfig:
    CONFIGDIR = os.path.dirname(os.path.abspath(__file__))
    BASEDIR = os.path.dirname(CONFIGDIR)
    CDN = os.path.join(BASEDIR, "cdn")
    IMAGES = os.path.join(CDN, "images")
    
    