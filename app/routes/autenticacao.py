from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from secrets import token_urlsafe
from urllib.parse import urljoin

from app import app

from app.forms.login_form import LoginForm
from app.services.AuthenticationService import AuthenticationService
from app.services.SuapAuthenticationService import SuapAuthenticationService

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
    session.clear()
    if not success:
        flash('Erro ao realizar o logout', category='error')
    return redirect(url_for('home'))


@autenticacao_bp.route('/login-suap')
def login_suap():
    state = token_urlsafe(32)
    redirect_uri = request.host_url.rstrip('/') + url_for('autenticacao.suap_callback')
    session['suap_oauth_state'] = state
    return redirect(SuapAuthenticationService.authorization_url(state, redirect_uri))


@autenticacao_bp.route('/suap/callback')
def suap_callback():
    state = session.pop('suap_oauth_state', None)
    if request.args.get('error') or not state or state != request.args.get('state', ''):
        flash('Falha na autenticação do SUAP.', 'error')
        return redirect(url_for('autenticacao.login'))

    # codigo de acesso temporario
    code = request.args.get('code')
    if not code:
        flash('Código de autorização do SUAP não recebido.', 'error')
        return redirect(url_for('autenticacao.login'))

    redirect_uri = request.host_url.rstrip('/') + url_for('autenticacao.suap_callback')
    tokens = SuapAuthenticationService.exchange_code(code, redirect_uri)
    if not tokens or not tokens.get('access_token'):
        flash('Não foi possível obter o token do SUAP.', 'error')
        return redirect(url_for('autenticacao.login'))

    dados = SuapAuthenticationService.meus_dados(tokens['access_token'])
    if dados is None:
        flash('Não foi possível consultar os dados do SUAP.', 'error')
        return redirect(url_for('autenticacao.login'))

    if AuthenticationService.login_suap(dados) is None:
        flash('Não foi possível vincular esta conta SUAP a um usuário local.', 'error')
        return redirect(url_for('autenticacao.login'))

    foto = dados.get('url_foto_75x100') or dados.get('url_foto') or dados.get('foto')
    foto_url = urljoin(app.config['SUAP_URL'] + '/', foto) if foto else None
    return render_template('suap_eu.html', title='Perfil SUAP', dados=dados, foto_url=foto_url)
