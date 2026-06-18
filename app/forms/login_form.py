from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired(message='Por favor, preencha o nome do usuário')])
    password = PasswordField('Senha', validators=[DataRequired(message='Por favor, preencha a senha')])
    remember_me = BooleanField('Permanecer conectado')
    submit = SubmitField('Entrar')