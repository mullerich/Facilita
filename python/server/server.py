from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager, login_user
from flask_hashing import Hashing
from models.forms import LoginForm, CadastroForm
import bd.aluno as aluno


app = Flask(__name__)
app.config.from_object('config')

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(_id):
    return aluno.Aluno(_id)

hashing = Hashing(app)

# ------------------ PÁGINAS ----------------------

@app.route("/")
def home():
    return "<p>Hello, World!</p>"


@app.route("/login", methods=['POST', 'GET'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        email, senha = form.email.data, form.senha.data
        _id = aluno.buscar(email=email)[0]
        user = aluno.Aluno(_id)
        if hashing.check_value(user.senha, senha):
            login_user(user)
            print('Usuário Logado')
            return redirect(url_for('home'))
    return render_template('login.html', form=form)


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro_page():
    form = CadastroForm()
    if form.validate_on_submit():
        nome, nascimento, email, senha = form.nome.data, form.nascimento.data, form.email.data, form.senha.data
        senha_hash = hashing.hash_value(senha)
        if aluno.registrar(nome, nascimento, email, senha_hash):
            print('Aluno registrado!')
            
        return redirect(url_for('login_page'))
        
    return render_template('cadastro.html', form=form)


app.run()
