"""
Esse programa tem o intuito de ler as tabelas de relatório disponibilizadas pelo INEP
https://sisu.mec.gov.br/#/relatorio#onepage, coletar os dados e transformar em 'json'

Os dados a serem extraídos são:

NU_ANO: Ano do processo seletivo
NU_EDICAO:	Número da edição do processo seletivo no ano de referência
CO_IES:	Código da instituição de ensino superior confome informações do cadastro e-MEC
NO_IES:	Nome da instituição de ensino superior confome informações do cadastro e-MEC
SG_IES:	Sigla da instituição de ensino superior confome informações do cadastro e-MEC
DS_ORGANIZACAO_ACADEMICA:	Descrição da organização acadêmica da instituição de ensino superior confome informações do cadastro e-MEC
DS_CATEGORIA_ADM:	Descrição da categoria administrativa da instituição de ensino superior confome informações do cadastro e-MEC
NO_CAMPUS:	Nome do campus da instituição de ensino superior confome informações do cadastro e-MEC
NO_MUNICIPIO_CAMPUS:	Nome do município do campus da instituição de ensino superior confome informações do cadastro e-MEC
SG_UF_CAMPUS:	Sigla da unidade da federação (UF) na qual está localizada o campus da instituição de ensino superior confome informações do cadastro e-MEC
DS_REGIAO_CAMPUS:	Descrição da região na qual está localizada o campus da instituição de ensino superior confome informações do cadastro e-MEC
CO_IES_CURSO:	Código do curso da instituição de ensino superior confome informações do cadastro e-MEC
NO_CURSO:	Nome do curso da instituição de ensino superior confome informações do cadastro e-MEC
DS_GRAU:	Grau do curso da instituição de ensino superior confome informações do cadastro e-MEC
DS_TURNO:	Turno do curso da instituição de ensino superior confome informações do cadastro e-MEC
TP_MODALIDADE:	Tipo da modalidade da oferta do curso no processo seletivo
DS_MOD_CONCORRENCIA:	Descrição do tipo da modalidade de concorrência ofertada para o curso no processo seletivo
NU_PERCENTUAL_BONUS:	Percentual de bônus definido para as ações afirmativas próprias das IES
QT_VAGAS_CONCORRENCIA:	Quantidade de vagas ofertadas naquela modalidade
NU_NOTACORTE:	Nota de corte da modalidade/curso conforme o resultado da chamada regular. A nota de corte é sempre igual a nota do último candidato classificado na última vaga ofertada para a modalidade/curso escolhida. Na modalidade de bônus a nota de corte é a mesma da modalidade ampla concorrência do mesmo curso porque as pessoas que se inscreveram na modalidade bônus concorrem pelas vagas ofertadas para ampla concorrência do mesmo curso/grau/turno/campus/IES. Alguns cursos podem não apresentar nota de corte pois não tiveram número de inscritos pelo menos igual ao número de vagas ou porque tiveram poucos inscritos e alguns desses inscritos tiveram seleção na 1ª opção de curso e, portanto, não têm sua nota considerada para sua 2ª opção de inscrição
QT_INSCRICAO:	Quantidade de inscrições para a modalidade
"""

from openpyxl import load_workbook

def leitor(nome_arquivo, nome_folha, colunas=[]):
    """
    Lê um arquivo excel e retorna os dados separados por coluna.

    Exemplo de retorno:
        {
            NU_ANO: [2019, 2019],
            DS_GRAU: ['Bacharelado', 'Licenciatura'],
            QT_INSCRICAO: [234, 726]
        }

    Itens de mesma posição fazem parte do mesmo dado.
    """

    excel_data = load_workbook(nome_arquivo, read_only=True)
    datasheet = excel_data[nome_folha]     # Folha inscricao_2019_2
    num_colunas = datasheet.max_column
    num_linhas = datasheet.max_row
    num_linhas = 5
    
    dados = {}
    if colunas == []:
        colunas_usadas = [x for x in range(1, num_colunas+1)]
        for c in range(1, num_colunas+1):
            dados[f"{datasheet.cell(1, c).value}"] = []
    
    else:
        colunas_usadas = []
        for c in range(1, num_colunas+1):
            if datasheet.cell(1, c).value in colunas:
                dados[f"{datasheet.cell(1, c).value}"] = []
                colunas_usadas.append(c)

    for col in colunas_usadas:
        titulo_coluna = datasheet.cell(1, col).value
        for row in range(2, num_linhas+2):
            dados[titulo_coluna].append(datasheet.cell(row=row, column=col).value)

    return dados


# print(leitor('planilhas/2019_2.xlsx', 'inscricao_2019_2', ['NU_ANO', 'NU_EDICAO', 'CO_IES']))

# leitura = leitor('planilhas/2019_2.xlsx', 'inscricao_2019_2', ['NU_ANO', 'NU_EDICAO', 'CO_IES', 'NO_IES', 'SG_IES', 'DS_ORGANIZACAO_ACADEMICA', 'DS_CATEGORIA_ADM', 'NO_CAMPUS', 'NO_MUNICIPIO_CAMPUS', 'SG_UF_CAMPUS', 'DS_REGIAO_CAMPUS', 'CO_IES_CURSO', 'NO_CURSO', 'DS_GRAU', 'DS_TURNO'])
