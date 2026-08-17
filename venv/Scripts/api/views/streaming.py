from typing import Annotated, List

from fastapi import (APIRouter, Form, UploadFile, 
                    File, HTTPException, status, Depends)
from fastapi.responses import JSONResponse

from stores.schemas import ImagePost
from configurations.image_settings import ImageProcessing

STREAMING = APIRouter(
    prefix="/streaming", 
    tags=["Streaming"]
)


@STREAMING.post("/upload")
async def postImages(caption: Annotated[str, Form()], 
                     picture: UploadFile = File(...)):
    processing =  ImageProcessing()
    # check the file extension (e.g [png, jpeg, jpg])
    if processing.checkExtension(picture):
        # RENAME THE IMAGE NAME
        processing.defaultRenameFilename(picture)
        # SAVE THE IMAGE
        # processing.saveImage(picture)
        return JSONResponse(
            status_code=status.HTTP_200_OK, 
            content={
                "image": picture.filename, 
                "caption": caption
            }
        )
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail="Extension not allowed ")
 
    

@STREAMING.get("/videostreaming")
def streamingVideoPageView():
    return