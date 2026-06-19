from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, ValidationError

class LoginForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired(message='Por favor, preencha o nome do usuário')])
    password = PasswordField('Senha', validators=[DataRequired(message='Por favor, preencha a senha')])
    remember_me = BooleanField('Permanecer conectado')
    submit = SubmitField('Entrar')
    
    def validate_username(self, field):
        if field.data.lower() == 'admin':
            raise ValidationError('O nome "admin" está reservado. Escolha outro.')