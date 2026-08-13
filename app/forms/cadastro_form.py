from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, ValidationError, Email

class CadastroUsuarioForm(FlaskForm):
    usuario = StringField('Usuário', validators=[DataRequired(message='Por favor, preencha o nome do usuário')])
    email = EmailField('Email', validators=[DataRequired(message='Por favor, preencha o email'), 
                                             Email(message="Email inválido")])
    senha = PasswordField('Senha', validators=[DataRequired(message='Por favor, preencha a senha')])
    submit = SubmitField('Entrar')
    
    def validate_username(self, field):
        if field.data.lower() == 'admin':
            raise ValidationError('O nome "admin" está reservado. Escolha outro.')