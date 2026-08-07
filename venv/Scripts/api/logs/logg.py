import logging


class Logger:
    
    def __init__(self, root_name: str | None = None) -> None:
        self.log = logging.getLogger(name=root_name)


        