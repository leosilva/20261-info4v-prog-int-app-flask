from app import db

class Usuario(db.Model):
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
    telefone = db.Column(db.String(20))
    posts = db.relationship('Post', back_populates='author')

