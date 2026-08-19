from app import app
from flask import render_template, redirect, flash, request
from app.forms.login_form import LoginForm
from app.forms.cadastro_form import CadastroUsuarioForm
from app.forms.buscar_form import BuscarUsuarioForm
from app.controllers.AuthenticationControllers import AuthenticationController
from app.controllers.UsuarioController import UsuarioController


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
            return redirect("/")
    return render_template("cadastro_usuario.html", form=formulario, title="Cadastro de Usuário")
    
@app.route("/listar", methods=['GET'])
def listar():
    usuarios = UsuarioController.listar()
    for u in usuarios:
        print(u.id, u.username, u.email)
    return render_template("index.html")

@app.route("/listar_com_filtro", methods=['GET'])
def listar_com_filtro():
    usuario = UsuarioController.listar_com_filtro()
    print(usuario.id, usuario.username, usuario.email)
    return render_template("index.html")


@app.route("/atualizar", methods=['GET'])
def atualizar():
    UsuarioController.atualizar()
    return render_template("index.html")


@app.route("/remover", methods=['GET'])
def remover():
    UsuarioController.remover()
    return render_template("index.html")

@app.route("/buscar", methods=['GET', 'POST'])
def buscar():
    formulario = BuscarUsuarioForm()
    if formulario.validate_on_submit():
        usuario = UsuarioController.buscar_por_email(formulario.email.data)
        print(usuario.id, usuario.username, usuario.email)
        usuario.email = "leo@email.com"
        UsuarioController.atualizar(usuario)
        
        usuario = UsuarioController.buscar_por_id(usuario.id)
        print(usuario.id, usuario.username, usuario.email)
        
        return render_template("index.html")
    return render_template("buscar_usuario.html", form=formulario)