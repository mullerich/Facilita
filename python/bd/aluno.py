from database_inject import insert, update
from database_consult import request


def registrar(nome, nascimento, email):
    try:
        insert('usuarios', ['nome', 'nascimento', 'email'], [nome, nascimento, email])
    except Exception as e:
        if 'Duplicate entry' in str(e):
            print('Já existe uma conta com este email.')
        else:
            print(e)


def buscar(_id=None, email=None):
    return request('*', 'usuarios', f'id = {_id}' if _id else f"email = '{email}'", limit=1)


class Aluno():
    """Acessar e escrever informações sobre o aluno"""

    def __init__(self, _id):
        dados = buscar(_id)
        self.id = dados[0]
        self.nome = dados[1]
        self.nascimento = dados[2]
        self.email = dados[3]

        self.tipo_conta = dados[4]
        self.cidades = dados[5]
        self.notas = dados[6]
        self.turnos = dados[7]
        self.cotas = dados[8]
        self.grau = dados[9]
        self.pendencias = dados[10]


    def alterar(self, attrs):
        # Exemplo de uso: aluno.alterar({'cidades': '["Nova Friburgo", "Florestal", "Ouro Preto"]'})
        update('usuarios', attrs, f'id = {self.id}')

    def descricao(self):
        # Traz uma descrição resumida e em linguagem humana sobre o aluno
        print(f'O aluno {self.nome} (id={self.id}), nascido em {self.nascimento}, possui uma conta {self.tipo_conta}. Suas cidades de interesse são {self.cidades}')

