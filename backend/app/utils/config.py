import os

class Config:
    def __init__(self):
        # App settings
        self.ROOTPATH = os.getenv("ROOTPATH")

config = Config()
