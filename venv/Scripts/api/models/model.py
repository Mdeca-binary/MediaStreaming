import uuid

from datetime import datetime

# SQLALCHEMY FRAMEWORK
from sqlalchemy import (Column, String)
from sqlalchemy.orm import (mapped_column, Mapped)
# 
from .database import Base


class UserModel(Base):
    __tablename__ = "users"
    
    id: Mapped[uuid.UUID] = mapped_column(uuid.uuid4, 
                                        primary_key=True,
                                        index=True, 
                                        nullable=False, 
                                        unique=True)
    username: Mapped[str] = mapped_column(String(100),
                                        nullable=False, 
                                        unique=True,
                                        index=True)
    password: Mapped[str] = mapped_column(String(),
                                          nullable=False,
                                          index=True 
                                          )
    