from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, SelectField
from wtforms.validators import DataRequired, ValidationError, Email, Length, EqualTo
from app.models import Usuario
from app.services.UsuarioService import UsuarioService

class UsuarioForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired(message='Por favor, preencha o nome do usuário')])
    email = EmailField('Email', validators=[DataRequired(message='Por favor, preencha o email'), 
                                             Email(message="Email inválido")])
    role = SelectField('Perfil', choices=Usuario.ROLES, validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired(message='Por favor, preencha a senha'), Length(min=6)])
    password2 = PasswordField('Confirmar Senha', validators=[DataRequired(message='Por favor, confirme a senha'),
                                                                    EqualTo('password', message="As senhas não coincidem")])
    submit = SubmitField('Salvar')
    
    def validate_username(self, username):
        if not UsuarioService.checar_unicidade(username.data.strip(), 'username'):
            raise ValidationError('Nome de usuário já cadastrado.')

    def validate_email(self, email):
        if not UsuarioService.checar_unicidade(email.data.strip().lower(), 'email'):
            raise ValidationError('Email já cadastrado.')