from planilhas.data_reader import leitor_xlsx, listar_xlsx
from bd.database_inject import *
from bd.database_consult import request


colunas = ['NU_ANO', 'NU_EDICAO', 'CO_IES', 'NO_IES', 'SG_IES', 'DS_ORGANIZACAO_ACADEMICA', 'DS_CATEGORIA_ADM', 'NO_CAMPUS', 'NO_MUNICIPIO_CAMPUS', 'SG_UF_CAMPUS', 'DS_REGIAO_CAMPUS', 'CO_IES_CURSO', 'NO_CURSO', 'DS_GRAU', 'DS_TURNO']
path = './planilhas/vagas'

def teste_database_inject():
    print('\nIniciando!\n')
    for planilha in listar_xlsx(path):
        print(f'\nLendo planilha {planilha}...')
        dados = leitor_xlsx(path+'/'+planilha)   
        insert_dados_base("vagas", dados)
        print('OK!')                    
    print('\nConcluído!')


def teste_verificacao():
    print('\nIniciando!\n')
    falhas = []
    for planilha in listar_xlsx(path):
        print(f'\nLendo planilha {planilha}...')
        dados = leitor_xlsx(path+'/'+planilha, ['CO_IES_CURSO'])  
        for dado in dados: 
            busca = request('ID', 'dados_base', f"'CO_IES_CURSO' = {dado[0]}")
            if busca != ():
                falhas.append(f"{planilha} - CO_IES_CURSO = {dado[0]}")
        print('OK!')                    
    print(f'\nConcluído com {len(falhas)} falhas!\n')
    for falha in falhas: 
        print('\t', falha)

    # FUNCIONANDO COM 0 FALHAS!!!


teste_database_inject()