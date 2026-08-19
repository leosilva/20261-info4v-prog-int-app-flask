from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField


class BuscarUsuarioForm(FlaskForm):
    email = EmailField('Email')
    submit = SubmitField('Buscar')