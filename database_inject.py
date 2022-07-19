import pymysql

# Conectando ao banco de dadps
connection = pymysql.connect(host='localhost', user='root', password='', database='inscricoes_sisu')


def lista_para_texto(lista, crase=True):
    texto = ''
    for elem in lista:
        if crase:
            texto += f'`{elem}`, '
        else:
            texto += f'{elem}, '
    
    return texto[:-2]


def insert(tabela, dados):
    """
    os dados são da forma:
    {
        col1: [el1, el2, ...., eln],
        col2: [el1, el2, ..., eln],
        ...
        coln: [el1, el2, ..., eln]
    }
    """

    with connection:
        #with connection.cursor() as cursor:
        sql = f"INSERT INTO {tabela} ({lista_para_texto(list(dados.keys()))}) VALUES"
        colunas = list(dados.keys())
        len_rows = len(dados[colunas[0]])
        for num_row in range(len_rows):
            print(num_row)
            row = [dados[x][num_row] for x in colunas]
            sql += f' ({lista_para_texto(row)}),'
        sql = sql[:-1]
    
    return sql

