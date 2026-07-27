from typing import LiteralString

from passlib.context import CryptContext

from fastapi.security import (
    OAuth2PasswordBearer, 
    OAuth2PasswordRequestForm, 
    SecurityScopes
)

from models.model import UserModel
from models.database import session

class Authentication:
    
    def __init__(self, username:LiteralString, password:LiteralString):
        self.username = username
        # THIS IS A PLAIN TEXT FROM USER-INPUT
        self.password = password
        self.hash_type = CryptContext(schemes=["bcrypt"], 
                                      deprecated="auto")
        self.user_database = UserModel
    
    @property
    def encrypt_user_password(self):
        return self.hash_type.hash(self.password)
    
    def verify_user_password(self, plain_password: LiteralString):
        return self.hash_type.verify(plain_password, self.encrypt_user_password)
    
    def check_username_exists(self, username:str):
        return username in \
            session.query(self.user_database).filter_by(username=username)
                
    def save_user_data(self):
        user = UserModel(
            username=self.username, 
            password=self.encrypt_user_password
        )
        with session:
            session.add(user)
            session.commit()
            session.refresh(user)
