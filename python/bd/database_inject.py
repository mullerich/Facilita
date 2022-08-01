import pymysql


# Conectando ao banco de dadps
connection = pymysql.connect(host='localhost', user='root', password='', database='inscricoes_sisu')

def escape_aspas(texto):
    if type(texto) == str and '"' in texto:  
        texto = texto.replace('"', r'\"')
    return texto


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
    """
    Constroi uma string contendo código SQL para inserir um determinado dado em uma tabela
    """
    sql = f"INSERT INTO {tabela} {f'(ID, {lista_para_texto(colunas, aspas=False)})' if colunas else ''} VALUES (default, {lista_para_texto(dados)})"
    return sql


def construtor_sql_update(tabela, attrs, where=None):
    """
    Constroi uma string contendo código SQL para alterar um determinado dado em uma tabela
    """
    sets = ""
    for k in attrs:
        value = escape_aspas(attrs[k])
        sets += f"{k} = '{value}', "
    sets = sets[:-2]
    sql = f"UPDATE {tabela} SET {sets} {f'WHERE {where}' if where else ''}"
    return sql


def insert(tabela, coluna, dados):
    cursor = connection.cursor()
    sql = construtor_sql_insert(tabela, coluna, dados)
    cursor.execute(sql)  
    connection.commit()
    

def insert_dados_base(tabela, dados, coluna=None):
    """
    Insere no banco de dados registros de cursos que não são duplicáveis
    """
    for n, dado in enumerate(dados):
        print(f"\tCarregando... ({n/len(dados)*100:.2f}%)", end='\r')
        reiniciar = True
        while reiniciar:
            try:
                insert(tabela, coluna, dado)
                reiniciar = False
            except Exception as e:
                if "Duplicate entry" in e.args[1]:  # Caso o dado já esteja no banco de dados
                    pass 
                else:
                    print(f"[ERRO] Linha {n} - {e}")
                    print(f"\n[SQL] = {construtor_sql_insert(tabela, coluna, dado)}")
                    reiniciar = True if input('\nDESEJA TENTAR NOVAMENTE? [S/N] -> ').upper() == 'S' else False
 
