from flask_wtf import FlaskForm
from wtforms import StringField, DateField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    senha = PasswordField('senha', validators=[DataRequired()])


class CadastroForm(FlaskForm):
    nome = StringField('nome', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    nascimento = DateField('nascimento', validators=[DataRequired()])
    senha = PasswordField('senha', validators=[DataRequired()])
