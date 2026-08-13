from app.models import Usuario
from app import db

class UsuarioController:
    def salvar(formulario):
        usuario = Usuario()
        usuario.username = formulario["usuario"].data
        usuario.email = formulario["email"].data
        usuario.password_hash = formulario["senha"].data
        
        db.session.add(usuario)
        db.session.commit()
        return True