import uuid

from datetime import datetime


from sqlalchemy import (String, Boolean, DateTime, Uuid)
from sqlalchemy import (create_engine,)
from sqlalchemy.orm import(sessionmaker)
from sqlalchemy.orm import (Mapped, 
                            mapped_column,
                            DeclarativeBase,)

from configurations.settings import (DBConfiguration)

db_configuration = DBConfiguration()

engine = create_engine(url=db_configuration.URL)
session_maker = sessionmaker(engine)

session = session_maker()

class Base(DeclarativeBase):
    pass

class UserDBModel(Base):
    __tablename__ = "user"
    id: Mapped[uuid.UUID] = mapped_column(Uuid, 
                                        primary_key=True, 
                                        nullable=False, 
                                        index=True)
    username: Mapped[str] = mapped_column(String(20), 
                                        nullable=False, 
                                        index=True)
    hashed_pwd: Mapped[str] = mapped_column(String(100), 
                                            nullable=False, 
                                            index=True)
    account_created: Mapped[datetime] = mapped_column(DateTime, 
                                                        nullable=False, 
                                                        index=True)
    last_visit: Mapped[datetime] = mapped_column(DateTime, 
                                                    nullable=True, 
                                                    index=True)
    is_active: Mapped[bool] = mapped_column(Boolean, 
                                            nullable=False, 
                                            index=True)
    is_superuser: Mapped[bool] = mapped_column(Boolean, 
                                                nullable=False, 
                                                index=True)
    is_anonymous: Mapped[bool] = mapped_column(Boolean, 
                                            nullable=False, 
                                            index=True)
    
    def __repr__(self):
        return ""

# class UserDBInterface:
#     def __init__(self, *, username: str|None = None, plain_pwd: str|None = None):
#         self.username:str = username
#         self.plain_pwd: str = plain_pwd
#         self.columns = UserDBModel()
#         self.db_config = DBConfiguration()
#         self.engine = create_async_engine(url=self.db_config.URL, echo=True)
#         self.async_session = async_sessionmaker(self.engine, expire_on_commit=False)
      
    
#     async def async_main(self) -> None:
#         async with self.engine.begin() as connect:
#             await connect.run_sync(Base.metadata.create_all)
            
    
#     async def create_object(self):
#         self.async_
#         async with self.async_session() as session:
#             user = self.columns(
#                 username=self.username, 
#                 hashed_pwd=self.plain_pwd
#             )
#             await session.add(user)
#             await session.commit()

Base.metadata.create_all(engine)