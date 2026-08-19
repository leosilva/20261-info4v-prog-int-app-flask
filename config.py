import secrets
from urllib.parse import quote_plus

class Config:
    DB_PASSWORD = ""
    DB_USERNAME = "root"
    SECRET_KEY = secrets.token_hex(16)
    SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{DB_USERNAME}:{quote_plus(DB_PASSWORD)}@localhost:3306/2026-info4v"