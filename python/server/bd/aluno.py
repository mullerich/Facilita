from bd.database_inject import insert, update
from bd.database_consult import request


def registrar(nome, nascimento, email, senha):
    try:
        insert('usuarios', ['nome', 'nascimento', 'email', 'senha'], [nome, nascimento, email, senha])
        return True
    except Exception as e:
        if 'Duplicate entry' in str(e):
            print('Já existe uma conta com este email.')
        else:
            print(e)
        return False

def buscar(_id=None, email=None):
    return request('*', 'usuarios', f'id = {_id}' if _id else f"email = '{email}'", limit=1)


class Aluno():
    """Acessar e escrever informações sobre o aluno"""

    @property
    def is_authencticated(self):
        return True
    
    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __init__(self, _id):
        dados = buscar(_id)
        self.id = dados[0]
        self.nome = dados[1]
        self.nascimento = dados[2]
        self.email = dados[3]
        self.senha = dados[4]

        self.tipo_conta = dados[5]
        self.cidades = dados[6]
        self.notas = dados[7]
        self.turnos = dados[8]
        self.cotas = dados[9]
        self.grau = dados[10]
        self.pendencias = dados[11]


    def alterar(self, attrs):
        # Exemplo de uso: aluno.alterar({'cidades': '["Nova Friburgo", "Florestal", "Ouro Preto"]'})
        update('usuarios', attrs, f'id = {self.id}')

    def descricao(self):
        # Traz uma descrição resumida e em linguagem humana sobre o aluno
        print(f'O aluno {self.nome} (id={self.id}), nascido em {self.nascimento}, possui uma conta {self.tipo_conta}. Suas cidades de interesse são {self.cidades}')

