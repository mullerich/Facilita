import pymysql

# Conectando ao banco de dadps
connection = pymysql.connect(host='localhost', user='root', password='', database='sisu')


def attrs_str(attrs_dict):
    string = ''
    for x in attrs_dict:
        string += f"{x} = '{attrs_dict[x]}', "
    return string[:-2]


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
    sql = f"INSERT INTO {tabela} {f'({lista_para_texto(colunas, aspas=False)})' if colunas else ''} VALUES ({lista_para_texto(dados)})"
    return sql


def construtor_sql_update(tabela, attrs, where=None):
    """Constroi uma string contendo código SQL para alterar um determinado dado em uma tabela"""
    sets = attrs_str(attrs)
    sql = f"UPDATE {tabela} SET {sets} {f'WHERE {where}' if where else ''}"
    print(sql)
    return sql


def insert(tabela, coluna, dados):
    executar_sql(construtor_sql_insert(tabela, coluna, dados))


def update(tabela, attrs, where=None):
    executar_sql(construtor_sql_update(tabela, attrs, where))
    
    