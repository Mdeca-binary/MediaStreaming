import pymysql

import urllib

from sqlalchemy import URL
from sqlalchemy import create_engine
from sqlalchemy.orm import (DeclarativeBase, sessionmaker)

from configurations.config import DATABASE_URL


# DATABASE CONFIGURATION
db_configuration = DATABASE_URL

db_url = URL.create(
    drivername=DATABASE_URL["drivername"], 
    username=DATABASE_URL["username"], 
    password=DATABASE_URL["password"], 
    host=DATABASE_URL["host"], 
    database=DATABASE_URL["database"]
) 

# CREATE ENGINE: THIS IS MYSQL DATABASE ENGINE
engine = create_engine(url=db_url)

# SESSION MAKER
sessionMaker = sessionmaker(bind=engine, 
                             autoflush=False, 
                             expire_on_commit=False)

session = sessionMaker()

class Base(DeclarativeBase):
    pass

Base.metadata.create_all(engine)