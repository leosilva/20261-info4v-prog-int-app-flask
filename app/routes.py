from app import app
from flask import render_template, redirect, flash, request
from app.forms.login_form import LoginForm
from app.forms.cadastro_form import CadastroUsuarioForm
from app.controllers.AuthenticationControllers import AuthenticationController
from app.controllers.UsuarioController import UsuarioController
from app.models import Usuario
from app import db


@app.route("/")
def home():
    usuario = {
        "nome": "Leo",
        "produtos": ["Banana", "Abacaxi", "Melancia"]
    }
    esta_logado = True
    return render_template("index.html", 
                           pessoa = usuario, 
                           usuario_logado = esta_logado)

@app.route("/sobre")
def sobre():
    return "Página Sobre"

@app.route("/index2")
def index2():
    return render_template('index2.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    formulario = LoginForm()
    if formulario.validate_on_submit():
        if AuthenticationController.login(formulario):
            flash("Login efetuado com sucesso!")
            return redirect('/')
        else:
            flash("Erro nas credenciais.")
            return redirect('/login')
    return render_template('login.html', title='Login', form=formulario)


@app.route('/inserir', methods=['GET', 'POST'])
def inserir():
    formulario = CadastroUsuarioForm()
    if formulario.validate_on_submit():
        if UsuarioController.salvar(formulario):
            print("Usuário criado com sucesso!")
            return render_template("index2.html")
    return render_template("index2.html")
    