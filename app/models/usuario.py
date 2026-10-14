from app import db
from flask_login import UserMixin

class Usuario(db.Model, UserMixin):
    ROLES = [
        ('PADRAO', 'Padrão'),
        ('PLUS', 'Plus'),
    ]

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), 
                         index=True, 
                         unique=True,
                         nullable=False)
    email = db.Column(db.String(64), 
                        index=True, 
                        unique=True,
                        nullable=False)
    password_hash = db.Column(db.String(256))
    role = db.Column(db.String(16), nullable=False, default=ROLES[0][0])
    posts = db.relationship('Post', back_populates='author')
