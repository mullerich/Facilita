from cmath import isnan
from numpy import nan
import pymysql
from bd.database_consult import request
import math


# Conectando ao banco de dadps
connection = pymysql.connect(host='localhost', user='root', password='', database='inscricoes_sisu')

def attrs_dict(colunas, dados):
    lista_atributos = {colunas[0]: dados[0], colunas[1]: dados[1], colunas[2]: dados[2]}
    return lista_atributos


def attrs_str(attrs_dict):
    string = ''
    for x in attrs_dict:
        string += f'{x} = {attrs_dict[x]} AND '
    return string[:-5]


def escape_aspas(texto):
    if type(texto) == str and '"' in texto:  
        texto = texto.replace('"', r'\"')
    return texto


def executar_sql(sql):
    cursor = connection.cursor()
    cursor.execute(sql)  
    connection.commit()


def lista_para_texto(lista, aspas=True):
    texto = ''
    for elem in lista:
        elem = escape_aspas(elem)
        if aspas:
            texto += f'"{elem}", '
        else:
            texto += f'{elem}, '
    return texto[:-2]


def construtor_sql_insert(tabela, colunas, dados):
    """Constroi uma string contendo código SQL para inserir um determinado dado em uma tabela"""
    
    sql = f"INSERT INTO {tabela} {f'(ID, {lista_para_texto(colunas, aspas=False)})' if colunas else ''} VALUES (default, {lista_para_texto(dados)})"
    return sql


def construtor_sql_update(tabela, attrs, where=None):
    """Constroi uma string contendo código SQL para alterar um determinado dado em uma tabel"""
    
    sets = attrs_str(attrs)
    sql = f"UPDATE {tabela} SET {sets} {f'WHERE {where}' if where else ''}"
    return sql


def insert(tabela, coluna, dados):
    executar_sql(construtor_sql_insert(tabela, coluna, dados))


def update(tabela, attrs, where=None):
    executar_sql(construtor_sql_update(tabela, attrs, where))
    

def insert_dados_base(tabela, dados, coluna=None):
    """
    Insere no banco de dados registros de cursos que não são duplicáveis
    """
    for n, dado in enumerate(dados):
        #print(f"\tCarregando... ({n/len(dados)*100:.2f}%)", end='\r')
        reiniciar = True
        while reiniciar:
            try:
                if len(dado) != len(coluna):    # Coluna bonus vazia
                    dado = list(dado)
                    dado.insert(18, "0")
                else:
                    if math.isnan(dado[18]):
                        dado[18] = 0
                if math.isnan(dado[17]):
                    dado[17] = 0
                insert(tabela, coluna, dado)
                reiniciar = False
            except Exception as e:
                if "Duplicate entry" in e.args[1]:  # Caso o dado já esteja no banco de dados
                    pass 
                else:
                    print(f"[ERRO] Linha {n} - {e}")
                    print(f"\n[SQL] = {construtor_sql_insert(tabela, coluna, dado)}")
                    reiniciar = True if input('\nDESEJA TENTAR NOVAMENTE? [S/N] -> ').upper() == 'S' else False
 

def update_dados_base(colunas, attrs, dados):
    print('\nIniciando [UPDATE]\n\n')
    for n, dado in enumerate(dados):
        print(f"\tCarregando... ({n/len(dados)*100:.2f}%)", end='\r')
        atributos = attrs_dict(colunas, list(attrs[n]))
        try:
            print(atributos)
            _id = request('ID', 'vagas', attrs_str(atributos), limit=1)
            print(_id)
        except Exception as e:
            print(f"[ERRO] Linha {n} - {e}")
            print(f"\n[SQL] = {construtor_sql_update('vagas', attrs_dict(colunas, dados))}")
            pause = input('')
        """try:
            update('vagas', attrs_str(atributos), f'ID = {_id}')
        except Exception as e:
            print(f"[ERRO] Linha {n} - {e}")
            print(f"\n[SQL] = {construtor_sql_update('vagas', attrs_dict(colunas, dados))}")
"""