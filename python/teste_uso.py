from planilhas.data_reader import leitor_xlsx, listar_xlsx
from bd.database_inject import *
from bd.database_consult import request


colunas = ['NU_ANO', 'NU_EDICAO', 'CO_IES', 'NO_IES', 'SG_IES', 'DS_ORGANIZACAO_ACADEMICA', 'DS_CATEGORIA_ADM', 'NO_CAMPUS', 'NO_MUNICIPIO_CAMPUS', 'SG_UF_CAMPUS', 'DS_REGIAO', 'CO_IES_CURSO', 'NO_CURSO', 'DS_GRAU', 'DS_TURNO', 'DS_PERIODICIDADE', 'QT_SEMESTRE', 'QT_VAGAS_OFERTADAS', 'NU_PERCENTUAL_BONUS', 'TP_MODALIDADE', 'DS_MOD_CONCORRENCIA', 'PESO_REDACAO', 'NOTA_MINIMA_REDACAO', 'PESO_LINGUAGENS', 'NOTA_MINIMA_LINGUAGENS', 'PESO_MATEMATICA', 'NOTA_MINIMA_MATEMATICA', 'PESO_CIENCIAS_HUMANAS', 'NOTA_MINIMA_CIENCIAS_HUMANAS', 'PESO_CIENCIAS_NATUREZA', 'NOTA_MINIMA_CIENCIAS_NATUREZA', 'NU_MEDIA_MINIMA_ENEM']
path = './planilhas'

def teste_database_vagas_inject():
    print('\nIniciando!\n')
    for planilha in listar_xlsx(path+'/vagas/'):
        print(f'\nLendo planilha {planilha}...')
        dados = leitor_xlsx(path+'/vagas/'+planilha, colunas)  
        insert_dados_base("vagas", dados, colunas)
        
        print('OK!')                    
    
    print('\nConcluído!')


def teste_database_inscricoes_inject():
    path = './planilhas/inscricoes/'
    for planilha in listar_xlsx(path):
        print(f'\nLendo planilha {planilha}...', end=' ')
        dados = leitor_xlsx(path+planilha, colunas=['QT_INSCRICAO', 'NU_NOTACORTE'])
        dados_attrs = leitor_xlsx(path+planilha, colunas=['NU_ANO', 'NU_EDICAO', 'CO_IES_CURSO'])
        # atributos = attrs_dict(colunas=['NU_ANO', 'NU_EDICAO', 'CO_IES_CURSO'], dados=dados_attrs[:10])
        update_dados_base(['NU_ANO', 'NU_EDICAO', 'CO_IES_CURSO'], dados_attrs, dados)
        print('OK!')


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


teste_database_vagas_inject()
#teste_database_inscricoes_inject()