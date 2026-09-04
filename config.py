import secrets
import os
from urllib.parse import quote_plus
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
SQLITE_DATABASE_PATH = BASE_DIR / "instance" / "app.sqlite3"

class Config:
    DB_PASSWORD = os.getenv("DB_PASSWORD", "labinfo")
    DB_USERNAME = os.getenv("DB_USERNAME", "root")
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "3306")
    DB_NAME = os.getenv("DB_NAME", "2026-info4v")
    SECRET_KEY = os.getenv("SECRET_KEY", secrets.token_hex(16))
    CURRENT_DATABASE = os.getenv("CURRENT_DATABASE", "sqlite").lower()

    if CURRENT_DATABASE == "sqlite":
        SQLALCHEMY_DATABASE_URI = f"sqlite:///{SQLITE_DATABASE_PATH}"
    elif CURRENT_DATABASE == "mysql":
        SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{DB_USERNAME}:{quote_plus(DB_PASSWORD)}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
