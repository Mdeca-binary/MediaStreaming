import uuid
import asyncio

from datetime import timedelta, timezone

from typing import Annotated

from fastapi import Request, Depends, Form, HTTPException, Response
from fastapi.routing import APIRouter
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.security import (
    OAuth2PasswordBearer, 
    OAuth2PasswordRequestForm,
    SecurityScopes
)

from aiortc import RTCPeerConnection, RTCSessionDescription
from aiortc.contrib.media import MediaBlackhole, MediaRelay

from main import Jinja2Templates
from webcam_sys.webcam import Webcam
from webcam_sys.media_transform_check import VideoTransformTrack
from configurations.config import TemplatesConfig, JWTConfig, OAUTH2_SCHEME
from authentication.oauth2 import Authentication
from models.schemas import UserBaseMode, Token, UserLogin
from models.database import session
from models.model import UserModel


# INITIATING VIEWS / PAGES OF THE APP
VIEWS = APIRouter()
JWT_CONFIG = JWTConfig()
auth = Authentication()

templates_config = TemplatesConfig()
templates = Jinja2Templates(directory=("%s"%templates_config.STORED_TO))

pcs = set()

# @VIEWS.get("/")
@VIEWS.get("/")
async def homepage(request: Request):
    
    # return templates.TemplateResponse(request=request, name="home.html")
    return {'user': request.cookies.get('username')}

@VIEWS.get("/profile")
async def profile(request: Request):
    pass

@VIEWS.post("/profile")
async def profile(request: Request):
    pass

@VIEWS.post("/login")
async def login(form_data: Annotated[OAuth2PasswordRequestForm,  Depends()]):
    user_data = {
        "username": form_data.username, 
        "password": form_data.password
    }
    stored_user_data = session.query(UserModel).filter_by(username=user_data["username"]).first()
    if stored_user_data.username is not None:
        if auth.decrypt_user_password(user_data["password"], stored_user_data.hashed_pwd) is True:
            user_dict = UserLogin(**user_data) 
            return {"access_token": user_dict.username, "token_type": "bearer"}
        else:
            raise HTTPException(status_code=400, detail="incorrect password.")
    else:
        raise HTTPException(status_code=400, detail="username doesn't exist.")
        
# @VIEWS.get("/signup")        
@VIEWS.post("/signup")
async def signup(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_form_data = {
        "username": form_data.username, 
        "password": form_data.password
    }
    users_data_in_db = session.query(UserModel).filter_by(username=user_form_data["username"]).first()
    print(users_data_in_db is not None)
    if users_data_in_db is not None:
        raise HTTPException(status_code=400, detail="User exist, please create another username.")
    
    encrypt_password = auth.encrypt_user_password(unhashed_pwd=user_form_data["password"])
    user_form_data["password"] = encrypt_password
    
    user_dicts = UserBaseMode(
        username=user_form_data["username"], 
        hashed_pwd=user_form_data["password"], 
    )
    store_user_in_db = UserModel(
        id=user_dicts.user_id, 
        username=user_dicts.username, 
        hashed_pwd=user_dicts.hashed_pwd, 
        account_created=user_dicts.account_created, 
        update_visit=user_dicts.update_visit, 
        is_active=user_dicts.is_active, 
        is_superuser=user_dicts.is_superuser, 
        is_anonymous=user_dicts.is_anonymous
    )
    # session.add(store_user_in_db)
    # session.commit()
    re = RedirectResponse(url="/", status_code=303)
    re.set_cookie(key="username", value=user_dicts.username)
    return re


@VIEWS.post("/logout")
async def logout(request: Request):
    pass

@VIEWS.post("/offer", include_in_schema=False)
async def offer(request: Request):
    params = await request.json()
    
    constraints = {"sdp": params["sdp"], "type": params["type"]}
    
    # offer = RTCSessionDescription(sdp=constraints["sdp"], type=constraints["type"])
    # PEER CONNECTION
    pc = RTCPeerConnection()
    
    @pc.on("datachannel")
    def on_channel(channel):
        @channel.on("message")
        def on_message(message):
            print(f"Received message: {message}")
            channel.send(f"Pong: {message}")
    await pc.setRemoteDescription(
        RTCSessionDescription(sdp=constraints["sdp"], type=constraints["type"])
    )
    answer = await pc.createAnswer()
    await pc.setLocalDescription(answer)
    return {'sdp': pc.localDescription.sdp, 'type': pc.localDescription.type}
