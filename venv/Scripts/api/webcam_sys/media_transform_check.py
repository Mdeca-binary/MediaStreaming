from aiortc import MediaStreamTrack

class VideoTransformTrack(MediaStreamTrack):
    kind = "video"
    def __init__(self, track, transform):
        self.track = track
        self.transform = transform
    
    async def recv(self):
        print(self.track)
        frame = await self.track.recv()
        print(frame)
        return frame