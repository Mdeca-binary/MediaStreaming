import platform

from aiortc.contrib.media import MediaRelay

class Webcam:
    def __init__(self):
        self.option = {"video_size": "1280x720", 
                       "framerate": "30"}
        self.relay = MediaRelay()
        self.webcam = None
        
    @property    
    def os_available(self):
        """
        FUNCTION THAT DETECT THE OPERATING SYSTEM, 
        THAT IS USING THE APPLICATION.
        (e.g windows, linux or ios)
        """
        os_name = platform.system()
        return os_name
    
    def tracks(self):
        return None, self.relay.subscribe(self.webcam.video)
            

c = Webcam()
print(c.os_available)    

        
    
