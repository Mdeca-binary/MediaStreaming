from datetime import datetime

from typing import LiteralString

from passlib.context import CryptContext

from fastapi.security import (
    OAuth2PasswordBearer, 
    OAuth2PasswordRequestForm, 
    SecurityScopes
)

from models.model import UserModel
from models.schemas import UserBaseMode
from models.database import session

class Authentication():
    
    def __init__(self, username:str|None, 
                 unhashed_password:str|None):
        self.username = username
        self.unhashed_password = unhashed_password
        self.password_context = CryptContext(
            schemes=["bcrypt", "pbkdf2_sha256"],
            deprecated=["md5_crypt"]
        )
        # self.db = UserModel()

    def encrypt_user_password(self, unhashed_pwd:str):
        # THIS METHOD HERE HASH'S  THE USER PASSWORD. 
        return \
            self.password_context.hash(unhashed_pwd)

    def decrypt_user_password(self, encrypted_password):
        # THIS METHOD CHECKS IF THE UNHASHED PASSWORD MATCHED
        # THE ENCRYPTED PASSWORD IS THE SAME AS.
        return self.password_context.verify(self.unhashed_password, encrypted_password)
    
    def user_data(self):
        usr = {
            "%s"%(self.username): {
                "username": self.username, 
                "hashed_pwd": self.encrypt_user_password(unhashed_pwd=self.unhashed_password),  
                "account_created": datetime.now(),
                "update_visit": datetime.now()
            }
        }
        if self.username in usr:
            user_dict = usr[self.username]
        return UserBaseMode(**user_dict)
         
    
    def save_user_in_database(self):
        if self.username is not None:
            if self.username not in session.query(UserModel).filter_by(username=self.username):
                _password = self.encrypt_user_password(self.unhashed_password)
                usr = UserModel(
                    username=self.username, 
                    password=_password,
                    account_created=datetime.datetime.now(),
                    update_visit = datetime.datetime.now()
                )
                session.add(usr)
                session.commit()
        
        