from app.models import Usuario
from app import db
import sqlalchemy as sa


class UsuarioService:
    def salvar(formulario):
        try:
            usuario = Usuario()
            formulario.populate_obj(usuario)
            db.session.add(usuario)
            db.session.commit()
            return True
        except Exception as e:
            print(f"Erro ao salvar usuário: {e}")
            db.session.rollback()
            return False
    
    def listar():
        query = sa.select(Usuario)
        return db.session.scalars(query)
    
    def listar_com_filtro():
        query = sa.select(Usuario).where(Usuario.username == 'leosilva')
        return db.session.scalar(query)
    
    def atualizar(usuario, formulário):
        try:
            formulário.populate_obj(usuario)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return False
            
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