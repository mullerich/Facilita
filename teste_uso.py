from data_reader import leitor, open_excel, which_column
from database_inject import *


planilha = 'planilhas/2019_2.xlsx'
folha = 'inscricao_2019_2'
colunas = ['NU_ANO', 'NU_EDICAO', 'CO_IES', 'NO_IES', 'SG_IES', 'DS_ORGANIZACAO_ACADEMICA', 'DS_CATEGORIA_ADM', 'NO_CAMPUS', 'NO_MUNICIPIO_CAMPUS', 'SG_UF_CAMPUS', 'DS_REGIAO_CAMPUS', 'CO_IES_CURSO', 'NO_CURSO', 'DS_GRAU', 'DS_TURNO']


def teste_database_inject():
    print('Iniciando!')
    datasheet = open_excel(planilha, folha, which_column(planilha, folha, colunas))
    dados = leitor(datasheet)   
    tamanho = len(dados) 
    for cont, dado in enumerate(dados):
        print(f"Em andamento... ({cont}/{tamanho})", end='\r')
        
        try:
            insert('dados_base', colunas, dado)
        except Exception as e:
            if "Duplicate entry" in e.args[1]:  # Caso o dado já esteja no banco de dados
                pass 
            else:
                print(f"[ERRO] - Linha {cont}", e)
                break
                
    print('Concluído!')


teste_database_inject()
