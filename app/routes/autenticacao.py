from flask import Blueprint, flash, redirect, render_template, request, url_for

from app.forms.login_form import LoginForm
from app.services.AuthenticationService import AuthenticationService

autenticacao_bp = Blueprint("autenticacao", __name__)

@autenticacao_bp.route('/login', methods=['GET', 'POST'])
def login():
    formulario = LoginForm()
    if formulario.validate_on_submit():
        if AuthenticationService.login(formulario):
            flash("Login efetuado com sucesso!", "success")
            next_page = request.args.get('next')
            if not next_page:
                next_page = url_for('home')
            return redirect(next_page)
        else:
            flash("Usuário ou senha inválidos.", "error")
    return render_template('login.html', title='Login', form=formulario)


@autenticacao_bp.route('/logout')
def logout():
    success = AuthenticationService.logout()
    if not success:
        flash('Erro ao realizar o logout', category='error')
    return redirect(url_for('home'))