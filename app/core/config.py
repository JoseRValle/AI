""" import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_KEY = os.getenv("OPENAI_API_KEY")
ENVIRONMENT = os.getenv("ENVIRONMENT", "development") """

from pydantic import BaseSettings

class Settings(BaseSettings):
    openai_key: str
    environment: str = "development"

    class Config:
        env_file = "..\.env"

settings = Settings()