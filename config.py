import secrets
import os
from urllib.parse import quote_plus

class Config:
    DB_PASSWORD = os.getenv("DB_PASSWORD", "labinfo")
    DB_USERNAME = os.getenv("DB_USERNAME", "root")
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "3306")
    DB_NAME = os.getenv("DB_NAME", "2026-info4v")
    SECRET_KEY = os.getenv("SECRET_KEY", secrets.token_hex(16))

    SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{DB_USERNAME}:{quote_plus(DB_PASSWORD)}@{DB_HOST}:{DB_PORT}/{DB_NAME}"