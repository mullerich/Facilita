from data_reader import leitor
from database_inject import *


dados = leitor('planilhas/2019_2.xlsx', 'inscricao_2019_2', ['NU_ANO', 'NU_EDICAO', 'CO_IES', 'NO_IES', 'SG_IES', 'DS_ORGANIZACAO_ACADEMICA', 'DS_CATEGORIA_ADM', 'NO_CAMPUS', 'NO_MUNICIPIO_CAMPUS', 'SG_UF_CAMPUS', 'DS_REGIAO_CAMPUS', 'CO_IES_CURSO', 'NO_CURSO', 'DS_GRAU', 'DS_TURNO'])
texto = insert('dados_base', dados)

print(texto)

