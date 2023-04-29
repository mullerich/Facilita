from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager, login_user
from flask_hashing import Hashing
from models.forms import LoginForm, CadastroForm, preferenciasVagasForm, preferenciasCursoForm
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


@app.route('/preferencias/curso', methods=['POST', 'GET'])
def preferencias_curso():
    form = preferenciasCursoForm()
    if form.validate_on_submit():
        cursos = form.cursos.data.split(',')
        bacharelado, licenciatura = form.bacharelado.data, form.licenciatura.data
        tecnologico, abi = form.tecnologico.data, form.abi.data
        print(cursos, bacharelado, licenciatura, tecnologico, abi)
        # Implementar uma função que redireciona de acordo com as pendencias
        return redirect(url_for('preferencias_vagas'))
    
    return render_template('dados_compl_1.html', form=form)


@app.route('/preferencias/vagas', methods=['GET', 'POST'])
def preferencias_vagas():
    form = preferenciasVagasForm()
    if form.validate_on_submit():
        matutino = form.matutino.data
        vespertino = form.vespertino.data
        noturno = form.noturno.data
        integral = form.integral.data
        ead = form.ead.data

        escola_publica = form.escola_publica.data
        preto_pardo = form.preto_pardo.data
        indigena = form.indigena.data
        deficiente = form.deficiente.data
        trans_trav = form.trans_trav.data
        quilombola = form.quilombola.data

        print(matutino, vespertino, noturno, integral, ead)
        print(escola_publica, preto_pardo, indigena, deficiente, trans_trav, quilombola)
        return redirect(url_for('home'))

    return render_template('dados_compl_2.html', form=form)


app.run()
