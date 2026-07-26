import platform
from typing import Optional, Required

from aiortc import RTCPeerConnection, RTCRtpSender
from aiortc.contrib.media import MediaRelay, MediaPlayer

class Webcam:
    def __init__(self):
        self.option = {"video_size": "1280x720", 
                       "framerate": "30"}
        self.relay = None
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
        if self.relay is None:
            # IF THE O.SYSTEM IS WINDOWS THEN PERFORM THIS CODE HERE
            if self.os_available == "Windows":
                self.webcam = MediaPlayer("video=Integrated Camera", 
                                        format="dshow", options=self.option)
            # OR PERFORM THIS CODE FOR IOS X
            elif self.os_available == "Darwin":
                self.webcam = MediaPlayer("default:none", format="avfoundation", 
                                        options=self.option)
            # OR THIS CODE FOR LINUX O.SYSTEM
            else:
                self.webcam = MediaPlayer("/dev/video0", format="v412", 
                                        options=self.option)
        return None, self.relay.subscribe(self.webcam.video)
    
    def codec(self, pc: RTCPeerConnection, sender: RTCRtpSender, _codec: str):
        kind = _codec.split("/")[0]
        codecs = RTCRtpSender.getCapabilities(kind).codecs
        transceiver = next(t for t in pc.getTransceivers()
                        if t.sender == sender)
        transceiver.setCodecPreferences(
            [codec for codec in codecs if codecs.mimeType == _codec]
        )
             
