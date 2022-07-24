import pymysql

# Conectando ao banco de dadps
connection = pymysql.connect(host='localhost', user='root', password='', database='inscricoes_sisu')


def lista_para_texto(lista):
    texto = ''
    for elem in lista:
        if type(elem) == str and '"' in elem:   # Escape das aspas
            elem = elem.replace('"', r'\"')
        texto += f'"{elem}", '
    return texto[:-2]


def construtor_sql(tabela, colunas, dados):
    sql = f"INSERT INTO {tabela} VALUES (default, {lista_para_texto(dados)})"
    return sql


def insert(tabela, coluna, dados):
    cursor = connection.cursor()
    sql = construtor_sql(tabela, coluna, dados)
    cursor.execute(sql)  
    connection.commit()
    

def insert_dados_base(tabela, coluna, dados):
    """
    Insere no banco de dados registros de cursos que não são duplicáveis
    """
    for n, dado in enumerate(dados):
        print(f"\tCarregando... ({n/len(dados)*100:.2f}%)", end='\r')
        try:
            insert(tabela, coluna, dado)
        except Exception as e:
            if "Duplicate entry" in e.args[1]:  # Caso o dado já esteja no banco de dados
                pass 
            else:
                print(f"[ERRO] Linha {n} - {e}")
                print(f"\n[SQL] = {construtor_sql(tabela, coluna, dado)}")
                pause = input('\n[PRESSIONE ENTER PARA CONTINUAR]')

