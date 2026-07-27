import uuid
import asyncio

from fastapi import Request
from fastapi.routing import APIRouter
from fastapi.responses import HTMLResponse, JSONResponse

from aiortc import RTCPeerConnection, RTCSessionDescription
from aiortc.contrib.media import MediaBlackhole, MediaRelay

from main import Jinja2Templates
from webcam_sys.webcam import Webcam
from webcam_sys.media_transform_check import VideoTransformTrack
from configurations.config import TemplatesConfig
from authentication.oauth2 import Authentication
from models.schemas import UserBaseMode

# INITIATING VIEWS / PAGES OF THE APP
VIEWS = APIRouter()

templates_config = TemplatesConfig()
templates = Jinja2Templates(directory=("%s"%templates_config.STORED_TO))

pcs = set()

@VIEWS.get("/", response_class=HTMLResponse, include_in_schema=False)
async def homepage(request: Request):
    return templates.TemplateResponse(request=request, name="home.html")

@VIEWS.get("/profile")
async def profile(request: Request):
    pass

@VIEWS.post("/profile")
async def profile(request: Request):
    pass

@VIEWS.get("/login")
@VIEWS.post("/login")
async def login(request: Request):
    pass

@VIEWS.get("/signup")
@VIEWS.post("/signup")
async def signup(user_registration: UserBaseMode):
    pass
    

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
