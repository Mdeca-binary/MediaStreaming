import uuid

from datetime import datetime

# SQLALCHEMY FRAMEWORK
from sqlalchemy import (String, DateTime)
from sqlalchemy.orm import (mapped_column, Mapped)
# 
from .database import Base


class UserModel(Base):
    __tablename__ = "users"
    
    id: Mapped[uuid.UUID] = mapped_column(
                                        default=uuid.uuid4, 
                                        primary_key=True,
                                        index=True, 
                                        nullable=False, 
                                        unique=True)
    username: Mapped[str] = mapped_column(String(100),
                                        nullable=False, 
                                        unique=True,
                                        index=True)
    # HASHED PASSWORD
    hashed_pwd: Mapped[str] = mapped_column(String(500),
                                          nullable=False,
                                          index=True 
                                          )
    # THIS FOR WHEN THE ACCOUNT WAS CREATED
    account_created: Mapped[datetime] = mapped_column(
                                            DateTime, 
                                            default=datetime.now)
    # UPDATE EACH AND EVERY TIME THE LOGINS IN THE SITE
    update_visit: Mapped[datetime] = mapped_column(DateTime,
                                            default=datetime.now 
                                            )
    is_active: Mapped[bool] =  mapped_column(default=True)
    is_superuser: Mapped[bool] = mapped_column(default=False)
    is_anonymous: Mapped[bool] = mapped_column(default=False)
    
    def __repr__(self):
        return f"<id: {self.id}; username: {self.username}>"