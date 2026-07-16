import os

# VIDEO STORAGE CONFIGURATION
class VideoConfig:
    # CURRENT DIR (e.g configuration/)
    _CURRENT_DIR = os.path.abspath(__file__)
    # ROOT DIR (e.g api/)
    _ROOT_DIR = os.path.dirname(os.path.dirname(_CURRENT_DIR))
    # APPOINTED DIR(e.g storage/video)
    STORED_TO = os.path.join(_ROOT_DIR, "storage", "video")
    