from data_reader import leitor_xlsx, listar_xlsx
from database_inject import *


colunas = ['NU_ANO', 'NU_EDICAO', 'CO_IES', 'NO_IES', 'SG_IES', 'DS_ORGANIZACAO_ACADEMICA', 'DS_CATEGORIA_ADM', 'NO_CAMPUS', 'NO_MUNICIPIO_CAMPUS', 'SG_UF_CAMPUS', 'DS_REGIAO_CAMPUS', 'CO_IES_CURSO', 'NO_CURSO', 'DS_GRAU', 'DS_TURNO']
path = 'planilhas/inscricoes'

def teste_database_inject():
    print('\nIniciando!\n')
    for planilha in listar_xlsx(path):
        print(f'\nLendo planilha {planilha}...')
        dados = leitor_xlsx(path+'/'+planilha, colunas)   
        insert_dados_base("dados_base", colunas, dados)
        print('OK!')                    
    print('\nConcluído!')


teste_database_inject()
