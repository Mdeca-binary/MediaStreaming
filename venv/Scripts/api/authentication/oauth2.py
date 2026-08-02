import jwt

from datetime import datetime, timedelta, timezone

from passlib.context import (CryptContext)

from models.model import UserModel
from models.schemas import UserBaseMode
from models.database import session
from configurations.config import JWTConfig

jwt_configuration = JWTConfig()

class Authentication:
    
    def __init__(self):
        self.password_context = CryptContext(
            schemes=["pbkdf2_sha256"],
            deprecated="auto", 
        )
        
    def encrypt_user_password(self, unhashed_pwd:str):
        # THIS METHOD HERE HASH'S  THE USER PASSWORD. 
        return \
            self.password_context.hash(unhashed_pwd)

    def decrypt_user_password(self, plain_password,  encrypted_password):
        # THIS METHOD CHECKS IF THE UNHASHED PASSWORD MATCHED
        # THE ENCRYPTED PASSWORD IS THE SAME AS.
        return \
            self.password_context.verify(plain_password, encrypted_password)
    