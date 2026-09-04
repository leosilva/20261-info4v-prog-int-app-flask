import secrets
import os
from pathlib import Path
from urllib.parse import quote_plus


BASE_DIR = Path(__file__).resolve().parent
SQLITE_DATABASE_PATH = BASE_DIR / "instance" / "app.sqlite3"


class Config:
    DB_PASSWORD = os.getenv("DB_PASSWORD", "labinfo")
    DB_USERNAME = os.getenv("DB_USERNAME", "root")
    SECRET_KEY = os.getenv("SECRET_KEY", secrets.token_hex(16))

    MYSQL_DATABASE_URI = f"mysql+mysqlconnector://{DB_USERNAME}:{quote_plus(DB_PASSWORD)}@localhost:3306/2026-info4v"
    SQLITE_DATABASE_URI = f"sqlite:///{SQLITE_DATABASE_PATH}"
    
    DATABASE_DRIVER = os.getenv("DATABASE_DRIVER", "sqlite").lower()
    if DATABASE_DRIVER == "mysql":
        SQLALCHEMY_DATABASE_URI = MYSQL_DATABASE_URI
    else:
        SQLALCHEMY_DATABASE_URI = SQLITE_DATABASE_URI
    