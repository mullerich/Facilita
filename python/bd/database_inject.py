import pymysql
from bd.database_consult import request


# Conectando ao banco de dadps
connection = pymysql.connect(host='localhost', user='root', password='', database='inscricoes_sisu')

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """Mostra uma barra de progresso"""
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()


def attrs_dict(colunas, dados):
    lista_atributos = {colunas[0]: dados[0], colunas[1]: dados[1], colunas[2]: dados[2]}
    return lista_atributos


def attrs_str(attrs_dict):
    string = ''
    for x in attrs_dict:
        string += f'{x} = {attrs_dict[x]}, '
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
    sql = f"INSERT INTO {tabela} {f'(ID, {lista_para_texto(colunas, aspas=False)})' if colunas else ''} VALUES (default, {lista_para_texto(dados)})"
    return sql


def construtor_sql_update(tabela, attrs, where=None):
    """Constroi uma string contendo código SQL para alterar um determinado dado em uma tabela"""
    sets = attrs_str(attrs)
    sql = f"UPDATE {tabela} SET {sets} {f'WHERE {where}' if where else ''}"
    return sql


def insert(tabela, coluna, dados):
    executar_sql(construtor_sql_insert(tabela, coluna, dados))


def update(tabela, attrs, where=None):
    executar_sql(construtor_sql_update(tabela, attrs, where))
    

def insert_dados_base(tabela, dados, coluna=None):
    """Insere no banco de dados registros de cursos que não são duplicáveis"""
    for n, dado in enumerate(dados):
        printProgressBar(n, len(dados), prefix="\t└─ Carregando:", suffix="Completo", length=50)
        reiniciar = True
        # Loop para inserir o dado, caso haja um erro de fácil resolução no bd.
        while reiniciar:
            try:
                insert(tabela, coluna, dado)
                reiniciar = False
            except Exception as e:
                print(f"[ERRO] Linha {n} - {e}")
                print(f"\n[SQL] = {construtor_sql_insert(tabela, coluna, dado)}")
                reiniciar = True if input('\nDESEJA TENTAR NOVAMENTE? [S/N] -> ').upper() == 'S' else False
 

def update_dados_base(dados):
    for n, dado in enumerate(dados):
        printProgressBar(n, len(dados), prefix="\t│\t└─ Carregando:", suffix="Completo", length=50)
        
        # Verifica a existência dos dados base na tabela
        NU_ANO, NU_EDICAO, CO_IES_CURSO, DS_TURNO, DS_MOD_CONCORRENCIA  = dado[0], dado[1], dado[2], dado[3], dado[4]
        _id = request(select='ID', _from='vagas', where=f"NU_ANO = {NU_ANO} AND NU_EDICAO = {NU_EDICAO} AND CO_IES_CURSO = {CO_IES_CURSO} AND DS_TURNO = '{DS_TURNO}' AND DS_MOD_CONCORRENCIA = '{DS_MOD_CONCORRENCIA}'", limit=1)

        # Caso haja, altera o registro inserindo os dados
        if _id:
            NU_NOTACORTE, QT_INSCRICAO = dado[5], dado[6]
            try:
                update('vagas', {'NU_NOTACORTE': NU_NOTACORTE, 'QT_INSCRICAO': QT_INSCRICAO}, where=f'ID = {_id}')
            except Exception as e:
                print(f"[ERRO] Linha {n} - {e}")
                print(f"\n[SQL] = {construtor_sql_update('vagas', {'NU_NOTACORTE': NU_NOTACORTE, 'QT_INSCRICAO': QT_INSCRICAO}, where=f'ID = {_id}')}")

        else:
            print('[ERRO] Não houve registro para', dado)

