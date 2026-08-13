import secrets
from urllib.parse import quote_plus

class Config:
    DB_PASSWORD = "SENHA"
    SECRET_KEY = secrets.token_hex(16)
    SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://root:{quote_plus(DB_PASSWORD)}@localhost:3306/2026-info4v"