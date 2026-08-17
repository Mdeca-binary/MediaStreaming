import os
import uuid 
import shutil
from pathlib import Path

from configurations.settings import ImageConfig

class ImageProcessing:
    
    def imageDimension(self, file):
        pass
    
    def defaultRenameFilename(self, file: str):
        name_of = file.filename
        # split filename in to two parts
        filename, ext = os.path.splitext(name_of)
        # rename the file using the uuid
        filename = "%s"%uuid.uuid4()
        # new name of the file
        name_of = f"{filename}{ext}"
        file.filename = name_of
        return file
    
    def checkFile(self, file:str):
        if file is None:
            raise FileN0otFoundError("%s: File is Valid.")
    
    def checkExtension(self, file):
        # checks if the file extension exists within the page allowed extension
        extensions = [".png", ".jpeg", ".jpg"]
        _file = Path(file.filename)
        if _file.suffix in extensions:
            return True
        return False
        
    def saveImage(self, file):
        path = ImageConfig()
        path = os.path.join(path.IMAGES, file.filename)
        with open(path, 'wb') as buffer:
            shutil.copyfileobj(file.file, buffer)
        return file