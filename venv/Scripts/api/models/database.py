from sqlalchemy import URL
from sqlalchemy import create_engine
from sqlalchemy.orm import (DeclarativeBase, sessionmaker)


from configurations.config import DATABASE_URL

# DATABASE CONFIGURATION
db_configuration = DATABASE_URL

# DATABASE URL
db_url = URL.create(
    drivername=db_configuration["drivename"], 
    username=db_configuration["username"], 
    password=db_configuration["password"], 
    host=db_configuration["host"], 
    database=db_configuration["database"]
) 

# CREATE ENGINE: THIS IS MYSQL DATABASE ENGINE
engine = create_engine(url=db_configuration.DATABASE_URL, 
                       connect_args={"check_same_thread": False})

# SESSION MAKER
sessionMaker = sessionmaker(bind=engine, 
                             autoflush=False, 
                             expire_on_commit=False)

session = sessionMaker()

class Base(DeclarativeBase):
    pass