import os

class Config:
    def __init__(self):
        # App settings
        self.ROOTPATH = os.getenv("ROOTPATH", "/")
        self.APP_ENVIRONMENT = os.getenv("APP_ENVIRONMENT", "test")

        # POSTGRES database related config
        self.POSTGRES_USER = os.getenv("POSTGRES_USER", "bunhub_user")
        self.POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "securepassword")
        self.POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
        self.POSTGRES_DATABASE = os.getenv("POSTGRES_DATABASE", "bunhub")
        self.POSTGRES_PORT = int(os.getenv("POSTGRES_PORT", "5432"))

config = Config()
