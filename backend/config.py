import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    user: str = os.getenv("DB_USER")
    password: str = os.getenv("DB_PASS")
    host: str = os.getenv("DB_HOST")
    port: str = os.getenv("DB_PORT")
    name: str = os.getenv("DB_NAME")


settings = Settings()
