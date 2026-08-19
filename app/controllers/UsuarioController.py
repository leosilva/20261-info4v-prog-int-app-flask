from app.models import Usuario
from app import db
import sqlalchemy as sa


class UsuarioController:
    def salvar(formulario):
        usuario = Usuario()
        usuario.username = formulario["usuario"].data
        usuario.email = formulario["email"].data
        usuario.password_hash = formulario["senha"].data
        
        db.session.add(usuario)
        db.session.commit()
        return True
    
    def listar():
        query = sa.select(Usuario)
        return db.session.scalars(query)
    
    def listar_com_filtro():
        query = sa.select(Usuario).where(Usuario.username == 'leosilva')
        return db.session.scalar(query)
    
    def atualizar(usuario):
        if usuario:
            db.session.commit()
            print("Usuário atualizado com sucesso!")
        else:
            print("Usuário não encontrado.")
            
    def remover():
        usuario = db.session.get(Usuario, 7)
        if usuario:
            db.session.delete(usuario)
            db.session.commit()
            print("Usuário removido com sucesso!")
        else:
            print("Usuário não encontrado.")
            
    def buscar_por_email(email):
        query = sa.select(Usuario).where(Usuario.email == email)
        return db.session.scalar(query)
    
    def buscar_por_id(id):
        query = sa.select(Usuario).where(Usuario.id == id)
        return db.session.scalar(query)